def format_out(input):
    while len(input)<3:
        input='0'+input
    lst=[int(x) for x in input]
    return 'B'*lst[0]+'S'*lst[1]+'123456789'[:lst[2]]
            
        
def main():
    print(format_out(input()))

if __name__ =='__main__':
    main()