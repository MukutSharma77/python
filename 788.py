'''Free Throw Probability
What's the probability of someone making a certain amount of free throws in a row given their free throw success percentage? If Sally makes 50% of her free shot throws. Then Sally's probability of making 5 in a row would be 3%.
Examples
free_throws("75%", 5) ➞ "24%"
free_throws("25%", 3) ➞ "2%"
free_throws("90%", 30) ➞ "4%"
Notes
p/100) ** k * 100'''

def free_throws(p,k):
    print(round((int(p[:-1])/100) ** k * 100),end="")
    print('%')


free_throws("75%", 5)
free_throws("25%", 3)
free_throws("90%", 30)
