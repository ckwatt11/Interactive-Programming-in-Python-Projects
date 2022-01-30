please run the game via the codeskulptor link provided : 
http://www.codeskulptor.org/#user43_hxj9b73Ea7MgX22_0.py


#Code of the program for reference


# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import simplegui
import random

guesses_left = 0
secret_number = random.randrange(0, 100)
#the default range is from 0 to 100 (excluding 100)
norange = 100


def new_game():
    
    global secret_number
    global guesses_left
    global norange
    secret_number = random.randrange(0, norange) 
    
    if norange == 100 : 
        guesses_left = 7
    elif norange == 1000 : 
        guesses_left = 10
        
    print "New game started.The Range is" + " " + str((0, norange)) + "."
    
    
   
    



def range100():
    
    global norange
        
    norange = 100
    new_game()
    

    
def range1000():
    
    global norange 
    norange = 1000
    new_game()
    
    
def input_guess(guess):
    
    global secret_number
    global guesses_left
    
    
#definition of  a variable called 'victory' that is false by default but becomes true if the player wins the game
    
    
    victory = False
    
    
    number = int(guess)
    print "Your guess is: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses : ", guesses_left
    
    if number > secret_number : 
        result = "Lower!"
    elif number < secret_number : 
        result = "Higher!"
    elif number == secret_number : 
        victory = True
    
    if victory : 
        print "Congratulations,you've beaten the game!"
        new_game()
        return          
    elif guesses_left == 0 : 
        print "Game over.You ran out of guesses."
        new_game()
    else :
        print result
        
image = simplegui.load_image("https://3.bp.blogspot.com/-bPC_u74JX0A/VufqNkvkaPI/AAAAAAAACNo/HP-c45UyP9ctxDotlM0gvGTca-ZZq86oQ/s1600/sinister-smiley-for-facebook.png")        
        
    
def draw(canvas): 
    canvas.draw_text("Can you beat the game?", [70,160], 24, "Red")
    canvas.draw_image(image, [200 , 250], (400, 350), [210, 230], (100 ,100))
    

frame = simplegui.create_frame("Guess the number", 400 , 400)


frame.add_input("Enter your number", input_guess , 100)
frame.add_button("Range is [0,100)" , range100 , 200)
frame.add_button("Range is [0,1000)" , range1000 , 200)
frame.set_draw_handler(draw)
 
new_game()



frame.start()