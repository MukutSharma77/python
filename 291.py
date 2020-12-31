'''Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
Examples
mood_today("happy") ➞ "Today, I am feeling happy"
mood_today("sad") ➞ "Today, I am feeling sad"
mood_today() ➞ "Today, I am feeling neutral"
'''

def function(mood):
    if mood:
        if mood=='happy':
            print("Today , I an feeling happy")
        elif mood=='sad':
            print("Today , I an feeling sad")

        else:
            pass

    else:
        print("Today , I an feeling neutral")

mood=input("Enter Your Mood :   ").lower()
function(mood)