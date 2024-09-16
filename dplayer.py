
import requests
from fake_useragent import UserAgent
import time
import random
import re
import execjs
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import urllib.parse

def sexbjcam(url):
    
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
    }
    embed='https://recordplay.biz/e/qwhggoycvztg'
    resp=requests.get(url=embed,headers=headers)
    source=resp.text
    script=re.findall(r'eval(.*?split\(\'\|\'\)\)\))',source)[0]
    js_code=f"function get_url(){{return {script}}}"
    context = execjs.compile(js_code).call('get_url')
    result=re.findall(r'file:"(http.*?)"',context)[0]
    return result 

def pornavhd(url):
    
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    embed=re.findall(r'<IFRAME SRC="(http.*?)"',html)[0]
    resp=requests.get(url=embed,headers=headers)
    source=resp.text
    script=re.findall(r'eval(.*?split\(\'\|\'\)\)\))',source)[0]
    js_code=f"function get_url(){{return {script}}}"
    context = execjs.compile(js_code).call('get_url')
    result=re.findall(r'file:"(http.*?)"',context)[0]
    return result 

def sexkbj(url):
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    embed=re.findall(r'<IFRAME SRC="(http.*?)"',html)[0]
    resp=requests.get(url=embed,headers=headers)
    source=resp.text
    script=re.findall(r'eval(.*?split\(\'\|\'\)\)\))',source)[0]
    js_code=f"function get_url(){{return {script}}}"
    context = execjs.compile(js_code).call('get_url')
    result=re.findall(r'file:"(http.*?)"',context)[0]
    return result 

def netflav(url):
    
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'referer':'https://netflav.com/'
    }
    #返回html信息
    html=requests.get(url,headers=headers).text
    data=re.findall(r'id="__NEXT_DATA__" type="application/json">(.*?)</script>',html)[0]
    json_data=json.loads(data)
    description=json_data['props']['initialState']['video']['data']['description']
    title=json_data['props']['initialState']['video']['data']['title_zh']
    src=json_data['props']['initialState']['video']['data']['src']
    previewVideo=json_data['props']['initialState']['video']['data']['previewVideo']

    resp=requests.get(url=src,headers=headers)
    source=resp.text
    script=re.findall(r'eval(.*?split\(\'\|\'\)\)\))',source)[0]
    js_code=f"function get_url(){{return {script}}}"
    context = execjs.compile(js_code).call('get_url')
    result=re.findall(r'file:"(http.*?)"',context)[0]
    return result 


def xgroovy(url):
    
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    }
    resp=requests.get(url,headers=headers)
    html=resp.text
    result=re.findall(r'id="main_video".*?src="(http.*?)"',html)[0]
    return result
    
def camcam(url):
    
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
    }

    resp=requests.get(url,headers=headers)
    html=resp.text
    result=re.findall(r'contentURL" content="(.*?)"',html)[0]
    return result

def baoyu(url):
    headers={
    "UserAgent":f'{UserAgent.random}',
    "Referer":"http://23.224.77.18"
    }

    resp=requests.get(url,headers=headers)
    code=re.findall(r'<script type="text/javascript">var player_data=(.*?)</script>',resp.text)
    data=json.loads(code[0])
    urlstr=data['url']
    # 定义密钥、IV 和加密的 URL 字符串
    key = '9q4h7kt7skwsc9af1qmwy14jkfq2biab'
    iv = '6b3gslw69k6eazmw'

    # Base64 解码
    urlstr = base64.b64decode(urlstr)

    # 转换密钥和IV
    key1 = key.encode('latin1')
    iv1 = iv.encode('latin1')

    # 创建 AES 解密对象
    cipher = AES.new(key1, AES.MODE_CBC, iv1)

    # 解密数据
    decrypted = unpad(cipher.decrypt(urlstr), AES.block_size).decode('utf-8')

    # 解析 URL 字符串
    urlstrs = urllib.parse.unquote(decrypted).split(',')

    # 定义 URL 模板
    workurl = 'https://cdn-m.asujp.com:59888/f'
    vodplay = f'{workurl}/{urlstrs[0]}/{urlstrs[1]}/{urlstrs[2]}/play.m3u8?_KS={urlstrs[3]}&_KE={urlstrs[4]}'
    return vodplay
    
if __name__=='__main__':
    #print(camcam('https://camcam.cc/asian-cam-ac2024932/'))
    #print(sexkbj('https://sexkbj.com/2024/09/05/kbj24090507_ch4465_sexkbj/'))
        print(baoyu('https://x115vz3w86ph9hli.com:58009/index.php/vod/play/id/163839/sid/1/nid/1.html'))
