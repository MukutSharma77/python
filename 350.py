'''350)Create a function that takes in the number of each challenge level a user has played and calculates the user's total number of points. Keep in mind that a user cannot complete negative challenges, so the function should return the string "invalid" if any of the passed parameters are negative.
Examples
score_calculator(1, 2, 3) ➞ 85
score_calculator(1, 0, 10) ➞ 205
score_calculator(5, 2, -6) ➞ "invalid"

'''

def score_calculator(list1):
    print((list1[0]*5)+(list1[1]*10)+(list1[2]*20))

list1=[1,2,3]
score_calculator(list1)