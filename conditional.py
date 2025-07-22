print("Check if you are eligible for vote.")

name = input("Enter name : ")
age = int(input("Enter age : "))

if(age>=18):
    print(name,"you can vote")
elif(age<18):
    print(name,"You can not vote")  