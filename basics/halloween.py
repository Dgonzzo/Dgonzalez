import tkinter as tk

windows = tk.Tk()
windows.title('Halloween 2024')

canvas = tk.Canvas(windows, width=400, height=400, background='black')
canvas.pack()

canvas.create_text(200, 50, text='Happy Halloween 2024', fill='white', font=('Comic Sans', 22, 'bold'))

canvas.create_oval(100, 150, 300, 350, fill='orange', outline='')

# Pumpkin's eyes
canvas.create_polygon(150, 200, 
                      170, 250,
                      130, 250) # left eye
canvas.create_polygon(250, 200,
                      230, 250,
                      270, 250) # right eye

# Pumpkin's nose
canvas.create_polygon(200, 280,
                      190, 260,
                      210, 260)

# Pupmkin's mouth
canvas.create_polygon(
    140, 300,
    260, 300,
    
    240, 320,
    220, 300,
    
    200, 320,
    180, 300,
    
    160, 320,
    fill='black' 
)

# grasp
canvas.create_rectangle(0, 350,
                        400, 400,
                        fill='green', outline='')

# canvas.create_rectangle(10,10,20,20, fill='red')

def show_boo(event=None):
    boo_text = canvas.create_text(200,100, text='Tonto el q lo lea', fill='red',font=('Arial', 19, 'bold'))
    
    canvas.after(2000, canvas.delete, boo_text)

canvas.bind('<Button-1>',show_boo)

windows.mainloop()

