#coding=utf-8
import os

str1=''
s=''

path='S:\\wipo\\wipo-alphatrain\\'
output='C:\\Users\\zxc82\\wipotest\\test\\'
for root, dirs, files in os.walk(path):
	print ("show folder: "+root) #輸出根目錄，debug
	for f in files:
		str1=open(os.path.join(root, f),'r').read() 
		s=s+str1+'\n'
s_=s.encode('utf-8')
n=output+'output.txt'
text_file = open(n, "w")
text_file.write(s)
text_file.close()