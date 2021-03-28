def main():
    input_len=int(input())
    heigher=input().split()
    lower=heigher.copy()
    for i in range(input_len-1):
        student=input().split()
        if int(student[2])>int(heigher[2]):
            heigher=student
        elif int(student[2])<int(lower[2]):
            lower=student
    print(' '.join(heigher[:2]))
    print(' '.join(lower[:2]))
if __name__ == '__main__':
    main()