#!/usr/bin/env python3

#ex5
number=sys.argv[1]
if(number.isdigit()):
        number=int(number)
        factorial=1
        while(number > 0):
                factorial=factorial*number
                number-=1
        print(factorial)
else:
        print(f'Must provide and integer')

#ex6

numbers = [101,2,15,22,95,33,2,27,72,15,52]

for num in numbers
        if num %2==0:
                print(num)


#ex7 

numbers = [101,2,15,22,95,33,2,27,72,15,52]
print(sorted(n))

soma=o
soma1=0
for num in numbers
        if num %2==0:
                print(num)
                soma = soma + num
        elif num %2 != 0:
        soma1 + soma1 + num

print(soma)
print(soma1)

#ex12

dna = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

list_of_tuples = [(len(dna),dna)} for dna in genes]
print(list_of_tuples)



