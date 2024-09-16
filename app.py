
from flask import Flask, render_template, request, jsonify
from dplayer import *
import urllib.parse
import requests
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
CORS(app)


@app.route('/get-url', methods=['GET'])
def get_url():
    url = request.args.get('url', '')
    # 根据输入的 URL 或选中的标签生成新的 URL
    m3u8_url = process_url(url)
    new_url = 'https://www.dplayer.top/index.php?url=' + urllib.parse.quote(m3u8_url)

    return jsonify({'newUrl': new_url})

@app.route('/baoyu-url', methods=['GET'])
def boayu_url():
    resp=requests.get(url="http://23.224.77.18/go.js")
    url=re.findall(r"top.location = '(https://.*?)/",resp.text)[0]
    return jsonify({"url": url})

def process_url(url):
    # 根据 URL 生成新的 URL
    # 这里简单地返回输入的 URL，你可以根据需要修改它
    # 这里可以添加更多的逻辑来处理不同的 URL
    if 'sexbjcam' in url:
        return sexbjcam(url)  # 替换为实际 URL
    elif 'pornavhd' in url:
        return pornavhd(url)  # 替换为实际 URL
    elif 'sexkbj' in url:
        return sexkbj(url)  # 替换为实际 URL
    elif 'netflav' in url:
        return netflav(url) # 替换为实际 URL
    elif 'xgroovy' in url:
        return xgroovy(url)  # 替换为实际 URL
    elif 'camcam' in url:
        return camcam(url)  # 替换为实际 URL
    elif '/sid/1/nid/1.html' in url:
        return baoyu(url)
    else:
        return url

@app.route('/')
def index():
    return render_template('index.html')
    
app.run(host='0.0.0.0')
