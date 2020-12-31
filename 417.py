'''Potential Friend?
Given two sets of two people's different interests, return whether both people have at least 2 things in common or have exact interests. Return True if there's a potential friend!
Examples
is_potential_friend(
  {"sports", "music", "chess"},
  {"coding", "music", "netflix", "chess"}
) ➞ True
is_potential_friend(
  {"cycling", "technology", "drawing"},
  {"dancing", "drawing"}
) ➞ False'''

friend1=  {"cycling", "technology", "drawing"}
friend2=  {"dancing", "drawing"}
friend_=friend1 & friend2
# print(friend_)
if len(friend_) >=2:
    print(True)
else:
    print(False)