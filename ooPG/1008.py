def main():
    N,M=(int(x) for x in input().split())
    input_array=[x for x in input().split()]
    M=M%N #避免出现 M > N 的情况
    output_array=input_array[-M:]+input_array[:-M] #后M位移至头部
    print(' '.join(output_array))

if __name__ == '__main__' :
    main()