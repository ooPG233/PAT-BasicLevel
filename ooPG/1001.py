n=int(input())

def function(n):
    times=0
    while n>1 :
        if n%2 ==0 :
            n/=2
        else:
            n=(n*3+1)/2
        times+=1
    return  times

print(function(n))