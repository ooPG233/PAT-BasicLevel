def get_derivation(A,n):
    if A == 0 or n == 0:
        return None
    else:
        return [A*n,n-1]

def main():
    input_list=[int(x) for x in input().split()]
    output_list=[]
    for i in range(0,len(input_list),2): #以步长为2遍历取出多项式的系数（跳过指数）
        derivation=get_derivation(input_list[i],input_list[i+1])
        if(derivation): #如果导数的值不为None，则格式化地加入输出序列
            output_list.append(' '.join([str(x) for x in derivation]))
    if output_list == []:
        print(0,0)
    else:
        print(' '.join(output_list))

if __name__ == '__main__':
    main()