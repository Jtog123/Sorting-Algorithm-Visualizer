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
        random_y = random.randint(1,590)
        bar = canvas.create_rectangle(x, 600, x+10, random_y, fill='black')
        bars.append(bar)

#make a main function put it in there
draw_bars()



'''
to randoize bars
loop through every bar
canvas.itemconfig(bars[i])

set new random coords
has to be 
canvas.coords(bar[i],rand,600,rand,rand)

#set new coords
def width(e):
    x0, y0, x1, y1 = canvas.coords(rectangle) # get the coords of rect
    y1 = 3 * float(e)                         # calc new coords
    canvas.coords(rectangle, x0, y0, x1, y1)  # set new coords

'''

#bars[i-1] is first bar in array, they return ints
#get the position of every bar
#take that bar then randomize the position


def reset():
    #Clear screen
    canvas.delete('all')

    #Redraw bars
    for x in range(0, WIDTH, 14):
        random_y = random.randint(1,590)
        bar = canvas.create_rectangle(x, 600, x+10, random_y, fill='black')
        bars.append(bar)




#Draw bars -- check
#be able to aceess singular bars -- check
#randomize the positions of each bar

#*************************************************************

#allows me to acess and configure any rectangle in the array
canvas.itemconfig(bars[10], fill='green')

#allows me to get the coords of each rectangle in the array
#I THINK in the order x0,y0,x1,y1
#So if I want height of rect
# y1 - y0
#not sure how this is unpacking?
#might not matter 

#unpacked like x0, y1, x1,y0
x0,y1,x1,y0 = canvas.coords(bars[10])
#print(x0,y0,x1,y1)
#print(abs(y1-y0))

#unpacked like x0, y1, x1,y0
x0,y1,x1,y0 = canvas.coords(bars[11])
#print(x0,y0,x1,y1)
#print(abs(y1-y0))

'''
FRAMES for buttons
top_frame = Frame(ui_frame, width=200,height=200, bg='blue').grid(row=0,column=0)
mid_frame = Frame(ui_frame, width=200,height=200, bg='yellow').grid(row=1,column=0)
low_frame = Frame(ui_frame, width=200,height=200, bg='red').grid(row=2,column=0)
'''

reset_button = Button(ui_frame, width=15,height=2, text='Reset', command=reset).grid(row=0,column=0)



#generate random num for 0-100 in steps of 10
x = random.randrange(0,100,10)
print(x)



window.mainloop()
