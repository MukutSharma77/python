#HOUR is greater or minutes or seconds
#input three value comma seprated

#fuction to print longer duration
def time(hour,min,sec):
    hour=hour*3600
    min=min*60

    if hour > min and hour > sec:
        print("Hour Dutration is more")
    elif min > hour and min > sec:
        print("Minutes Dutration is more")
    else:
        print("Seconds Dutration is more")

#Input Hours minutes seconds
hour = int(input("Enter hours :   "))
min = int(input("Enter minutes :   "))
sec = int(input("Enter Seconds :    "))

time(hour,min,sec)