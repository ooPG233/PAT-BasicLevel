def Callatz(n):
    if n%2 :
        return (n*3+1)/2
    else:
        return n/2
def main():
    input_len=int(input())
    input_list=[int(x) for x in input().split()]
    set1=set(input_list)
    set2=set()
    for i in input_list:
        while i>1 :
            i = Callatz(i)
            if i in set2:
                continue
            set2.add(i)
    key_list=[str(x) for x in sorted(list(set1-set2),reverse=True)]
    print(' '.join(key_list))

if __name__=='__main__':
    main()

