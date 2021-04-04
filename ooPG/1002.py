from functools import reduce
def main():
    input_n=input()
    spell_dict={'0':"ling",'1':"yi",'2':"er",'3':"san",'4':"si",'5':"wu",'6':"liu",'7':"qi",'8':"ba",'9':"jiu"}
    
    sum_n = lambda n : str(reduce(lambda x,y:x+y,[int(i) for i in input_n])) #加和

    spell = lambda n : ' '.join([spell_dict[i] for i in sum_n(n)])
    
    print(spell(input_n))

if __name__ == '__main__':
    main()