from tkinter import *

'''
Create a window try and draw an array of rectangles of various size right next to each other
- start putting them highest to lowest
- after this randomize their postiions

Num rectangles used global namepsace NUMBARS = 50 used to loop through and draw?


'''

window = Tk()
window.title("Sorting Algorithm Visualizer")
window.resizable(False,False)

WIDTH = 700


ui_frame = Frame(window, width=250, height=600, bg = 'red')
ui_frame.grid(row=0, column=0, padx=10, pady=10)

#width was 700
canvas = Canvas(window, width=610, height=600)
canvas.grid(row=0, column=1)

bars = []

#Code to draw rectangle across screen
#now we need to adjust their heights
#randomize their postions
#for x in range(0, WIDTH, 14):
#    canvas.create_rectangle(x, 600, x+10, x, fill='black')

#every rect is 10 x 600 - 

#for x in range(0, WIDTH, 14):
   #canvas.create_rectangle(x, 600, x+10, x, fill='black')
   #print(x, 600, x+10, x)



'''
What does Bar class need?
needs an x coord
needs a y coords
needs a width
needs to now its left and right neighbor and the height of ots left and right neighbor

'''



'''
Create an array of rects
spread across screen

use another loop and itemconfig every rect
if rect[i].height

'''

#or should we randomize them before creating the bars?
#after we have each bar how do we know randomize the positions?

class Bar:
    def __init__(self, x0, y0, x1, y1, color) -> None:
        self.rect = canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.color = color

        #Will configure items
        #How to configure just one?
        #canvas.itemconfig(self.rect, fill='blue')

        #Calculate the height of each bar, use it to compare against other bars
        self.height = y0 - y1

        #Each bar needs to know its left and right neighbor, to compare heights
        self.left_neighbor = None
        self.right_neighbor = None


'''
def on_click():
   canvas.itemconfig(line, fill="green")

'''

#Create all the bars, and append them
def draw_bars(x0, y0, x1, y1, color):
        bar = Bar(x0,y0,x1,y1,color)
        bars.append(bar)


#draw and arrange bars bars
for x in range(0, WIDTH, 14):
    draw_bars(x, 600, x+10, x, 'black')


#Randomize positions of inididual bars, use array?
print(bars[0].rect.itemconfig())



print(bars[0].color, bars[3].height)






window.mainloop()
