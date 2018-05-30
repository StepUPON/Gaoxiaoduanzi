import requests
from fake_useragent import UserAgent
from lxml import etree
import sqlite3

con = sqlite3.connect('imgs.db')
cursor = con.cursor()
cursor.execute("create table if not exists image(alt text,src text)")

agent = UserAgent()

header = {
    "User-Agent":agent.random

}
for i in range(1900,1,-1):
    print("正在下载第{}页".format(str(i)))
    resposne = requests.get("http://ogaoxiao.com/page/{}".format(str(i)),headers = header)
    root = etree.HTML(resposne.content)
    div_article = root.xpath('//div[@class="left"]/div[@class="article"]')

    for item in div_article:
       src  = item.xpath("p/a/img/@src")
       src = src[0] if src else "None"
       alt = item.xpath("p/a/img/@alt")
       alt = alt[0] if alt else '暂时没有文字'
       cursor.execute('insert into image(alt,src)values (?,?)',(src,alt))
       con.commit()
       print(src,alt)


cursor.close(
    )
con.close()
