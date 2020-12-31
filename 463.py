'''Get the File Extension
Write a function that maps files to their extension names.
Examples
get_extension(["code.html", "code.css"])
➞ ["html", "css"]
get_extension(["project1.jpg", "project1.pdf", "project1.mp3"])
➞ ["jpg", "pdf", "mp3"]
get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"])
➞ ["rb", "cpp", "py", "js"]'''

list_=["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"]
list2=[]
for i in list_:

    idx=i.index('.')
    list2.append(i[idx+1:])

print(list2)