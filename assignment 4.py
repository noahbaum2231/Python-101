#13
#a 1,2,3,4
#b 5,6,7,8,9
#c 5,8,11,14,17
#f (empty)
#g (empty)

#15
#a range(6)
#b range (5,0,-1)
#c range(5,31,5)
#d range (30,4,-5)
#e range(-3,4)
#f range (3,-4,-1)
#g range (-50,-9,10)
#h range(0)

#19 99
#23 199
#24 19

# Write a program that asks the user for number input, and if it matches a number in a range you choose, print out
# "You guessed correctly!" -> Please try to do this one alone -> Make sure you test it for every case you can think of
range (7)
x = int(input("Please enter a number"))
if x>=0 and x<=7:
    print("You guessed it correctly!")
else:
    print("Wrong")