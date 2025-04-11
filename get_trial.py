```python
import os 
from concurrent.futures import ThreadPoolExecutor 
from datetime import timedelta 
from random import choice, randint 
from time import time 
from urllib.parse import urlsplit, urlunsplit 

from apis import PanelSession, TempEmail, guess_panel, panel_class_map 
from subconverter import gen_base64_and_clash_config, get 
from utils import (clear_files, g0, keep, list_file_paths, list_folder_paths, 
 rand_id, read, read_cfg, remove, size2str, str2timestamp, 
 timestamp2str, to_zero, write, write_cfg) 

def safe_run(func, *args, **kwargs):
    """
    A wrapper function to run a function safely, ignoring all errors.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error occurred in {func.__name__}: {e}")
        return None

def get_sub(session: PanelSession, opt: dict, cache: dictstr, liststr): 
    url = cache['sub_url']0] 
    suffix = ' - ' + g0(cache, 'name') 
    if 'speed_limit' in opt: 
        suffix += ' ⚠️限速 ' + opt['speed_limit'] 
    try: 
        info, *rest = safe_run(get, url, suffix)
        if not info:
            origin = urlsplit(session.origin):2] 
            url = '|'.join(urlunsplit(origin + urlsplit(part)2:]) for part in url.split('|')) 
            info, *rest = safe_run(get, url, suffix)
            cache['sub_url']0] = url
        if not info and hasattr(session, 'get_sub_info'): 
            session.login(cache['email']0]) 
            info = safe_run(session.get_sub_info)
        return info, *rest 
    except Exception as e:
        print(f"Error in get_sub: {e}")
        return None,

def should_turn(session: PanelSession, opt: dict, cache: dictstr, liststr]]): 
    if 'sub_url' not in cache: 
        return 1, 
    
    now = time() 
    try: 
        info, *rest = safe_run(get_sub, session, opt, cache)
        if not info:
            return 1,  # Assuming need to turn if no info is retrieved
    except Exception as e:
        msg = str(e)
        if '邮箱' in msg and ('不存在' in msg or '禁' in msg or '黑' in msg):
            if (d := cache['email']0].split('@')1]) not in ('gmail.com', 'qq.com', g0(cache, 'email_domain')):
                cache['banned_domains'].append(d)
            return 2, 
        return 1,  # Assuming need to turn if an error occurs
    
    return int( 
        not info 
        or opt.get('turn') == 'always' 
        or float(info['total']) - (float(info['upload']) + float(info['download'])) < (1 << 28) 
        or (opt.get('expire') != 'never' and info.get('expire') and str2timestamp(info.get('expire')) - now < ((now - str2timestamp(cache['time']0])) / 7 if 'reg_limit' in opt else 2400)) 
    ), info, *rest 

def _register(session: PanelSession, email, *args, **kwargs): 
    try: 
        return safe_run(session.register, email, *args, **kwargs) 
    except Exception as e: 
        print(f"Error in _register: {e}")
        return None

def _get_email_and_email_code(kwargs, session: PanelSession, opt: dict, cache: dictstr, liststr]]): 
    while True: 
        tm = TempEmail(banned_domains=cache.get('banned_domains')) 
        try: 
            email = kwargs['email'] = tm.email 
        except Exception as e: 
            print(f"Error in _get_email_and_email_code (getting email): {e}")
            return None
        try: 
            safe_run(session.send_email_code, email)
        except Exception as e:
            msg = str(e)
            if '禁' in msg or '黑' in msg:
                cache['banned_domains'].append(email.split('@')1])
                continue
            print(f"Error in _get_email_and_email_code (sending email code): {e}")
            return None
        email_code = tm.get_email_code(g0(cache, 'name'))
        if not email_code:
            cache['banned_domains'].append(email.split('@')1])
            print(f"Error in _get_email_and_email_code (getting email code): Timeout")
            return None
        kwargs['email_code'] = email_code 
        return email 

def register(session: PanelSession, opt: dict, cache: dictstr, liststr]], log: list) -> bool: 
    kwargs = keep(opt, 'name_eq_email', 'reg_fmt', 'aff') 
    
    if 'invite_code' in cache: 
        kwargs['invite_code'] = cache['invite_code']0] 
    elif 'invite_code' in opt: 
        kwargs['invite_code'] = choice(opt['invite_code'].split()) 
    
    email = kwargs['email'] = f"{rand_id()}@{g0(cache, 'email_domain', default='gmail.com')}" 
    while True: 
        if not (msg := safe_run(_register, session, **kwargs)):
            if g0(cache, 'auto_invite', 'T') == 'T' and hasattr(session, 'get_invite_info'):
                if 'buy' not in opt and 'invite_code' not in kwargs:
                    session.login()
                    try:
                        code, num, money = safe_run(session.get_invite_info)
                    except Exception as e:
                        if g0(cache, 'auto_invite') == 'T':
                            log.append(f'{session.host}({email}): {e}')
                        if '邀请' in str(e):
                            cache['auto_invite'] = 'F'
                            return False
                    if 'auto_invite' not in cache:
                        if not money:
                            cache['auto_invite'] = 'F'
                            return False
                    balance = session.get_balance()
                    plan = session.get_plan(min_price=balance + 0.01, max_price=balance + money)
                    if not plan:
                        cache['auto_invite'] = 'F'
                        return False
                    cache['auto_invite'] = 'T'
                    cache['invite_code'] = code, num]
                    kwargs['invite_code'] = code
                session.reset()
            
            if 'email_code' in kwargs:
                email = safe_run(_get_email_and_email_code, kwargs, session, opt, cache)
                if not email:
                    return False
            else:
                email = kwargs['email'] = f"{rand_id()}@{email.split('@')1]}"
            
            if (msg := safe_run(_register, session, **kwargs)):
                break
            
            if 'invite_code' in kwargs:
                if 'invite_code' not in cache or int(cache['invite_code']1]) == 1 or randint(0, 1):
                    session.login()
                    safe_run(try_buy, session, opt, cache, log)
                    try:
                        cache['invite_code'] = [*safe_run(session.get_invite_info):2]]
                    except Exception as e:
                        if 'invite_code' not in cache:
                            cache['auto_invite'] = 'F'
                        else:
                            log.append(f'{session.host}({email}): {e}')
