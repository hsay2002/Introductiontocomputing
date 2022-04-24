# Name= Yash Vashishth     Branch= Mechanical     SID= 21107083
# Question 1 solution
num_1=int(input("enter first no. : "))
num_2=int(input("enter second no. :"))
num_3=int(input("enter third no. :"))
#average = (sum of all numbers)/(Total numbers)
Average=(num_1+num_2+num_3)/3
print("Average of the given numbers: ",Average)

# Question 2 solution:
Gross_income = float(input("Enter your gross income(in $) :"))
Dependents_in_family = int(input("Enter the number of dependents in your family : "))
Standard_deduction = 1000    #to be charged on all tax payers
tax_rate = 0.2     #20% tax rate chardged on all tax payers
Deduction_per_dependent = 3000      # (in $)
Taxable_income = Gross_income - Standard_deduction - (Deduction_per_dependent*Dependents_in_family)
Tax = Taxable_income*tax_rate
print("Taxable income: ",Taxable_income)
print("Tax",Tax)

# Question 3 solution:
user_sec=int(input("Enter number of seconds: "))
#for minutes
minutes = user_sec//60
#for seconds
seconds = user_sec%60
print("Given seconds converts to :",minutes,"minutes",seconds,"seconds")

# Question 4 solution:
num1 = 25                  #integer
num2 = int("25")           #string converted to integer
num3 = int(25.0)          #float value coverted to integer
Addition = num1 + num2 + num3
str(Addition)
print("Addition :",Addition)

# Question 5 solution:
import math                                 # Command to import math module in order to use mathematical terms and values
for i in range(0,360,15):                   # for loop is used first shows starting value
                                                             # second shows ending value
                                                             # third shows steps or gaps to be taken
    cosine=math.cos(math.radians(i))       # i is a variable runing in for loop
    sine=math.sin(math.radians(i))         # Gives answer in radians
    print( "cosine(",i,") is",round(cosine,4),"sine(",i,") is",round(sine,4))
