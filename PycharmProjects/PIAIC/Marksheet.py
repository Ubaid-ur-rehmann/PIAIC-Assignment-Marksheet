Name=input("Enter Your name")
Age=input("Age?")
print("Enter Your Given Numbers")
Eng=int(input("Enter Numbers of English"))
Maths=int(input("Enter Numbers of Maths"))
sindhi=int(input("Enter Numbers of Sindhi"))
PST=int(input("Enter Numbers of PST"))
Chem=int(input("Enter Numbers of Chemistry"))
Total=Eng+Maths+sindhi+PST+Chem
print("Marks Obtained : ",Total,' Out Of 500')
Per=float((Total/500)*100)
print("You got",Per,' Percent')
if(Per >=80 and Per < 100):
    print("Grade : A")
elif(Per >=70 and Per <80):
    print("Grade : B")
elif(Per >=60 and Per<70):
    print("Grade : C")
elif(Per>=50 and Per<60):
    print("Grade : D")
else:
    print ("Fail")
