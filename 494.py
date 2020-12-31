'''Fix the Broken Code
A student learning Python was trying to make a function that sorts all the letters of a string, but their code is broken, and they can't figure out why.
Spot and fix the error(s) in the code to make the function work. As an added challenge for those who are more advanced, see if you can shrink (the fixed version of) the student's code down to only a single line.
Examples
sort_word("dcba") ➞ "abcd"
sort_word("Unpredictable") ➞ "Uabcdeeilnprt"
# Capital letters should come first.
sort_word("pneumonoultramicroscopicsilicovolcanoconiosis") ➞ "aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv"'''

string_='Unpredictable'
print(''.join(sorted(string_)))