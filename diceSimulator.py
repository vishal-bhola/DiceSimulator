import random
print("This is a dice simulator")

x="y"
while x=="y":
    randnumber = random.randint(1,6)
    if randnumber==1:
        print("-----------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("-----------")
    elif randnumber==2:
        print("------------")
        print("| O        |")
        print("|          |")
        print("|        O |")
        print("------------")
    elif randnumber==3:
        print("------------")
        print("| O        |")
        print("|     O    |")
        print("|        O |")
        print("------------")  
    elif randnumber==4:
        print("-----------")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("-----------")
    elif randnumber==5:
        print("-----------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("-----------")
    elif randnumber==6:
        print("-----------")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("-----------")    
    x=input("Press y to roll again and n to exit\n")    

