'''Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged
'''

stirng=' Aman in makret'

if 'Is' in stirng[:2]:
    print("String is unchenged")
    print("\n",stirng)

else:
    stirng_='Is '
    stirng_+=stirng
    print(stirng_)