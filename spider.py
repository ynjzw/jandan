from lxml import html
import requests
import cx_Oracle

#连接数据库
db = cx_Oracle.connect('tom/lintao@localhost/orcl')
c = db.cursor()

#获取煎蛋网首页HTML文档
html_doc=requests.get('http://jandan.net').text
selector=html.fromstring(html_doc)
ul_list=selector.xpath("//div[@class='indexs']")

#爬取首页24篇文章的链接，主标题，副标题，并保存数据库
for li in ul_list:
	urls=li.xpath("h2/a/@href")
	str1=''.join(urls)
	title=li.xpath("h2/a/text()")
	str2 = ''.join(title)
	info=li.xpath("text()")
	str=info[-1].replace('\r\n\t', '')
	str3=str.replace('\t','')
	
	sql="insert into jandan (url,title,info) values ('%s','%s','%s')" % (str1,str2,str3)
	c.execute(sql)

r=c.execute("select * from jandan")
for i in r.fetchall():
	print(i)

db.close()

