#Input three angle than tell is it triangle or not

ang1=float(input("Enter angle1 :   "))
ang2=float(input("Enter angle2 :   "))
ang3=float(input("Enter angle3 :   "))

tot=ang1+ang2+ang3

if tot==180:
    print("Yes it is triangle")
else:
    print("No its not a triangle")