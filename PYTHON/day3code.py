##### 1)    **BUILD A BETTER CALCULATOR USING IF STATEMENTS**
a = int(input("enter a number:"))
b = int (input("enter another numer:"))
c = input("enter operator:")
if (c == "+"):
    print(a + b)
elif (c == "-") :
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("operator invalid")


##### 2)    **BUILD A GUESSING GAME**
animal_name = "lion"  #write lion under parenthesis
guess_animal = input( "enter animal name:" )  #dont use int for animal name
if guess_animal == animal_name:
    print("YOU GUESSED CORRECTLY,YOU WON")
else:
    print("HINT:KING OF FOREST")

    guess_animal = input("try one last time:")  # use to limit one time try and continue if loop again
    
    if guess_animal == animal_name:
        print("YOU GUESSED CORRECTLY,YOU WON")
    else:
        print("YOU LOST")


    