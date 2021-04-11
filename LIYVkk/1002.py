n=input()
t=0
for i in n:
    t+=int(i)
str_word=str(t)
dic={'0':"ling",'1':"yi",'2':"er",'3':"san",'4':"si",'5':"wu",'6':"liu",'7':"qi",'8':"ba",'9':"jiu"}
list_word=[]
for i in str_word:
    if i in dic:
        list_word.append(dic[i])
print(" ".join(list_word))