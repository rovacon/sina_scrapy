import urllib
import sys

with open(sys.argv[1],'r') as f:
	for line in f.readlines():
		line=line.strip()
		host,query=urllib.splitquery(line)
		key=host
		querylist=query.split('&')
		querylist.sort()
		for attr in querylist:
			key+="+"+urllib.splitvalue(attr)[0]
		print key
			
