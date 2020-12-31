'''Assign Person to Occupation
You have two lists. One shows the names of the people, while the other shows their occupation. Your task is to make a dictionary displaying each person to their respective occupations.
Person	Job
Annie	Teacher
Steven	Engineer
Lisa	Doctor
Osman	Cashier'''

list_name=['Annie','Steven','Lisa','Osman']
list_job=["Teacher" , 'Engineer','Doctor',"Cashier"]

dict_=dict(zip(list_name,list_job))
print(dict_)