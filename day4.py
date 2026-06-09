"""
User can type "add", "show", or "quit". Add task adds to a list. Show prints all tasks numbered. Quit exits. 
Everything inside functions — one function per action.
"""
import sys
tasks=[]
def add():
    t1=input("enter task to do ")
    tasks.append(t1)
    
    
def show():
    for i in range(0,len(tasks)):
      print(f"{i+1}.  {tasks[i]}")
    
def quit():
    print("goodbye")
    sys.exit() 

while True:
    
     choice= input("enter")
     if(choice == 'add'):
      add()
     elif(choice == 'show'):
      show()
     elif(choice == 'quit'):
      quit()
      
     else:
      print("wrong choice ")
      


