# math game'
import random

x = random.randint(1, 10)
y = random.randint(1, 10)

while   True:
    print ("1.main")
    print ("2.quit")
    cois = int(input("="))
    if cois == 1:
        print("---Level---")
        print("1.easy")
        print("2.medium")
        print("3.hard")
        print("4.extreme")
        play = int(input("= "))
        if play == 1:
            print ("Level Easy")
            print (x,"+",y)
            ans = int(input("= "))
            if ans == x+y:
                print("the answer is",x+y)
                print("yes i know u can answer that")
            else:
                print("bruhh u so stupid?!")
        if play == 2:
            print("Level Medium")
            print(x,"*",y)
            ans = int(input("= "))
            if ans == x*y:
                print("the answer is",x*y)
                print("yes u got it")
            else:
                print("hum, are u sure? u cant answer it?!")
        if play == 3:
            print("Level Extreme")
            print (x,"/",y)
            ans = float(input("= ")) 
            if ans == x/y:
                print("the answer is",x/y)
                print("nice good job")
            else:
                print("lmao u r so bad at math")
        if play == 4:
            print("Level Hard")
            print (x,"^",y)
            ans = int(input("= "))
            if ans == x*y:
                print("the answer is",x*y)
                print("woah u r a genius")
            else:
                print("nope, try again bruh")
       