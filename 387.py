'''Similar Bread
Given two lists, which represent two sandwiches, return whether both sandwiches use the same type of bread. The bread will always be found at the start and end of the list.
Examples
has_same_bread(
  ["white bread", "lettuce", "white bread"],
  ["white bread", "tomato", "white bread"]
) ➞ True
has_same_bread(
  ["brown bread", "chicken", "brown bread"],
  ["white bread", "chicken", "white bread"]
) ➞ False
has_same_bread(
  ["toast", "cheese", "toast"],
  ["brown bread", "cheese", "toast"]
) ➞ False
'''


list1=["white bread", "lettuce", "white bread"]
list2= ["white bread", "tomato", "white bread"]

if len(list1) ==3 and len(list2):
    if list1[0]==list1[-1] and list2[0]==list2[-1]:
        print(True)
    else:
        print(False)