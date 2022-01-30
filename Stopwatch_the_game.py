

the goal of the game is to successfully stop the timer at multiples of 5. the score is of the format successful stop points/total stop points. to win the game,your successful stop points should be greater than or equal to your total stop points. Scoring pattern : for every successful stop at a multiple of 5, your successful stop points will be incremented by one whereas your total stop points will not change.For all other cases,the opposite will be true.

#please run the program via the codeskulptor link provided. http://www.codeskulptor.org/#user43_uESk965pFmAu54o.py

Code for reference :
template for "Stopwatch: The Game"

import simplegui import math import random
define global variables

count = 0 stop = True t_stops = 0 success_stops = 0 interval = 100
define helper function format that converts time
in tenths of seconds into formatted string A:BC.D

def format(t): mintenth = (t // 100) % 6 mins = (t // 600) % 600 secs = (t // 10) % 10 sectenth = t % 10 msg = str(mins) + ":" + str(mintenth) + str(secs) + "." + str(sectenth) return msg
define event handlers for buttons; "Start", "Stop", "Reset"

def start(): global count, stop stop = False timer.start()

def stop(): global t_stops, success_stops, stop if stop == False : if count % 10 == 0 and count != 0 : success_stops += 1 t_stops += 1 elif count != 0 : t_stops += 1 stopped = True timer.stop()

def reset(): global count, succes_stops, total_stops count = 0 stop = True t_stops = 0 success_stops = 0 timer.stop()

def tick() : global count count += 1

timer = simplegui.create_timer(100, tick)

def draw(canvas) : msg2 = format(count) canvas.draw_text(msg2,[105, 160], 40, "White") canvas.draw_text(str(success_stops) + "/" + str(t_stops),[250, 20],21, "Red")

#create a frame frame = simplegui.create_frame("Stopwatch : The Game", 300, 300) frame.set_canvas_background("Black") frame.add_button("Start", start, 100) frame.add_button("Stop", stop ,100) frame.add_button("Reset", reset, 100)
register event handlers

frame.set_draw_handler(draw) timer = simplegui.create_timer(interval, tick)
start frame

frame.start()
