#coding=utf-8
import string  
import re
import os
import io #檔案io
from nltk.corpus import stopwords #去無用字
#traning_path=['alphatrain-A','alphatrain-B','alphatrain-C','alphatrain-D','alphatrain-E','alphatrain-F','alphatrain-G','alphatrain-H']
#l_list=['human necessities ','performing operation Transportation ','Metallurgy ','textile paper ','fix construcions ','mechanical ','physics ','electriciy ']

def dealOneFile(para):
    orgdoc=io.open(para, "r", encoding="UTF-8")
    modifiedDoc=" "
    try:
        modifiedDoc=orgdoc.read()

    except (Exception):
    	modifiedDoc=''
    print(modifiedDoc)

    stop = stopwords.words('english')
    str1=''
    modifiedDoc=re.sub(r"[^A-Za-z\s]+"," ",modifiedDoc)
    modifiedDoc=modifiedDoc.lower()
    for i in modifiedDoc.split():
    	if i not in stop:
    		str1=str1+i+' '
    orgdoc.close()

    wholeParagraph=str1
    mdfdoc=io.open(para, "w")
    mdfdoc.write(wholeParagraph.decode("UTF-8"))
    mdfdoc.close()
    print("perform text operation successfully! "+wholeParagraph)

#主程式
if __name__ == '__main__':
    #針對我所需要的工作資料夾走訪每個檔案
    # for root, dirs, files in os.walk(os.getcwd()+"\\test\\"):
    
    	path='S:\\wipo\\wipo-alphatrain\\'
    	for root, dirs, files in os.walk(path):
    		print ("show folder: "+root)
    		for f in files:
    			print ("show file" +os.path.join(root, f))
    			dealOneFile(os.path.join(root, f))
    	