'''Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.
Examples
correct_spacing("The film   starts       at      midnight. ")
➞ "The film starts at midnight."'''



string="The film   starts       at      midnight. "
print(' '.join(string.split()))