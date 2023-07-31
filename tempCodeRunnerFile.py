from tkinter import *
import random


window = Tk()
window.resizable(False,False)
canvas = Canvas(window)

WIDTH = 700

ui_frame = Frame(window, width=250, height=600, bg = 'red')
ui_frame.grid(row=0, column=0, padx=10, pady=10)

#width was 700
canvas = Canvas(window, width=610, height=600)
canvas.grid(row=0, column=1)

#contains 50 bars
bars = []

def draw_bars():
    for x in range(0, WIDTH, 14):
        bar = canvas.create_rectangle(x, 600, x+10, x, fill='black')
        bars.append(bar)

#make a main function put it in there
draw_bars()



def randomize_bar_positions():
    for i in bars:
        #x0, y1, x1, y0 = canvas.coords(bars[i-1])

        vals = random.sample(range(0, WIDTH, 10), 50)
        
        #canvas.coords(bars[i-1], vals[i-1], 600, vals[i-1] + 10, vals[i-1])



reset_button = Button(ui_frame, width=15,height=2, text='Reset').grid(row=0,column=0)

randomize_bar_positions()

#generate random num for 0-100 in steps of 10
x = random.randrange(0,100,10)
print(x)



window.mainloop()
