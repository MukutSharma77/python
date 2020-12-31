'''Cricket Balls to Overs!
In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls nBalls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.
Examples
total_overs(2400) ➞ 400
total_overs(164) ➞ 27.2
total_overs(945) ➞ 157.3
total_overs(5) ➞ 0.5'''

def total_overs(balls):
    over=balls//6
    ball=balls - over*6
    print(str(over)+'.'+str(ball))



total_overs(2400)
total_overs(164)
total_overs(945)
total_overs(5)