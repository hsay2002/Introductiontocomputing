'''      Name   ==> Yash Vashishth
         SID    ==> 21107083
         Branch ==> Mechanical
                                    '''
                                    
# Ques 1:
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = input("Enter your string here : ")

print(" The reversed string is : ",reverse(s))


#Ques 2:
lower = int(input(" Enter the lower range limit: "))
upper = int(input(" Enter the upper range limit: "))
n = int(input(" Enter the number to be divided by: "))
for i in range( lower, upper+1):
    if i%n == 0:
        print(i)

#Ques 3:
import math
a=int(input("Enter the first side: "))
b=int(input("Enter the second side : "))
c=int(input("Enter the third side : "))
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle: ',area)

#Ques 4:
n = 5;
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')

#Ques 5:
rows = int(input("Enter Right Triangle Consecutive Alphabets Rows = "))
print("====The Right Triangle of Consecutive Alphabets Pattern====")
alphabet = 65
for i in range(rows):
    for j in range(i + 1):
        print('%c' %alphabet, end = ' ')
        alphabet = alphabet + 1
    print()

#Ques 6:
lower_value = int(input ("Please, Enter the Lowest Range Value: "))
upper_value = int(input ("Please, Enter the Upper Range Value: "))

print ("The Prime Numbers in the range are: ")
for number in range (lower_value, upper_value + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)

#Ques 7:
nl=[]
for x in range(1,500):
    if (x%7==0) and (x%11==0):
        nl.append(str(x))
print (','.join(nl))

#Ques 8:
lst = []
for i in range(0, 10):
    ele = int(input(" Enter the numbers: "))
    lst.append(ele)
pn = []
nn = []
on = []
en = []
for i in range(0, 10):
    if(i>=0):
        pn.append(i)
    if(i<0):
        nn.append(i)
    if(i%2==0):
        on.append(i)
    if(i%2!=0):
        en.append(i)
print(pn)
print(nn)
print(on)
print(en)
def word_count(lst):
    counts = dict()
    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count(lst))

#Ques 9:
def word_count(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
print( word_count('Python is a case sensitive language.'))
