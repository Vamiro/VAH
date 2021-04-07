import tkinter as tk
import time
import random

def click_button():
    import numpy as np
    I_text = Entry3.get()
    I_text += '.txt'
    Textfile = open(I_text, 'w')
    MaxI = Entry1.get()
    step_pos = Entry2.get()
    np.double(step_pos)
    np.double(MaxI)
    MinI = np.double(MaxI)
    MinI = MinI * (-1)
    np.double(MinI)
    step_pos = Entry2.get()
    np.double(step_pos)
    root2 = tk.Tk()
    root2.title("Graph")
    hscreen_width = root2.winfo_screenwidth() // 4
    hscreen_height = root2.winfo_screenheight() // 4 + 30
    root2.geometry('980x640+{}+{}'.format(hscreen_width, hscreen_height))
    c = tk.Canvas(root2, width=980, height=640, bg="black")
    c.pack()
    c.create_line(490, 40, 490, 600, width=2, fill="white", arrow=tk.FIRST)
    c.create_line(40, 320, 940, 320, width=2, fill="white", arrow=tk.LAST)
    c.create_text(480, 40, text = "I", fill = "white", font="Verdana 10", anchor="w")
    c.create_text(940, 330, text = "U", fill = "white", font="Verdana 10", anchor="w")
    sdvig = 40
    txx=-1.0
    while sdvig <= 940:
        c.create_text(sdvig - 10, 325, text = round(txx, 1), fill = "white", font="Verdana 8", anchor="w")
        txx += 0.1
        c.create_line(sdvig, 40, sdvig, 600, width=0.1, fill="grey")
        sdvig += 45
    U = 450 / (1 / np.double(step_pos))
    np.double(U)
    end = 0
    x = 490
    y = 320
    v_max = 1.01
    v_min = 0
    level_list = np.arange(0.02, v_max, np.double(step_pos), dtype=np.double)
    for level in level_list:
        I = random.randint(-25, 100)
        c.create_line(x, y, 490 + U, 320 - I, width=2, fill="red")
        Textfile.write(str(I) + ' I; ' + str(U) + ' V' + '\n')
        x = 490 + U
        y = 320 - I
        U += 450 / (1 / np.double(step_pos))
        if np.double(I) >= np.double(MaxI) or np.double(I) <= np.double(MinI):
            break
            end = 1
        root2.update()
        time.sleep(0.01)
    if end == 0:
        U -= 450 / (1 / np.double(step_pos))
        v_max = 1
        v_min = -1.01
        level_list = np.arange(v_max, v_min, np.double(step_pos) * -1, dtype=np.double)
        for level in level_list:
            I = random.randint(-100, 25)
            c.create_line(x, y, 490 + U, 320 - I, width=2, fill="green")
            Textfile.write(str(I) + ' I; ' + str(U) + ' V' + '\n')
            x = 490 + U
            y = 320 - I
            U -= 450 / (1 / np.double(step_pos))
            if np.double(I) >= np.double(MaxI) or np.double(I) <= np.double(MinI):
                break
            root2.update()
            time.sleep(0.01)
    def move_start(event):
        c.scan_mark(event.x, event.y)
    def move_move( event):
        c.scan_dragto(event.x, event.y, gain=1)
    pressed = False  
    #масштабирование
    def pressed2(event):
        global pressed
        pressed = not pressed
        c.scan_mark(event.x, event.y)
    def move_move2(event):
        if pressed:   
            c.scan_dragto(event.x, event.y, gain=1) 
    def zoomer(event):
        if (event.delta > 0):
            c.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            c.scale("all", event.x, event.y, 0.9, 0.9)
        c.configure(scrollregion = c.bbox("all"))
    c.bind("<MouseWheel>",zoomer)
    root2.bind_all("<MouseWheel>",zoomer)
    c.bind("<ButtonPress-1>", move_start)
    c.bind("<B1-Motion>", move_move)
    c.bind("<ButtonPress-2>", pressed2)
    c.bind("<Motion>", move_move2)
    root2.update()
    Textfile.close()
    root2.mainloop()

root = tk.Tk()
root.title("Menu")
hscreen_width = root.winfo_screenwidth() // 4
hscreen_height = root.winfo_screenheight() // 4
root.geometry('980x640+{}+{}'.format(hscreen_width, hscreen_height))
    
max1_label = tk.Label(text="MinI-MaxI mI:", font="Verdana 10")
max1_label.grid(row=0, column=0, sticky="w")
step_label = tk.Label(text="Step:", font="Verdana 10")
step_label.grid(row=1, column=0, sticky="w")
txt_label = tk.Label(text="Name:", font="Verdana 10")
txt_label.grid(row=2, column=0, sticky="w")
Entry1 = tk.Entry(root,width=20,font='Verdana 10')
Entry1.grid(row=0,column=1, padx=5, pady=5)
Entry2 = tk.Entry(root,width=20,font='Verdana 10')
Entry2.grid(row=1,column=1, padx=5, pady=5)
Entry3 = tk.Entry(root,width=20,font='Verdana 10')
Entry3.grid(row=2,column=1, padx=5, pady=5)

button1 = tk.Button(text="START", background="black", activebackground="red", foreground="red", bd="4", padx="20", pady="8", font="Verdana 16", command = click_button)
button1.place(x=0, y=95)

root.mainloop()