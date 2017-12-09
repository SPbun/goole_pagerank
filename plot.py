import matplotlib.pyplot as plt
import numpy as np
import requests
import re

f = open('result__www.scutde.net.txt','r')

urls = []

while True:
	url = f.readline().rstrip('\n')

	if url:
		urls.append(url)
	else:
		break

relation_matrix = np.zeros((len(urls),len(urls)))
#generate a matrix to be plotted
for i in range(0,len(urls)):
	try:
		r = requests.get(urls[i],timeout=5)
	except :
		print 'timeout'
		continue
	# find out all urls in the specific website
	print("good,dealing the {}/500 url".format(i))
	content = r.content
	pattern_url = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')
	result1 = pattern_url.findall(content)
	#if each item in urls is included by the specific website  content urls
	for j in range(0,len(urls)):
		if urls[j] in result1:
			relation_matrix[i][j] = 1

#diagonal number should be 1
for i in range(0,len(urls)):
	relation_matrix[i][i] = 1
