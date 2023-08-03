    reset_button.config(state=DISABLED)


        for i in range(len(bars)-1, -1, -1):
            for j in range(0, i):
                _, y1_low ,_ ,_ = canvas.coords(bars[j])
                _, y1_curr, _ , _ = canvas.coords(bars[j+1])
                if y1_curr > y1_low and i > j:
                    swap_bars(bars[j],bars[j+1])
                    bars[j+1], bars[j] = bars[j], bars[j+1]
            
            window.update()
            time.sleep(.1)
        
        for k in range(0, len(bars)):
            canvas.itemconfig(bars[k], fill='green') 
            window.update()
            time.sleep(.01)  
        
            reset_button.config(state=NORMAL)