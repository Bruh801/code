import random
while True:
    question=input("Ask the magic 8 ball a question: (press enter to quit) ")
    answer=random.randint(1,20)
    if question=="":
        print("Stopping the Game.")
        break
    if answer==1:
        print("It is certain.")
    elif answer==2:
        print("It is decidedly so.")
    elif answer==3:
        print("Without a doubt.")
    elif answer==4:
        print("Yes definitely.")
    elif answer==5:
        print("You may rely on it.")
    elif answer==6:
        print("As I see it, yes.")
    elif answer==7:
        print("Most likely.")
    elif answer==8:
        print("Outlook good.")
    elif answer==9:
        print("Yes.")
    elif answer==10:
        print("Signs point to yes.")
    elif answer==11:
        print("Reply hazy, try again.")
    elif answer==12:
        print("Ask again later.")
    elif answer==13:
        print("Better not tell you now.")
    elif answer==14:
        print("Cannot predict now.")
    elif answer==15:
        print("Concentrate and ask again.")
    elif answer==16:
        print("Don't count on it.")
    elif answer==17:
        print("My reply is no.")
    elif answer==18:
        print("My sources say no.")
    elif answer==19:
        print("Outlook not so good.")
    elif answer==20:
        print("Very doubtful.")
