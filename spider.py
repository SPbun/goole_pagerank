import requests
import re

'''
init web pages query
'''
websites = []
tmp_websites = []

def find_all_url(content):
	'''
	find all urls in the content and return a list of them
	'''
	pattern_url = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')
	result1 = pattern_url.findall(content)
	#print result1
	for x in result1:
		tmp_websites.append(x)

def find_url(url):
	if url in websites:
		return
	try:
		r = requests.get(url,timeout=5)
	except:
		print 'timout'
		return
	else:
		print 'good'
		text = r.content
		#regex ,to find out all valid url,add to tmp_query
		tmp_url_list = find_all_url(text)
		#print text
		#tmp url added in websites query
		websites.append(url)
	

#text = 'http://baidu.com/1.html \n<>KLKJKJuhhulkj s,https://dsasdf.dsf.c.cdsaf.com/sdfasdf.htm'
#find_all_url(text)

#def append_url(

if __name__ =='__main__':
	init_url = 'http://www.sjtu.edu.cn/'
	tmp_websites.append(init_url)
	#websites.append(init_url)
	print tmp_websites[0]
	#tmp_url = tmp_websites[0]
	

	
	while len(websites)<500 and len(tmp_websites)>=1:
		print("spidering the {}/500 page ".format(len(websites)+1))
		#get the first url of websites query
		tmp_url = tmp_websites[0]
		#delete the first item
		del tmp_websites[0]
		find_url(tmp_url)
		#print websites
		

	print 'saving data***********'
	file = open('result_'+init_url.replace(init_url,'shjd')+'.txt','w+')
	for x in websites:
		file.write(x + '\n')
	file.close()
