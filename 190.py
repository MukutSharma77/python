#Python program to convert temperature from Celsius to Fahrenheit and vice-versa

#Aksking user to choose any on of then
print("1)Celsius to Fahrenheit\t\t2)Fahrenheit to Celsius ")
choose=int(input("\n Choose :   "))

if choose==1:
    print("Celsius to Faharenit")
    c = float(input("Enter Celsius  :   "))
    print("Celsius in Fahrenhit  is   :   ", ((c + 32) * (9 / 5)).__round__(2))

elif choose==2:
    f = float(input("Enter Fahrenhit :   "))
    print("Fahrenhit in Celsius  is   :   ", (((f - 32) * (5 / 9))).__round__(2))

else:
    print("Invalid")