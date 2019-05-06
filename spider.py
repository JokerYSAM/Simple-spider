import re
import time
import json
import random
import requests
from bs4 import BeautifulSoup
#https://img001.yayxcc.com/images/comic/61/121460/
def get_html(url):
    response=requests.get(url)
    return response.content

def parse_html(html,n):
    count=0
    soup=BeautifulSoup(html,features='html.parser')
    body=soup.find('body')
    script=body.find('script')
    script = str(script).replace("var ", '"')
    script = str(script).replace('<script>;', '{')
    script = str(script).replace(" '", '" ')
    script = str(script).replace(" ", '')
    script = str(script).replace("=", '":')
    script = str(script).replace(";", ',')
    script = str(script).replace(",,", ',')
    script = str(script).replace(";;", '; ')

    script = str(script).replace(',</script>', '}')
    scrip=json.loads(script)
    list=scrip["chapterImages"]
    for i in list:
        imgurl='https://img001.yayxcc.com/images/comic/61/121{0}/'.format(n)+str(i)

        download(imgurl)
def download(imgurl):
    global count
    html=requests.get(imgurl)
    print('downloading the {0} picture'.format(count))
    with open(r'C:\Users\jokerYSAM\Desktop\touxin\{0}.jpg'.format(count),'wb') as f:
        time.sleep(random.uniform(0,1))
        for chunk in html.iter_content(128):
            f.write(chunk)
    f.close()
    count += 1



def main():
    global count
    count=1
    try:
        for i in range(460,918):
           url='https://www.36mh.com/manhua/touxingjiuyuetian/121{0}.html'.format(i)
           html=get_html(url)
           parse_html(html,i)

    except:
        print('have gotten bottom!')
if __name__ == '__main__':
    main()