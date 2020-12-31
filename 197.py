'''Given a range of years as a string, return the number of leap years there are within the range'''

#inputing year
#Displaying all leap year start from year input and end with leap year
yearto=int(input("Start Year  to :   "))
yearfrm=int(input("Start Year  from :   "))

count=0
#loop to check leap year to and from
for i in range(yearto,yearfrm+1):
    if i % 4 == 0 or i % 400 == 0:
        print(i,end="  ")
        count+=1

if count==0:
    print("No leap year")