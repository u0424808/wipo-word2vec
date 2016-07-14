#coding=utf-8
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
from xml.dom import minidom
import xml.dom
import xml
import os
import codecs
import re


strs=''
s=''

path = 'S:\\wipo\\wipo-alphatrain\\'
for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		file=os.path.join(dirPath, f)
		print ("show file" +os.path.join(dirPath, f))
		try:
			dom=parse(file)
			name=dom.getElementsByTagName('ab')[0]
			if name.firstChild:
				ab=(name.firstChild.data).replace('\n','')
				strs=ab
				text_file = open(file+".txt", "w")
				text_file.write(strs)
				text_file.close()

			else:
				strs=strs
		except:
			print('error::'+file)



