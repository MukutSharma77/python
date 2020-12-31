'''Double Character Swap
Write a function to replace all instances of character c1 with character c2 and vice versa.
Examples
double_swap("aabbccc", "a", "b") ➞ "bbaaccc"
double_swap("random w#rds writt&n h&r&", "#", "&")
➞ "random w&rds writt#n h#r#"
double_swap("128 895 556 788 999", "8", "9")
➞ "129 985 556 799 888"'''

def double_swap(string , replace_to , replace_by):
    str_=''
    for i in string:
        if i == replace_to:
            str_+=replace_by

        elif i==replace_by:
            str_+=replace_to

        else:
            str_+=i

    print(str_)

double_swap("aabbccc", "a", "b")
double_swap("random w#rds writt&n h&r&", "#", "&")
double_swap("128 895 556 788 999", "8", "9")