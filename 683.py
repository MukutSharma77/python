'''CMS Selector Based on a Given String
Create a function that takes a list and a string as arguments and returns the list of CMSs that include the given string. Return the names in a list in alphabetical order.
Examples
cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]
cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]
cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]
Notes
The given letter(s) are case insensitive and can be more than one.
In the case of an empty string, return the entire list.
A CMS is a Content Management System.'''

lst=["WordPress", "Joomla", "Drupal"]
search='ru'
lst_2=[]
for i in lst:
    if search in i.lower():
        lst_2.append(i)

print(lst_2)