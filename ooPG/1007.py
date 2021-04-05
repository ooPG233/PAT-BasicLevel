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

def main():
    lst = get_primeslist(int(input()))
    count = 0
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == 2:
            count += 1
    print(count)

if __name__ == '__main__' :
    main()