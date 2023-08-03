from tkinter import *
from tkinter import ttk
import random
import time

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

canvas = Canvas(window, width=700, height=600)
canvas.grid(row=0, column=1)

#contains 50 bars
bars = []

def draw_bars():
    
    for x in range(0, WIDTH, 14):
        random_y = random.randint(1,590)
        #or x ,600, x+10 ,random_y, fill='black'   or   x, random_y, x+10, 600, fill='black'
        #maybe no fill looks kind of cool
        bar = canvas.create_rectangle(x ,600, x+10 ,random_y, fill='black' )
        bars.append(bar)






'''


#set new coords
def width(e):
    x0, y0, x1, y1 = canvas.coords(rectangle) # get the coords of rect
    y1 = 3 * float(e)                         # calc new coords
    canvas.coords(rectangle, x0, y0, x1, y1)  # set new coords

'''

def swap_bars(bar_0, bar_1):
    #x0_low, y1_low ,x1_low ,y0_low
    x00, _ , x01, _ = canvas.coords(bar_0)
    x10, _ , x11, _ = canvas.coords(bar_1)

    canvas.move(bar_0, x10-x00,0)
    canvas.move(bar_1,x01-x11,0)

    #canvas.move(oval, 10, 0)   #  for x += 10
    #canvas.move(oval, 0, -10)  #  for y -= 10


    #canvas.move(bars[49], -50, 0)
    

'''
def sort_bars(bar_0, bar_1):
    #Unpack x and y
    x00, y00, _, _ = canvas.coords(bar_0)
    x10,y10, _, _ = canvas.coords(bar_1)

    #if heights are off
    if y10 < y00:
        canvas.move(bar_0,-abs(x00-x10), 0)
        canvas.move(bar_1, abs(x00-x10), 0)
        return True
    else:
        return False
'''


def start_algo(bars, tick_time):

    #first bar in list
    canvas.itemconfig(bars[0], fill='red')

    canvas.itemconfig(bars[49], fill='blue')


    #all the coords of the first bar in the list
    #x0_lowest, y1_lowest, x1_lowest,y0_lowest = canvas.coords(bars[0])


    
    #The GREATER the y1_current the smaller the bar
    #so 

    #NOWWWWW figure out how to swap positions, just swap x's and use canvas.move while decrementing value, refer to github
    #if y1_current > y1_lowest
    #swap
    #temp  = y1_lowest
    #y1_lowest = y1_current
    #y1_curr = temp
    #canvas.move

    
    #first bar = bars[i]
    #get its coords
    #next bar after = bars[j]
    '''
    for i, _ in enumerate(bars):
        x0_low, y1_low ,x1_low ,y0_low = canvas.coords(bars[i])
        for j, _ in enumerate(bars,):
            x0_curr, y1_curr, x1_curr, y0_curr = canvas.coords(bars[j])

    so on what condition do i need to swap bars?


    '''

    #Bubble sort

    '''
    for i, _ in enumerate(bars):
        x0_low, y1_low ,x1_low ,y0_low = canvas.coords(bars[i])  #unpack
        for j, _ in enumerate(bars):
            x0_curr, y1_curr, x1_curr, y0_curr = canvas.coords(bars[j])  #unpack
            if y1_curr > y1_low:
                swap_bars(bars[i],bars[j])
                bars[i], bars[j] = bars[j], bars[i]

    '''
    for i in range(len(bars)-1, -1, -1):
        for j in range(0, i):
            _, y1_low ,_ ,_ = canvas.coords(bars[j+1])
            _, y1_curr, _ , _ = canvas.coords(bars[j])
            if y1_curr < y1_low:
                swap_bars(bars[j],bars[j+1])
                bars[j+1], bars[j] = bars[j], bars[j+1]
        
        window.update()
        time.sleep(0.1)

    #pos0 = bars[0]
    #pos1 = bars[49]

    #swap_bars(pos0, pos1)
    #bars[10], bars[20] = bars[20],bars[10]
            



        #print(x0_current, y1_current ,x1_current ,y0_current)



        


#tkinter is keeps adding to the index
#for exmaple bar should go to 50
#after I delete it it keeps bar count going starting from 50 51

def reset():
    canvas.delete('all')
    bars.clear()
    draw_bars()




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




algo_values = ['Bubble Sort', 'MergeSort']
ttk.Combobox(ui_frame,values=algo_values).grid(row=0,column=0)

start_button = Button(ui_frame, width=15,height=2, text='Start', command= lambda a=bars, b=0:start_algo(a,b)).grid(row=1,column=0)
reset_button = Button(ui_frame, width=15,height=2, text='Reset', command=reset).grid(row=2,column=0)




draw_bars()
#start_algo(bars, 0)

l1 = [7,6,5,89,2]

#Bubble sort python
for i in range(0, len(l1)):
    for j in range(1 + i, len(l1)):
        if l1[i] > l1[j]:
            tmp = l1[i]
            l1[i] = l1[j]
            l1[j] = tmp
            

window.mainloop()
