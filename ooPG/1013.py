def get_prime_index_upper_bound(n):#获取第n个素数的上界
    import math
    if n>=6:
        n=float(n)
        return int(n*math.log(n)+n*math.log(math.log(n))) #计算素数上界近似函数
    else:
        return 15

def get_primeslist(N):
    flag=[1 for i in range(N+1)] #为了让下标等于值，便于计算
    flag[0]=flag[1]=0
    primes_list=[]
    for i in range(2,N+1):
        if flag[i]: #值为1代表这个值是素数
            primes_list.append(i) #下标等于值
            j = i
            while j*i <= N : #从素数本身开始自底向上将素数的倍数标记为合数（非素数）
                flag[j*i] = 0 
                j += 1
    return primes_list

def get_primeslist_between(M,N):#获取第M个到第N个及其之间的素数
    pn=get_prime_index_upper_bound(N)
    primes_list=get_primeslist(pn)
    return primes_list[M-1:N]
    


def main():
    M,N=(int(i) for i in input().split())
    out_put_list=[str(i) for i in get_primeslist_between(M,N)]
    if len(out_put_list)/10>0:
        for i in range(len(out_put_list)//10): #输出满10个数字的行
            print(' '.join(out_put_list[i*10:(i+1)*10]))
        if len(out_put_list)%10:    #输出不满10个数字的行
            print(' '.join(out_put_list[-(len(out_put_list)%10):]))

if __name__ == '__main__':
    main()
