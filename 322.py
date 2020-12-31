'''Given a dictionary of people and their ages, return how old the people would be after n years have passed. Use the absolute value of n.
Examples
after_n_years({
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}, 1) ➞ {
  "Joel" : 33,
  "Fred" : 45,
  "Reginald" : 66,
  "Susan" : 34,
  "Julian" : 14
}'''

after_n_years={
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}

num=int(input("Add age of all :  "))

for i,j in  after_n_years.items():
    after_n_years[i]=j+1

print(after_n_years)