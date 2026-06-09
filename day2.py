"""Problem 1: Income Tax Calculator (Progressive Tax System)

Create a program that asks for a person's annual income and calculates tax according to these rules:
Income Range	Tax Rate
0 - 50,000	0%
50,001 - 100,000	10%
100,001 - 200,000	20%
200,001 - 500,000	30%
Above 500,000	40%

Additional rules:

If age > 60 → reduce tax by 10%.
If age > 75 → reduce tax by 20%.
If income > 1,000,000 → add luxury surcharge of 5%.
Final tax can never be negative.
"""
income=int(input("Enter the annual income"))
age=int(input("enter the age "))
tax=0
if(income<=5000):
    tax=0
elif(income>5000 and income<=100000):
    tax=10/100*income
    if(age>60 and age<75):
        tax=tax-10/100*tax
    elif(age>75):
        tax=tax-20/100*tax
elif(income>100000 and income<=200000):
    tax=20/100*income
    if(age>60 and age<75):
        tax=tax-10/100*tax
    elif(age>75):
        tax=tax-20/100*tax        
elif(income>200000 and income<=500000):
    tax=30/100*income
    if(age>60 and age<75):
        tax=tax-10/100*tax
    elif(age>75):
        tax=tax-20/100*tax        
elif(income>500000 and income<=1000000):
    tax=40/100*income
    if(age>60 and age<75):
        tax=tax-10/100*tax
    elif(age>75):
        tax=tax-20/100*tax
else:
    tax=tax+5/100*income
    if(age>60 and age<75):
        tax=tax-10/100*tax
    elif(age>75):
        tax=tax-20/100*tax



if(tax<0):
    print("the final tax is 0")
else:
    print("the final tax is ",tax)





"""
Ask user for their age. If under 18 print "You are a minor". If 18–60 print "You are an adult". If above 60 print "You are a senior".
 Run it 3 times with different inputs.
"""
age1=int(input(" enter your age1 \n"))
if(age<18):
    print("u r minor ")
elif(age>=18 and age<=60):
    print("u r adult")
else:
    print("u r senior")



"""
Ask user for two numbers and an operator (+, -, *, /). Print the result. 
Handle division by zero — if someone types 0 as second number, print "Cannot divide by zero" instead of crashing.
"""
num1=int(input("enter number 1\n"))
num2=int(input("enter number 2\n"))
op=input("enter th operator from + - * / \n")
if(op=='+'):
    print("the result is ",num1+num2)
elif(op=='-'):
    print("the result is ",num1-num2)
elif(op=='*'):
    print("the result is ",num1*num2)
elif(op=='/'):
    if(num2==0):
        print("cant divide by zero")
    else:
        print("the result is ",num1/num2)
