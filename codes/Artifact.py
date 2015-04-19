# -*- coding: utf-8 -*-
# Parses the twitter data (json form) to extract the artifacts and lies and share of each artifacts

import json
import urllib2
import sys

p=sys.argv[1]

f=open('./output/TwArtifact_like.txt','w+')
f1=open('./output/TwArtifact.txt','w+')

def main():
    input_file = open(p)
    data = input_file.readlines()
    for idata in data:
    	d = json.loads(idata)
    	if 'retweeted_status' in d:
			d=d['retweeted_status']
	
        
        for j in range(0,len(d['entities']['urls'])):
			l=d['entities']['urls'][j]['expanded_url']
			try:
				a=urllib2.urlopen(l)
				sg=a.url
				if sg.endswith("/"):
					sg=sg[:-1]
				f.write(str(sg).encode('utf8')+" ")
				f1.write(str(sg)+'\n')
				f.write(str(d['favorite_count'])+" ")
				f.write(str(d['retweet_count'])+" ")
				f.write("\n")
				f.flush()
				f1.flush()
			except:
				continue
	

if __name__ == '__main__':
    main()
    f.close()
    f1.close()
