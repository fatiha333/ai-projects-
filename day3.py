"""

Problem 1: Longest Consecutive Increasing Streak

Ask the user for n numbers one by one.
Find:

The length of the longest increasing consecutive streak.
The starting and ending values of that streak.

Example:
Enter n: 10

5
7
8
3
4
5
6
2
9
10

Streaks:

5 → 7 → 8      length = 3
3 → 4 → 5 → 6  length = 4
2 → 9 → 10     length = 3

Output:
Longest streak length: 4
Starts at: 3
Ends at: 6


logic used :
ask nos
loop lgayenge enter no 
then us loop m no daalte daalte  chk krenge ke i+1 hai agr hai toh i store krenge then jb tk krte rhenge jb tk i+1 chlta rhega jaise hi nhi toh stop and store end 
nhi h toh enter krwate rhenge or do teen extra variables to maintain use honge 

5-6-7-8-2-4
contINERS PDHNE HAI ABHI ARRAY LIST DICT HASHMAP 


import array as ar

n = int(input("Enter how many numbers: "))

no = ar.array('i')

for i in range(n):
    value = int(input("Enter number: "))
    no.append(value)

max_length = 1
current_length = 1

start_value = no[0]
end_value = no[0]

temp_start = no[0]

for i in range(1, n):

    if no[i] == no[i - 1] + 1:
        current_length += 1

        if current_length > max_length:
            max_length = current_length
            start_value = temp_start
            end_value = no[i]

    else:
        current_length = 1
        temp_start = no[i]

print("Longest streak length =", max_length)
print("Starts at =", start_value)
print("Ends at =", end_value)
"""

"""
Ask user for a number. Print its multiplication table from 1 to 10 using a for loop.


num=int(input("enter a number"))
for i in range(1,11):
    print(i*num)

"""
"""
Build: Guessing game
Program picks a number between 1–10 (use import random then random.randint(1,10)).
User keeps guessing in a while loop until correct. Print "Too high", "Too low", or "Correct!" each round."""
import random
no=random.randint(0,10)
print(no)
i=int(input("enter a no "))
while(i!=no):
    
    if(i>no):
        print("too high")
        i=int(input("enter a no ")) 
    elif(i<no):
        print("too low")
        i=int(input("enter a no "))
    
print("yes no matched the guessed no is ",i)