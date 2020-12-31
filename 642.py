'''Get Student Names
Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
Examples
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]
'''


stu={
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
lst=sorted(list(stu.values()))
print(lst)