'''Get the File Name
Create a function that returns the selected filename from a path. Include the extension in your answer.
Examples
get_filename("C:/Projects/pil_tests/ascii/edabit.txt") ➞ "edabit.txt"
get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") ➞ "Beethoven_5.mp3"
get_filename("ffprobe.exe") ➞ "ffprobe.exe"'''

string="C:/Users/johnsmith/Music/Beethoven_5.mp3".split('/')
print(string[-1])