def A1(input_list):
    if not(input_list):
        return 'N'
    else:
        return str(sum(input_list))
    
def A2(input_list):
    if not(input_list):
        return 'N'
    else:
        return str(sum([input_list[x]*(-1)**(x) for x in range(len(input_list))]))

def A3(input_list):
    if not(input_list):
        return 'N'
    else:
        return str(len(input_list))

def A4(input_list):
    if not(input_list):
        return 'N'
    else:
        return '%.1f'%(sum(input_list)/len(input_list))    
    
def A5(input_list):
    if not(input_list):
        return 'N'
    else:
        return str(max(input_list))

def main():
    input_list=[int(x) for x in input().split()[1:]] #去除掉首个代表长度的输入
    output_list=[[] for i in range(5)] #生成包含5个空列表的列表
    for i in  input_list:
        remainder=i%5 #对5求余
        if remainder:   #如果余数不为零则直接添加进对应的列表
            output_list[remainder].append(i)
        else: #如果余数为零则判断是否是偶数，是则加入对应列表
            if not(i%2):
                output_list[remainder].append(i)
    for i in range(5):
        output_list[i]=eval('A{}({})'.format(str(i+1),str(output_list[i]))) #对分好类的列表格式化调用执行对应的函数并接收返回值

    print(' '.join(output_list))

if __name__ == '__main__':
    main()