
"""
Problem 1 — FizzBuzz with a twist
Print numbers 1 to 100. But:

If divisible by 3 → print "Fizz"
If divisible by 5 → print "Buzz"
If divisible by both 3 and 5 → print "FizzBuzz"
Otherwise print the number



for i in range(1,101):
    if(i%3==0 and i%5!=0):
        print("Fizz")
    elif(i%5==0 and i%3!=0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
"""
"""
Ask user to type a sentence. Print how many times each word appears.
Example input: "the cat sat on the cat"
Output:
the: 2
cat: 2
sat: 1
on: 1

"""
"""""
sent=input("enter a sentence ")
dict={}

for i in sent.split():
     if(i in dict):
        dict[i]+=1
     else:
        dict[i]=1
print(dict)
"""
"""
Ask user for a word. Tell them if it's a palindrome or not. A palindrome reads the same forwards and backwards. "racecar" → yes. "hello" → no.
One rule: solve it without reversing the whole string using [::-1]. Use a loop and logic instead.
"""

sent=input("enter a sentence ")
length=len(sent)
new=[]
for v in range(length -1,-1,-1):
        
        new.append(sent[v])
print(new)  
new="".join(new)      
if(sent==new):
    print("yes palindrome")
else:
      print("no not palindrome")

