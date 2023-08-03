from tkinter import *
from tkinter import ttk
import random
import time


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

    #should be 700
    for x in range(0, 700, 14):
        random_y = random.randint(1,590)
        bar = canvas.create_rectangle(x ,600, x+10 ,random_y, fill='black' )
        bars.append(bar)



def swap_bars(bar_0, bar_1):

    #get the x coords for each bar
    x00, _ , x01, _ = canvas.coords(bar_0)
    x10, _ , x11, _ = canvas.coords(bar_1)

    diff = x00 - x10

    #move them
    canvas.move(bar_0, -diff,0) 
    canvas.move(bar_1, +diff,0)
       


def start_algo(bars, tick_time):

    #first bar in list
    #canvas.itemconfig(bars[0], fill='red')
    #canvas.itemconfig(bars[49], fill='blue')

   
    #Bubble sort
    '''
    for i, _ in enumerate(bars):
        _, y1_low ,_ ,_ = canvas.coords(bars[i])  #unpack
        for j, _ in enumerate(bars[1:]): 
                _, y1_curr, _ , _ = canvas.coords(bars[j])  #unpack
                print(i,j)
                if y1_curr < y1_low:
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
              
    

    
def reset():
    canvas.delete('all')
    bars.clear()
    draw_bars()



algo_values = ['Bubble Sort', 'MergeSort']
ttk.Combobox(ui_frame,values=algo_values).grid(row=0,column=0)

start_button = Button(ui_frame, width=15,height=2, text='Start', command= lambda a=bars, b=0:start_algo(a,b)).grid(row=1,column=0) 
reset_button = Button(ui_frame, width=15,height=2, text='Reset', command=reset).grid(row=2,column=0)


draw_bars()


window.mainloop()
