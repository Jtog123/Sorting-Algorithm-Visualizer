from tkinter import *
from tkinter import ttk
import random
import pdb

'''
TO DO

Create a main?
color for start bar
color for current bar
swap positions of bars
start button
drop down select of different algos
speed bar


'''


window = Tk()
window.resizable(True,False)
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
        #or x ,600, x+10 ,randon_y   or   x, random_y, x+10, 600, fill='black'
        #tags????
        bar = canvas.create_rectangle(x, 600, x+10, random_y, fill='black')
        bars.append(bar)
        #print(bar)
        #print('length is :' + str(len(bars)))

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


def start_algo(bars, tick_time):

    #first bar in list
    canvas.itemconfig(bars[0], fill='red')

    #all the coords of the first bar in the list
    x0_lowest, y1_lowest, x1_lowest,y0_lowest = canvas.coords(bars[0])

    #Create a list from 0-49 use as indexes
    

    for index, _ in enumerate(bars):
        x0_current, y1_current ,x1_current ,y0_current = canvas.coords(bars[index])
        print(index)


    #for i in bars:
     #   x0_current, y1_current ,x1_current ,y0_current = canvas.coords(bars[new_list[i-1]])
     #   print(x0_current,y1_current,x1_current,y0_current)
        #if bars[i-1]
        


#tkinter is keeps adding to the index
#for exmaple bar should go to 50
#after I delete it it keeps bar count going starting from 50 51

def reset():
    #Clear screen

    #canvas.delete(ALL)
    canvas.delete('all')

 
    #for bar in bars:
    
   

    bars.clear()


    draw_bars()
    #Redraw bars
    #for x in range(0, WIDTH, 14):
     #   random_y = random.randint(1,590)
      #  bar = canvas.create_rectangle(x, 600, x+10, random_y, fill='black')
       # bars.append(bar)




#Draw bars -- check
#be able to aceess singular bars -- check
#randomize the positions of each bar

#*************************************************************

#allows me to acess and configure any rectangle in the array
#canvas.itemconfig(bars[10], fill='green')

#allows me to get the coords of each rectangle in the array
#I THINK in the order x0,y0,x1,y1
#So if I want height of rect
# y1 - y0
#not sure how this is unpacking?
#might not matter 

#unpacked like x0, y1, x1,y0
#x0,y1,x1,y0 = canvas.coords(bars[10])
#print(x0,y0,x1,y1)
#print(abs(y1-y0))

#unpacked like x0, y1, x1,y0
#x0,y1,x1,y0 = canvas.coords(bars[11])
#print(x0,y0,x1,y1)
#print(abs(y1-y0))



#top_frame = Frame(ui_frame, width=200,height=200, bg='blue').grid(row=0,column=0)
#mid_frame = Frame(ui_frame, width=200,height=200, bg='yellow').grid(row=1,column=0)
#low_frame = Frame(ui_frame, width=200,height=200, bg='red').grid(row=2,column=0)

'''
timeValues = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = StringVar()
ttk.Label(recordInfo, text='Time').grid(row=0, column=1)
ttk.Combobox(recordInfo,textvariable=variables['Time'], values=timeValues
            ).grid(row=1, column=1, sticky=(W + E))

'''


algo_values = ['Bubble Sort', 'MergeSort']
ttk.Combobox(ui_frame,values=algo_values).grid(row=0,column=0)

start_button = Button(ui_frame, width=15,height=2, text='Start', command= lambda a=bars, b=0:start_algo(a,b)).grid(row=1,column=0)
reset_button = Button(ui_frame, width=15,height=2, text='Reset', command=reset).grid(row=2,column=0)




#start_algo(bars, 0)

window.mainloop()
