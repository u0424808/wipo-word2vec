import gensim
import re
# print result
model = gensim.models.Word2Vec.load("C:\\Users\\zxc82\\wipotest\\model\\text8.model")
rname_list=['britain','america','taiwan','china','france','japan','afghanistan']


a='queen king prince princess'
b='sushi restaurant'
c='baseketball baseball'
d='war oil'
# load fresh model

#for x in rname_list:
#	result =model.n_similarity(a,x)
#	print (x,result)
result = model.most_similar_in_list(a.split(' '), topn=5, restrict_vocab=rname_list)
result2 = model.most_similar_in_list(b.split(' '), topn=5, restrict_vocab=rname_list)
result3 = model.most_similar_in_list(c.split(' '), topn=5, restrict_vocab=rname_list)
result4 = model.most_similar_in_list(d.split(' '), topn=5, restrict_vocab=rname_list)

print('queen king prince princess 相似的國家是',result)

print('sushi restaurant 相似的國家是',result2)

print('baseketball baseball 相似的國家是',result3)

print('war oil 相似的國家是',result4)
