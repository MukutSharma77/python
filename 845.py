'''C*ns*r*d Str*ngs
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.
Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"'''

def uncensor(string,vow):
    # string=string.split(' ')
    count=0
    str_=''
    for i in string:
        if '*' in i:
            str_+=vow[count]
            count+=1
        else:
            str_+=i

    print(str_)


uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
uncensor("abcd", "")
uncensor("*PP*RC*S*", "UEAE")