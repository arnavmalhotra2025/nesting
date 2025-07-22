#Activiy 1
#exam attendence
medical_cause = input("did you have a medical cause Y or N: ")
atten = int(input("enter the attendence of the student:"))

if medical_cause == 'Y':
    print ("You are allowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")
    
#Activity 2
#electricity
units = int(input("Please enter number of unitsyou consumed: "))

if(units<50):
    amount = units * 2.60
    
elif(units <= 100):
    amount = 130 + 162.50 + ((units - 50)*3.25)
    surcharge = 35
    
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100)*5.26)
    surcharge = 45
    
else:
    amount = 130 + 162.50 + 526 + ((units - 200)*8.45)
    surcharge = 75
    
total = amount + surcharge
print("\nElectricity bill = %.2f" %total)

#Activity 3
#ride
print("select your ride:")
print("1. bike")
print("2. car")

choice = int(input("Enter your choise"))

if(choice == 1): 
    print("what type of bike")
    print("1. scooty\n")
    print("2. scooter\n")
    
    choice2 = int(input("enter your choice 2 :"))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")
        
elif(choice == 2): 
    print("what type of car")
    print("1. lamborgini\n")
    print("2. ferrari\n")
    
    choice3 = int(input("enter your choice 2 :"))
    if choice3 == 1:
        print("you have selected lamborgini")
    else:
        print("you have selected ferrari")
    

