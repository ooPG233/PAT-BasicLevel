def main():
    def conditon_1(input_text):
        # 判断是否只含有'P','A','T'三个字符
        if set(input_text)=={'P','A','T'}:
            return True
        else:
            return False
    
    def condition_2and3(input_text):
        # 条件2是P、T之间只有一个A时，两边的元素个数（即两边A的个数）相等
        # 条件3是在条件1，2得到正确的基础上（题中'如果 aPbTc 是正确的'）进行的递推条件，即是在xPATx的基础上
        # 中间每多一个A，则在最后加多一个x，即xPAATxx、xPAAATxxx,所以可知该条件为（P左边元素的数量*PT中间元素的数量）==T右边元素的数量
        index_P=input_text.find('P')#正好也是P左边元素的数量
        index_T=input_text.find('T')
        countA_betweenPandT=index_T-index_P-1#中间元素的数量
        # print(index_P,index_T,countA_betweenPandT,len(input_text))
        if index_P*(countA_betweenPandT)==len(input_text)-index_T-1 : 
            return True
        else :
            return False
    
    def judge(input_text):
        if conditon_1(input_text) and condition_2and3(input_text):
            print('YES')
        else:
            print('NO')
    
    times=int(input())
    for i in range(times):
        judge(input())

if __name__ == '__main__':
    main()