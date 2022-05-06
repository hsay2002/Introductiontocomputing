# Name = Yash Vashishth     Branch = Mechanical      SID = 21107083
# Ques 1
'''For taking length of string
First take input of string'''
string = "Python is a case sensitive language"

#len() is used for taking length of given string.
print("A) Length of the given string: ",len(string),"\n")

# This is for giving output string in reverse order.
print("B) Reverse of the given string is :")
print(string[::-1],"\n")

#slicing the string.
new_string = string[10:26]
print("C) New sliced string is: ","\n", new_string,"\n")

#replace a string using replace function in string slicing,
Replaced_string= string.replace('a case sensitive' , 'object oriented')
print("D) String after replacing: ", "\n" ,Replaced_string ,"\n")

#Finding the index of "a" in the input string.
print("E) Index of substring 'a' is:", string.find("a"),"\n")

#Printing the string without white spaces using replace in string.
print("F) Sting without white spaces: ","\n",string.replace(" ", ""))

# Ques 2
Name = str(input("Enter your name :\t"))
SID = int(input("Enter your SID :\t"))
CGPA = float(input("Enter your CGPA:\t"))
department_name = str(input("ENter your department name :\t"))

print("Hey,",Name, "Here!\nMy SID is", SID,"\nI am from", department_name, "department and my CGPA is", CGPA )

# Ques 3
# Use of Bitwise Operators.
a = 56
b = 10

# Use of Bitwise AND(&) operator.
print("A. a & b =", a & b)

# Use of Bitwise OR(|) operator.
print("B. a | b =", a | b)

# Use of Bitwise XOR(^) operator.
print("C. a ^ b =", a ^ b)

# Use of shift(left) operator.
print("D. a << 2 = ", a << 2)

# Use of shift(both) operator.
print("E. a >> 2 = ", a >> 2, " and ", "b >> 4 = ", b >> 4)

# Ques 4
# Taking input
string1 = str(input("Enter any string: "))

# Using string slicing to find a word in the string
checked = string1.find("name")

# Here '==' is comparison operator
if checked == -1:  # '-1' is the value as an output of find function indicating the absence of particular string in it.
    print("No")

else:
    print("Yes")

# Ques 5
# Taking inputs of the sides of the triangle.
n1 = int(input("Enter First length : "))
n2 = int(input("Enter Second length : "))
n3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
F1 = n1 > n2 + n3
F2 = n2 > n1 + n3
F3 = n3 > n1 + n2

# Here we check wheather the all conditions are satisfied or not.
Output = str(F1 or F2 or F3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))

#QUESTION 6

def function(a,b):
    ab_xor=a^b
    count=0
    while ab_xor:

        count=count+ (ab_xor & 1)
        ab_xor=ab_xor>>1
    print(count)


a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
function(a,b)