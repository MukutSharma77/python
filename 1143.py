'''In N Days...
If today was Monday, in two days, it would be Wednesday.
Create a function that takes in a list of days as input and the number of days to increment by. Return a list of days after n number of days has passed.
Examples
after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]
after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]
after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]'''


def after_n_days(week_lst , idx):
    week_day=['Sunday' , 'Monday' ,'Tuesday' , 'Wednesday' , 'Thursday' ,'Friday', 'Saturday' , 'Sunday']
    output=[]
    for i in week_lst:
        output.append(week_day[(week_day.index(i)+idx)%7])
    print(output)



after_n_days(["Thursday", "Monday"], 4)
after_n_days(["Sunday", "Sunday", "Sunday"], 1)
after_n_days(["Monday", "Tuesday", "Friday"], 1)