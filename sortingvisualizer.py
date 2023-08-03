from tkinter import *
from tkinter import ttk
import random
import time

'''
TO DO

Make algo only run after drop down and start
change function to bubble sort
fix ui bar
add speed dropdown?


To set speed add variable back to lambda, add arg back to function, create tk combobox, speed options, 

'''


window = Tk()
window.resizable(True,False)
canvas = Canvas(window)

WIDTH = 700

ui_frame = Frame(window, width=250, height=600, bg = 'red')
ui_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(window, width=700, height=600, bg='black')
canvas.grid(row=0, column=1)

bars = []

def draw_bars():
    
    for x in range(0, WIDTH, 14):
        random_y = random.randint(1,590)
        #or x ,600, x+10 ,random_y, fill='black'  or  x, random_y, x+10, 600, fill='black'
        #maybe no fill looks kind of cool
        bar = canvas.create_rectangle(x ,600, x+10 ,random_y , outline='white')
        bars.append(bar)


def swap_bars(bar_0, bar_1):
    x00, _ , x01, _ = canvas.coords(bar_0)
    x10, _ , x11, _ = canvas.coords(bar_1)

    canvas.move(bar_0, x10-x00,0)
    canvas.move(bar_1,x01-x11,0)



def start_algo(bars ,speed):

    if algo_val_string.get() == 'Bubble Sort':

        reset_button.config(state=DISABLED)

        for i in range(len(bars)-1, -1, -1):
            for j in range(0, i):
                _, y1_low ,_ ,_ = canvas.coords(bars[j])
                _, y1_curr, _ , _ = canvas.coords(bars[j+1])
                if y1_curr > y1_low and i > j:
                    swap_bars(bars[j],bars[j+1])
                    bars[j+1], bars[j] = bars[j], bars[j+1]
            
            window.update()
            if speed_value_string.get() == 'Fast':
                time.sleep(.01)
            elif speed_value_string.get() == 'Medium':
                time.sleep(.1)
            elif speed_value_string.get() == 'Slow':
                time.sleep(.3)
        
        for k in range(0, len(bars)):
            canvas.itemconfig(bars[k], fill='green') 
            window.update()
            time.sleep(.01)  
        
            reset_button.config(state=NORMAL)
    
    '''
    for i in range(len(bars)-1, -1, -1):
        for j in range(0, i):
            _, y1_low ,_ ,_ = canvas.coords(bars[j+1])
            _, y1_curr, _ , _ = canvas.coords(bars[j])
            if y1_curr < y1_low and i > j:
                swap_bars(bars[j],bars[j+1])
                bars[j+1], bars[j] = bars[j], bars[j+1]
        
        window.update()
        time.sleep(.07)
    
    for k in range(0, len(bars)):
        canvas.itemconfig(bars[k], fill='green') 
        window.update()
        time.sleep(.01)  
    
        reset_button.config(state=NORMAL)
    

    '''


def reset():
    canvas.delete('all')
    bars.clear()
    draw_bars()



algo_values = ['Bubble Sort', 'MergeSort']
algo_val_string = StringVar()
algo_options = ttk.Combobox(ui_frame,values=algo_values, textvariable=algo_val_string)
algo_options.grid(row=0,column=0)

algo_options.current(0)

speed_values = ['Fast', 'Medium', 'Slow']
speed_value_string = StringVar()
speed_options = ttk.Combobox(ui_frame, values=speed_values, textvariable=speed_value_string)
speed_options.grid(row=0,column=1)

speed_options.current(1)

draw_bars() 

start_button = Button(ui_frame, width=15,height=2, text='Start', command= lambda a=bars:start_algo(a ,speed_value_string))
start_button.grid(row=1,column=0)
reset_button = Button(ui_frame, width=15,height=2, text='Reset', command=reset)
reset_button.grid(row=2,column=0)



window.mainloop()
