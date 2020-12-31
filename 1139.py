'''Anonymous Name
You are in the process of creating a chat application and want to add an anonymous name feature. This anonymous name feature will create an alias that consists of two capitalized words beginning with the same letter as the users first name.
Create a function that determines if the list of users is mapped to a list of anonymous names correctly.
Examples
is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]) ➞ True
is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"]) ➞ True
is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]) ➞ False
# Both words in "Brandishing Mimosa" should begin with a "B" - "Brandishing Beaver" would do the trick.
Notes
Both words in the alias should be capitalized.'''


def is_correct_aliases(lst1 , lst2):
    count=0
    for i in range(len(lst1)):
        lst_check1=lst1[i].split(' ')
        lst_check2 = lst2[i].split(' ')
        if lst_check1[0][0]==lst_check2[0][0] and lst_check1[0][0]==lst_check2[1][0]:
            count+=1

    print(len(lst1)==count)

is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"])
is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"])
is_correct_aliases(["Beth T."], ["Brandishing Mimosa"])