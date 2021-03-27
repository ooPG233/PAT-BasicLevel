from functools import reduce
def main():
    input_n=input()
    spell_list=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
    
    sum_n = lambda n : str(reduce(lambda x,y:x+y,[int(i) for i in input_n]))

    spell = lambda n : ' '.join([spell_list[int(i)] for i in sum_n(n)])
    
    print(spell(input_n))

if __name__ == '__main__':
    main()