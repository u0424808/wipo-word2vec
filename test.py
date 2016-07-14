#coding=utf-8
import sys
import os
from gensim.models import word2vec
import csv

path=''
num=15
all_num=0
word_counter = {}
a=[]
b=[]
over=[]
no=['one','first','second','end','means','third', 'least', 'said','member']

traning_path=['alphatrain-A','alphatrain-B','alphatrain-C','alphatrain-D','alphatrain-E','alphatrain-F','alphatrain-G','alphatrain-H']
model_=['A_.model','B_.model','C_.model','D_.model','E_.model','F_.model','G_.model','H_.model']
n=0
t=0
type_n=0
def readtraingfile(words_a,num):
    
   
    s=0
    while s<len(model_) :
        model_p='C:\\Users\\zxc82\\wipotest\\model\\'+model_[s]
        s=s+1
        n=0
        while n<len(traning_path) :
            t=0
            all_num=0
            tr_p='S:\\wipo\\wipo-alphatrain\\'+traning_path[n]
            model = word2vec.Word2Vec.load(model_p) 
            for word in words_a:
                if word in word_counter:
                    if word in model.vocab:
                        if word not in no:
                            word_counter[word] += 1
                else:
                     word_counter[word] = 0
         
            popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
       
            print(popular_words[:num])
            a=popular_words[:num]
            for root, dirs, files in os.walk(tr_p):
                print("doing")
                print ("show folder: "+root) #輸出根目錄，debug
                for f in files:
                    filetest2=open(os.path.join(root, f),'r') 
                    str2=filetest2.read()  
                    words=str2.strip().split(' ')
                    word_counter2 = {}
                    for word in words:
                        if word in word_counter2:
                            #if word in model.vocab:
                            if word not in no:
                                 word_counter2[word] += 1
                        else:
                            word_counter2[word] =0
                 
                    popular_words2 = sorted(word_counter2, key = word_counter2.get, reverse = True)
                    #print(popular_words2[:num])
                    b=popular_words2[:num]
                        #print (b_)
                   
                    
                    try:
                        sim =model.n_similarity(a, b)
                        print('輸入的檔案目前和',traning_path[n],'的相似度為 ',sim)
                        t=t+1
                        all_num=all_num+sim
                    except:
                        sim=0
                        print('輸入的檔案目前和',traning_path[n],'的相似度無法比較 為 ',sim)
                        t=t+1
            p=all_num/t
            print(traning_path[n],p)
            over.append([traning_path[n],p,model_p])
                    
            #readtraingfile()
            n=n+1


    text_file = open("result\\result2.csv", "w")
    w = csv.writer(text_file)
    w.writerows(over)
    text_file.close()
    print('done')
    print(over)

def readfile(path):
    filetest=open(path,'r') 
    str1=filetest.read()
    words=str1.strip().split(' ')
    num = int(input(">>> 欲比較的頻率字數: "))
   
    return readtraingfile(words,num)

def rawInput():
    path = input(">>> 檔案: ")
    print ('檔案==> '+path)
    over.append(['測試的檔案==> ',path])
    return readfile(path)




if __name__ == '__main__':
    rawInput()