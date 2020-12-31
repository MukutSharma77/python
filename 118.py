#Write a function that returns a lambda expression, which transforms its input by adding a particular suffix at the end.

#using lambda to Conactenate word and suffix
output=lambda word,suffix:word+suffix


#Inputting Word and suffix
word=input("Enter Word :   ")
suffix=input("Enter Suffix  :    ")
print("Word + Suffix :  ",output(word,suffix))
