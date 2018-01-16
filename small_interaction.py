'''
This is just a small experimentation with an app that interact with you 
and ask questions.
run the file from the terminal in order to use it.

'''



word = input("Hi, what's your name? (reply with just your name): ")
print("Hello " + word)
secword = input("can I ask you one question? (reply with either yes or no): ")
if secword == "yes":
    print("ok, let get started")
else:
    print("Why not? ")
    print("please just one question to test my algorithm!") 
tword = input("What's your favorit color? ")
fword = ("for your reply, " + tword + " is a sexy color,\nthanks for taking the test")


print("Thanks "+ word +" "+ fword)








