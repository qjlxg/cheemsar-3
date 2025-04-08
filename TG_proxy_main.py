# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy
# v2ray_collecto
# coding=utf-8
import base64
import requests
import re
import time
import os
import threading
from tqdm import tqdm
import random, string
import datetime
from time import sleep
import chardet

#试用机场链接
home_urls =(
'https://sub1.pingboy.top',
'https://5.44.251.106',
'https://api.heima2u.com',
'https://www.kuaidog010.top',
'http://47.101.67.199:6699',
'http://subssr.xfxvpn.me',
'https://terfghtll.dashuai.us',
'https://sub.flygfw.top',
'http://51.255.173.39',
'https://api.shanhai.one',
'https://cloud.jisuba.live',
'https://bp123.xyz',
'https://xingclouds.xyz',
'https://xingcloud.pwzvd.cn',
'https://aimanman.me',
'https://sjy001.xyz',
'https://cloud.jsfx.tech',
'https://cloud.gougou.live',
'https://tlnnm.ntgdada.top',
'https://xes.al',
'https://10run.vip',
'https://hssl8088.icu',
'https://yihicloud.top',
'https://xjyjc.top',
'https://nekros.us',
'https://laosijicc.top',
'https://pianyijichang.com',
'https://haitunyun1.cfd',
'https://chuifengji.top',
'https://haitunyun2.cfd',
'https://sytcloud.top',
'https://wuxianjc.top',
'https://cmy.ewwnu.cn',
'https://xiaofeixia.me',
'https://by.yunduanjc.top',
'https://yunduanjc.top',
'https://kuailejc.xyz',
'https://changyouvpn.top',
'https://w02.qytl2web01.cc',
'https://kaikaixinxin.me',
'https://magicm.sbs',
'https://magicm.link',
'https://kn.kngtxy.top',
'https://magicm.top',
'https://666v.xyz',
'https://magicm.cc',
'https://magicm.click',
'https://console.veseai.com',
'https://dash.minizz.online',
'https://xyz.noseisei.com',
'https://abc.noseisei.com',
'https://passwall.link',
'https://zxc.noseisei.com',
'https://bailian.site',
'https://dgg.idsduf.com',
'https://a.yousu.cc',
'https://c.yousu.cc',
'https://b.yousu.cc',
'https://surfgb8.world',
'http://vyy.idsduf.com',
'https://www.xbyun.live',
'https://thecom.today',
'https://panel.moku.pro',
'https://xmfwww.cc',
'https://rtx.al',
'https://zzz.youxuan.wiki',
'https://www.jiasuniu.com',
'https://ddddd.site',
'https://1.vyunyun.top',
'https://maple.icu',
'https://xx-ai.io',
'https://www.aaaspeed.cc',
'https://zqjc.org',
'http://1run.vip',
'https://vpn.sudatech.store',
'https://sq9xy6.cpminig.com',
'https://app.cloudlion.me',
'https://moluo.cloud',
'https://www.susucloud.net',
'https://zhuiyun.top',
'https://b.xiaow.cc',
'https://hktix.net',
'https://www.mangshe.org',
'https://www.eyujichang.com',
'https://db.shellnet.net',
'https://jisovpn.site',
'https://niercloud.com',
'https://qingyun.zybs.eu.org',
'https://www.xfxssr.com',
'https://iii1.caty.moe',
'https://www.xiercloud.uk',
'https://snangua.com',
'https://client.3i.lol',
'https://plinkc.top',
'https://lanmaoyun.icu',
'https://wumaojichang.com',
'https://cococloud.online',
'https://www.dukadi.one',
'https://yingwuyun.top',
'https://www.yunanyun.com',
'https://app.lwjyj.com',
'https://www.hurricanerelay.net',
'https://xueyejiasu.com',
'https://leflycloud.com',
'https://www.tencloud.net',
'https://ktmcloud.net',
'https://ktmcloud1.top',
'https://ktmcloud.shop',
'https://ktmcloud.top',
'https://ktmcloud.one',
'https://ktmcloud.link',
'https://ktmcloud.vip',
'https://xianyuwangluo.top',
'https://ai.totwo.top',
'https://ai.totwo.link',
'https://a1.darkforest.cloud',
'https://darkforest.cloud',
'https://cxk.lol',
'https://syq.tw',
'https://sanxijichang.com',
'https://store.kakocloud.pro',
'https://sidog.top',
'https://gfw.best',
'https://chiguayun.org',
'https://chiguayun.net',
'https://chiguayun.com',
'https://guanwang.me',
'https://liulangdiqiu.cc',
'https://qianggewangluo.com',
'https://themeserver.cutecloudone.de',
'https://bobapi.kkhhyytt.cn',
'http://nanbei.buzz',
'http://nanbei.cloud',
'https://www.1365365.xyz',
'https://bt3.one',
'https://tblack.xyz',
'https://shuimu.site',
'https://tcity8.top',
'https://liangyuandian.club',
'https://reborn.kaochang.ltd',
'https://fastestcloud.xyz',
'https://www.xihoogsi.com',
'https://fastcloud.store',
'https://neko.services',
'https://kuaiqiangshou.xyz',
'https://neko.yuriuni.com',
'https://vpn.gunyoung.top',
'https://my.legeth.com',
'http://dash.legeth.com',
'https://gossr.pw',
'http://onefall.top',
'http://www.paopao.dog',
'https://app.birds.hk',
'https://www.1655ss.com',
'https://22.lownet.xyz',
'https://wayen.eu',
'https://jk-cloud.net',
'https://www.9yuan.top',
'https://www.fooksun.xyz',
'https://home.caiyun.mom',
'https://caiyun.wiki',
'http://ov2rayo.top',
'http://17yxyy.cc',
'https://54fxp.xyz',
'https://haoba.cloud',
'https://mianmd.ninja',
'https://www.gogocloud.cyou',
'https://planb.cat',
'https://v.cheerfun.dev',
'https://www.cantonx.com',
'https://air.yoyoss.xyz',
'https://91yun.buzz',
'https://portal.buddhajumpsoverthewall.com',
'http://network2.magic-in-china.com',
'https://kedouair.top',
'http://oceancloud.asia',
'https://ssr.giize.com',
'https://www.wkyun1688.com',
'https://air.misakano.eu.org',
'https://yhcvpn.xyz',
'https://starlink.to',
'https://www.dageyun.net',
'https://apidagecloud.com',
'https://www.starlink9527.xyz',
'https://bajie.info',
'https://bajie.pw',
'https://8rkt.xyz',
'https://58rocket.com',
'https://api.dashsp.top',
'https://miaona.co',
'https://miaona.org',
'https://miaona.xyz',
'https://latiao.club',
'https://58sd.net',
'https://latiao.us',
'https://latiao.buzz',
'https://glados.network',
'https://glados.one',
'https://bityun.org',
'http://bityun.org',
'http://sub.chbjpw.mobi',
'https://www.58mdss.com',
'https://88catnet.com',
'https://mdss.cloud',
'https://www.99catnet.com',
'https://glados.space',
'https://panel.keleofficial.com',
'https://a02.qytvipaff.pro',
'https://fengwo.pro',
'https://a.kpyun.live',
'https://一家机场.com',
'https://悟空机场.com',
'https://app.jingfan.me',
'https://巅峰机场.com',
'https://优惠机场.com',
'https://五分机场.live',
'https://便宜机场.co',
'https://app.cloudog.me',
'https://xn--wtq35pfyd55o.co',
'https://xn--mes91t7ofgnw.com',
'https://xn--4oq11ryli3rg.com',
'https://www.kuaidog006.top',
'https://gy888.xyz',
'https://gy777.xyz',
'https://dobcloud.com',
'http://qingyunti.cc',
'https://www.hj522.top',
'https://www.hj521.top',
'https://sy.niaoniao.co',
'https://pkq.xlm.plus',
'https://www.naiunet.com',
'https://mpddt.top',
'https://fengcheyun.xyz',
'https://dash.catnet.uk',
'https://一个机场.com',
'https://xn--4gqvd492adjr.com',
'https://epclub.xyz',
'https://66yun.lat',
'https://yl.hq12.top',
'https://myaqiqi.top',
'https://myxiongadi.top',
'https://anydoor.cloudns.ch',
'https://api.mail.tm',
'https://anydoor.eu.org',
'https://ansuyun.xyz',
'https://nyxen.org',
'https://moluo.fun',
'https://cainiao999.top',
'https://www.23800.top',
'https://inlook.me',
'https://w03.qytweba07.cc',
'https://fly-cloud.top',
'https://666.xnphf.cn',
'https://www.vfast.life',
'https://fxy.pw',
'https://fxyjs.fun',
'https://fqqcqat.qytvipaff.cc',
'https://lesubiu.net',
'https://api.lesubiu.net',
'https://cainiao88.top',
'https://dfjc.xyz',
'https://falcoonline.xyz',
'https://npccloud.top',
'https://stashbox1.top',
'https://iepl.io',
'https://qingsiyun.top',
'https://bailian.uk',
'https://myyan.flmweb.cc',
'https://lanyan.flmweb.cc',
'https://my.cloudlion.me',
'http://154.19.242.131:8881',
'https://baiyangxing.com',
'https://hjvip.cc',
'https://a123.buzz',
'https://jiasuniu.com',
'http://sub.kjdjakskl.cyou',
'https://svip.xingheyun.sbs',
'http://wuxianjc.top',
'http://kuailejc.xyz',
'http://changyouVPN.top',
'https://tuanzi.xyz',
'http://bailian.site',
'http://xueyejiasu.com',
'http://yl.hq12.top',
'https://1.dishuyun.top',
'https://qytnody.qingyunti.cc',
'https://xbvpn.vip',
'https://www.moakt.com/zh',


)
#文件路径
update_path = "./sub/"
#所有的clash订阅链接
end_list_clash = []
#所有的v2ray订阅链接
end_list_v2ray = []
#所有的节点明文信息
end_bas64 = []
#获得格式化后的链接
new_list = []
#永久订阅
e_sub = ['']
#频道
urls =[]
#线程池
threads = []
#机场链接
plane_sub = ['']
#机场试用链接
try_sub = []
#获取频道订阅的个数
sub_n = -25
#试用节点明文
end_try = []

#获取群组聊天中的HTTP链接
def get_channel_http(url):
    headers = {
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://t.me/s/oneclickvpnkeys',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        url, headers=headers)
    #print(response.text)
    pattren = re.compile(r'"https+:[^\s]*"')
    url_lst = pattren.findall(response.text)
    #print('获取到',len(url_lst),'个网址')
    #print(url_lst)
    return url_lst


#对bs64解密
def jiemi_base64(data):  # 解密base64
    # 对 Base64 编码后的字符串进行解码，得到字节字符串
    decoded_bytes = base64.b64decode(data)
    # 使用 chardet 库自动检测字节字符串的编码格式
    encoding = chardet.detect(decoded_bytes)['encoding']
    # 将字节字符串转换为字符串
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str

#判读是否为订阅链接
def get_content(url):
    #print('【获取频道',url,'】')
    url_lst = get_channel_http(url)
    #print(url_lst)
    #对链接进行格式化
    for i in url_lst:
        result = i.replace("\\", "").replace('"', "")
        if result not in new_list:
            if "t" not in result[8]:
                if "p" not in result[-2]:
                    new_list.append(result)
    #print(new_list)
    #print("共获得", len(new_list), "条链接")
    #获取单个订阅链接进行判断
    i = 1
    try:
        new_list_down = new_list[sub_n::]
    except:
        new_list_down = new_list[len(new_list) * 2 // 3::]
    #print("共获得", len(new_list_down), "条链接")
    #print('【判断链接是否为订阅链接】')
    for o in new_list_down:
        try:
            res = requests.get(o)
            #判断是否为clash
            try:
                skuid = re.findall('proxies:', res.text)[0]
                if skuid == "proxies:":
                    #print(i, ".这是个clash订阅", o)
                    end_list_clash.append(o)
            except:
                #判断是否为v2
                try:
                    #解密base64
                    peoxy = jiemi_base64(res.text)
                    #print(i, ".这是个v2ray订阅", o)
                    end_list_v2ray.append(o)
                    end_bas64.extend(peoxy.splitlines())
                    
                #均不是则非订阅链接
                except:
                    #print(i, ".非订阅链接")
                    pass
        except:
            #print("第", i, "个链接获取失败跳过！")
            pass
        i += 1
    return end_bas64

#写入文件
def write_document():
    if e_sub == [] or try_sub == []:
        print("订阅为空请检查！")
    else:
        #永久订阅
        random.shuffle(e_sub)
        for e in e_sub:
            try:
                res = requests.get(e)
                proxys=jiemi_base64(res.text)
                end_bas64.extend(proxys.splitlines())
            except:
                print(e,"永久订阅出现错误❌跳过")
        print('永久订阅更新完毕')
        #试用订阅
        random.shuffle(try_sub)
        for t in try_sub:
            try:
                res = requests.get(t)
                proxys=jiemi_base64(res.text)
                end_try.extend(proxys.splitlines())
            except Exception as er:
                print(t,"试用订阅出现错误❌跳过",er)
        print('试用订阅更新完毕',try_sub)
        #永久订阅去重
        end_bas64_A = list(set(end_bas64))
        print("去重完毕！！去除",len(end_bas64) - len(end_bas64_A),"个重复节点")
        #永久订阅去除多余换行符
        bas64 = '\n'.join(end_bas64_A).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #试用去除多余换行符
        bas64_try = '\n'.join(end_try).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #获取时间，给文档命名用
        t = time.localtime()
        date = time.strftime('%y%m', t)
        date_day = time.strftime('%y%m%d', t)
        #创建文件路径
        try:
            os.mkdir(f'{update_path}{date}')
        except FileExistsError:
            pass
        txt_dir = update_path + date + '/' + date_day + '.txt'
        #写入时间订阅
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(bas64)
        file.close()       
        
        #减少获取的个数
        r = 1
        length = len(end_bas64_A)  # 总长
        m = 8  # 切分成多少份
        step = int(length / m) + 1  # 每份的长度
        for i in range(0, length, step):
            print("起",i,"始",i+step)
            zhengli = '\n'.join(end_bas64_A[i: i + step]).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
            #将获得的节点变成base64加密，为了长期订阅
            obj = base64.b64encode(zhengli.encode())
            plaintext_result = obj.decode()
            #写入长期订阅
            file_L = open("Long_term_subscription"+str(r), 'w', encoding='utf-8')
            file_L.write(plaintext_result)
            r += 1
        #写入总长期订阅
        obj = base64.b64encode(bas64.encode())
        plaintext_result = obj.decode()
        file_L = open("Long_term_subscription_num", 'w', encoding='utf-8')
        file_L.write(plaintext_result)
        #写入试用订阅
        obj_try = base64.b64encode(bas64_try.encode())
        plaintext_result_try = obj_try.decode()
        file_L_try = open("Long_term_subscription_try", 'w', encoding='utf-8')
        file_L_try.write(plaintext_result_try)
        #写入README
        with open("README.md", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        now_time = datetime.datetime.now()
        TimeDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index in range(len(lines)):
            try:
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
                    lines.pop(index+4)
                    lines.pop(index+4)
                    lines.insert(index+4, f'Updata：`{TimeDate}`\n')
                    lines.insert(index+4, f'### Try the number of high-speed subscriptions: `{len(try_sub)}`\n')
                if lines[index] == '>Trial subscription：\n': # 目标行内容
                    lines.pop(index)
                    lines.pop(index)
                """
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
                """
            except:
                #print("写入READ出错")
                pass
        #写入试用订阅
        for index in range(len(lines)):
            try:
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        #lines.insert(index+n-1, f'\n>')
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
            except:
                print("写入试用出错")
        
        with open("README.md", 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            f.write(data)
        print("合并完成✅")
        try:
            numbers =sum(1 for _ in open(txt_dir))
            print("共获取到",numbers,"节点")
        except:
            print("出现错误！")
        
    return

#获取clash订阅
def get_yaml():
    print("开始获取clsah订阅")
    urls = []
    n = 1
    for i in urls:
        response = requests.get(i)
        #print(response.text)
        file_L = open("Long_term_subscription" + str(n) +".yaml", 'w', encoding='utf-8')
        file_L.write(response.text)
        file_L.close()
        n += 1
    print("clash订阅获取完成！")

#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com' or current_url == 'https://seeworld.pro'  or current_url == 'https://www.jwckk.top'or current_url == 'https://vvtestatiantian.top':
                try:
                    fan_res = requests.post(
                        f'{current_url}/api/v1/passport/auth/register', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    #print(auth_data)
                    fan_header = {
                        'Origin': current_url,
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': current_url,
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        f'{current_url}/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    #print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        f'{current_url}/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={fan_res.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as result:
                    print(result)
                    break
            else:
                try:
                    response = requests.post(
                        current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as e:
                    print("获取订阅失败",e)
            i += 1

            
  
def get_kkzui():
    # ========== 抓取 kkzui.com 的节点 ==========
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
        article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)"',res.text).groups()[0]
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]
        print(sub_url)
        e_sub.append(sub_url)
        print("获取kkzui.com完成！")
    except:
        print("获取kkzui.com失败！")
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://www.cfmem.com/search/label/free",headers=headers)
        article_url = re.search(r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html",res.text).group()
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'>v2ray订阅链接&#65306;(.*?)</span>',res.text).groups()[0]
        print(sub_url)
        try_sub.append(sub_url)
        e_sub.append(sub_url)
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    print("========== 开始获取机场订阅链接 ==========")
    get_sub_url()
    print("========== 开始获取kkzui.com订阅链接 ==========")
    get_kkzui()
    print("========== 开始获取频道订阅链接 ==========")
    for url in urls:
        #print(url, "开始获取......")
        thread = threading.Thread(target=get_content,args = (url,))
        thread.start()
        threads.append(thread)
        #resp = get_content(get_channel_http(url))
        #print(url, "获取完毕！！")
    #等待线程结束
    for t in tqdm(threads):
        t.join()
    print("========== 准备写入订阅 ==========")
    res = write_document()
    clash_sub = get_yaml()
    print("========== 写入完成任务结束 ==========")
