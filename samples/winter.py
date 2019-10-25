name = 'Winter '
season = 'Winter '
status = 'is coming. '

print(name + status)

title = 'some words'
print(title)

#these are examples of constructing "sentences" by implementing variables with string
#using a "," adds a space, using "+" adds the variable without a space
print('we are going to play with',title)
print('we are going to bundle up when it is',name)
print('we think the best time of year',status)
print('you will meet',name + 'because',season + status)

#thoughts: we need some ways to alter punctuation in these statements. Maybe there is a way to automate this.


user = input('What is yr name? ')
print('Hello,',user + ". Let's write some poetry.")

print("Lookout world!",user,status)



while True:
    answer = input("Are you a girl or a boy? ")
    if answer == "neither":
        print("Cool. Yah, me neither.")
        loop = False
        break
    else:
        print("Nope! The correct answer is neither, There are no walls in space.")


while True:
    answer2 = input("Do you enjoy creating with words? ")
    if answer2 == "yes":
        print("OK. Let's get started then. ")
        loop = False
        break
    else:
        print("Do you even language? ")

##at this point I want to learn how to accept any alphbet based answer as an acceptable break to the loop.
##another work around is to reject numbers/integers as appropriate answers.
while True:
    answer3 = input("Tell me about your favorite color. Do you have a favorite color? Pick one. ")
    if answer3.isalpha():
        print(answer3,"is a great color! I have an aunt that is",answer3,".")
        loop = False
        break
    else:
        print("That's not a color")
