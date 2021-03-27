n=input()
l=len(n)
t=0
for i in range(l):
    t+=int(n[i])
t=str(t)
dic={'0':"ling",'1':"yi",'2':"er",'3':"san",'4':"si",'5':"wu",'6':"liu",'7':"qi",'8':"ba",'9':"jiu"}
for i in t:
    if i in dic:
        if i != t[len(t)-1]:
            print(dic[i],end=' ')
        else:
            print(dic[i])
