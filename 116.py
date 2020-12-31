#Max of three number

#OInputting three number from user
num1=int(input("Enter NMumber1   :    "))
num2=int(input("Enter NMumber2   :    "))
num3=int(input("Enter NMumber3   :    "))

#Condion for which number is greater among three

if num3==num2 and num3==num1:
    print("All three Numnber are equal")
elif num1 > num2 and num1 > num3:
    print("Nubmer 1 is gtreatest")
elif num2 > num1 and num2 > num3:
    print("Nubmer 2 is gtreatest")

elif num3 > num2 and num3 > num1:
    print("Nubmer 3 is gtreatest")

elif num1 == num2 and num1 > num3:
    print("Number 1 and number 2 are eqaul and greatest")

elif num3 == num2 and num3 > num1:
    print("Number 3 and number 1 are eqaul and greatest")

else:
    pass