#find the winner of the day from given two basketball teams.
# Input : Team1 Team2 Team1


print("Comma seprated")
round_=input("enter the teams :  ").split(",")

if round_.count('Team1') > round_.count('Team2'):
    print("Team1 Wins")

elif round_.count('Team2') > round_.count('Team1'):
    print("Team2 Wins")

else:
    print("Match Draws")