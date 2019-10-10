from lxml import html
import requests
import cx_Oracle


#获取煎蛋网首页HTML文档
html_doc=requests.get('http://jandan.net').text
selector=html.fromstring(html_doc)
ul_list=selector.xpath("//div[@class='indexs']")

#爬取首页24篇文章的链接url，主标题title，副标题info
for li in ul_list:
	urls=li.xpath("h2/a/@href")
	url=''.join(urls)
	titles=li.xpath("h2/a/text()")
	title= ''.join(title)
	infos=li.xpath("text()")
	infomation=infos[-1].replace('\r\n\t', '')
	info=infomation.replace('\t','')

        #爬取对应文章下的评论comment,评论者commentator
        html_doc=requests.get(url).text
	s=html.fromstring(html_doc)
        cm_list=s.xpath("//ol[@class='commentlist']/li")
	for cm in cm_list:
		commentators=cm.xpath("//div[@class='author']/strong/text()")
		comments=cm.xpath("//div[@class='text']/p/text()")
		for commentator in commentators:
			print(commentator )

		for comment in comments:
			print(comment )
