'''Week day by input number and get week name from dictionary'''
week={
    '1' : 'Sunday',
    '2' : 'Monday',
    '3' : 'Tuesday',
    '4' : 'Wednesday',
    '5' : 'Thursday',
    '6' : 'Friday',
    '7' : 'Saturday'
}

week_num=input("Enter Number :   ")
print(week.get(week_num , 'Wrong Input!'))