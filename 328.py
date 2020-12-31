'''You just returned home to find your mansion has been robbed! Given a dictionary of the stolen items, return the total amount of the burglary (number). If nothing was robbed, return the string "Lucky you!".
Examples
calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}) ➞ 100'''


calculate_losses={
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}

tot=0
for i in calculate_losses.values():
    tot+=i

print(tot)