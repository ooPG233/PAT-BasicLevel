def main():
    for i in range(1,int(input())+1):
        input_list=[int(x) for x in input().split()]
        print('Case #'+str(i)+': '+str(input_list[0]+input_list[1]>input_list[2]).lower()) #布尔值转为小写输出

if __name__ == '__main__':
    main()        