# Take in the Marks of 5 Subjects and Display the Grade

# fuction for total of marks and percentage and grade

def grade(sub1,sub2,sub3,sub4,sub5):
    tot=sub1+sub2+sub3+sub4+sub5
    print("\nTotal marks scorded   :   ",tot)
    percent=(tot * 100 ) /500
    print("Percent scored  :  ",percent)

    if percent >= 80:
        print("A++")
    elif percent >= 60:
        print("B++")
    elif percent >=40:
        print("PASS")
    else:
        print("FAIL")

#Inputting a Marks for 5 subject and calling a funtion\
sub1=float(input("Enter Maths Marks : "))
sub2=float(input("Enter Hindi Marks : "))
sub3=float(input("Enter English Marks : "))
sub4=float(input("Enter Science Marks : "))
sub5=float(input("Enter Computer Marks : "))
grade(sub1,sub2,sub3,sub4,sub5)