#please open and run the program via the codeskulptor link provided

http://www.codeskulptor.org/#user43_wRcRsDjs4C3ZdaO_0.py


#Code of the program  for reference


import random
import simplegui

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions


def name_to_number(name):
    
    
    if name == "rock" : 
        return 0
    elif name == "Spock" : 
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" : 
        return 3
    elif name == "scissors" :
        return 4
    else : 
        return "Error : Invalid choice"
    
    
    
   

   


def number_to_name(number):
    
    
    if number == 0 : 
        return "rock"
    elif number == 1 : 
        return "Spock"
    elif number == 2 : 
        return "paper"
    elif number == 3 : 
        return "lizard"
    elif number == 4 : 
        return "scissors"
   
    
    
    

def rpsls(player_choice): 
    
    
       
    
    print " "
    
    
    print "Player chose" + " " + player_choice + "."
    
    player_number = name_to_number(player_choice)
     
    
    comp_number = random.randint(0,4)
    
    
    comp_number = random.randint(0 , 4)
    comp_choice = number_to_name(comp_number)
    
    
    print "Computer chose" + " " + comp_choice + "." 
    
    diff = (player_number - comp_number)
    result = diff % 5 
    
   
    
    if result == 1 : 
        print "Player wins!"
    elif result == 2 : 
        print "Player wins!"
    elif result == 3 : 
        print "Computer wins!"
    elif result == 4 : 
        print "Computer wins!"
    elif result == 0 : 
        print "The player and computer have tied!!"
 

#frame in order to make the game interactive

frame = simplegui.create_frame("Rock Paper Scissors Lizard Spock", 500, 500)
frame.add_label("The available player choices are : ",)
label1 = frame.add_label("rock")
label2 = frame.add_label("Spock")
label3 = frame.add_label("paper")
label4 = frame.add_label("lizard")
label5 = frame.add_label("scissors")
label6 = frame.add_label(" ")
frame.add_input("Input your choice and press enter", rpsls, 100)

def draw(canvas): 
    canvas.draw_text("Please enter the choices exactly as they've been listed.",[50,200], 15, "Red")

    
    
    
    
frame.set_draw_handler(draw)

frame.start()
