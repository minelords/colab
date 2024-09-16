import re

def first():
    with open('url1.html','r',encoding='utf-8') as f:
        lines=f.readlines()
    with open('url1.html','w',encoding='utf-8') as f:
        for line in lines:
            try:
                url=re.findall(r'.*?(http.*?index.m3u8)',line)[0]
                title=re.findall(r'<br>(.*?):http.*?',line)[0]
                final=f'<br><a href="https://www.dplayer.top/index.php?url={url}" target="_blank">{title}</a>:{url}'
                print(final)
                f.write(final+"\n")
            except:
                print(line)
                f.write(line)
                
def inittt(i):
    with open(f'url{i}.html','r',encoding='utf-8') as f:
        lines=f.readlines()                
    
    with open(f'url{i}.html','w',encoding='utf-8') as f:
        lines = lines[:-2]
        titles=[]
        urls=[]
        for line in lines:
            try:    
                title=re.findall(r'<p>(.*?)：</p>',line)[0]
                titles.append(title)
            except:
                try:
                    url=re.findall(r'<p>(http.*?)</p>',line)[0] 
                    urls.append(url)
                except:
                    f.write(line)        
        for title,url in zip(titles,urls):
            final=f'<p><a href="https://www.dplayer.top/index.php?url={url}"  target="_blank">{title}</a><p>\n<p>{url}</p>\n'
            f.write(final)
        f.write("</body>\n</html>")
        
def yw(i):
    with open(f'url{i}.html','r',encoding='utf-8') as f:
        lines=f.readlines()                
    
    with open(f'url{i}.html','w',encoding='utf-8') as f:
        lines = lines[:-2]
        titles=[]
        urls=[]
        for line in lines:
            try:    
                title=re.findall(r'<p>(.*?)：</p>',line)[0]
                titles.append(title)
            except:
                try:
                    url=re.findall(r'<p>(http.*?)</p>',line)[0] 
                    urls.append(url)
                except:
                    pass        
        for title,url in zip(titles,urls):
            final=f'<p><a href="https://www.dplayer.top/index.php?url={url}"  target="_blank">{title}</a><p>\n<p>{url}</p>\n'
            f.write(final)
from urllib.parse import  quote_plus

def bj():
    with open("cngirl.txt",'r',encoding='utf-8') as f:
        lines=f.readlines()
        
    with open('cngirlll.html','w',encoding='utf-8') as f:
        for line in lines:
            l=line.split("###")
            html=f"""<a href="https://www.dplayer.top/index.php?url={quote_plus(l[0])}">
                    <img src="{l[1]}" alt="Image 1">
                    <span>{l[2]}</span>
            </a>
            """
            f.write(html)
        
def switch():
    with open('sex.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

    # 开始构建HTML内容
    html_content = ""

    # 遍历每一行，将其转换为HTML段落
    for line in content:
        if line.strip():  # 处理非空行
            html_content += f"<p>{line.strip()}</p>\n"
        else:  # 处理空行，转换为换行符
            html_content += "<br>\n"
            
bj()