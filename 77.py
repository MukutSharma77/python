# You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.


#given string and creating an empty string to count uniqu value frequency
string='aabbbccde'
freq=" "

for i in string:
    if i not in freq:
        freq+=i
        print(f"{i}   :    {string.count(i)}")