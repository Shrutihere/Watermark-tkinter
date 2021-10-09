from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# select images
# select logo
# set logo
# apply to all and save

def save():
    for img in all_images:
        pic = Image.open(img)
        pic.paste(LOGO, OFFSET)
        pic.save(fp=f"{img}.png")
    save_btn.config(text="Saved", state="disable" )

def up(event):
    global OFFSET
    OFFSET = [OFFSET[0], OFFSET[1]-15]
    IMG = Image.open(all_images[0])
    place(IMG, LOGO, OFFSET)

def down(event):
    global OFFSET
    OFFSET = [OFFSET[0], OFFSET[1]+15]
    IMG = Image.open(all_images[0])
    place(IMG, LOGO, OFFSET)

def left(event):
    global OFFSET
    OFFSET = [OFFSET[0]-15, OFFSET[1]]
    IMG = Image.open(all_images[0])
    place(IMG, LOGO, OFFSET)

def right(event):
    global OFFSET
    OFFSET = [OFFSET[0]+15, OFFSET[1]]
    IMG = Image.open(all_images[0])
    place(IMG, LOGO, OFFSET)

def place(img, logo, offset):
    img.paste(logo, offset)
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel = Label(window, image = img, padx=50, pady=50)
    panel.image = img
    panel.grid(row = 3, column=1, columnspan=3)


def logo():
    global IMG, LOGO, OFFSET
    logo_img = filedialog.askopenfilename(title ='Photos')
    LOGO = Image.open(logo_img)
    lg_w, lg_h = LOGO.size

    IMG = Image.open(all_images[0])
    img_w, img_h = IMG.size
    
    OFFSET = [(img_w - lg_w) // 2, (img_h - lg_h) // 2]
    place(IMG, LOGO, OFFSET)


def openfilename():
    global all_images
    all_images = filedialog.askopenfilenames(title ='Photos')
    img = Image.open(all_images[0])
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image = img, padx=50, pady=50)
    panel.image = img
    panel.grid(row = 3, column=1, columnspan=3)    

window = Tk()
window.title("Water Marking App")
window.config(padx=100, pady= 100, bg="#F3D5C0" )
window.geometry("1500x1000")


title = Label(window, text="Add Custom Watermarks To Your Photos\n(Use up, down, left, right arrows to place the logo)", font = "Courier 30", bg="#F3D5C0", padx=60, pady=30)
title.grid(row=1, column=1, columnspan=3)


btn1 = Button(window, text ='Choose Images', command = openfilename, font= "Times 20", bg="#506D84")
btn1.grid(row = 2, column = 1, columnspan=1)

btn2 = Button(window, text ='Choose Logo', command = logo, font= "Times 20", bg="#506D84")
btn2.grid(row = 2, column = 2, columnspan=1)

save_btn = Button(window, text ='Save', command = save, font= "Times 20", bg="#506D84")
save_btn.grid(row = 2, column = 3, columnspan=1)

window.bind('<Up>', up)
window.bind('<Down>', down)
window.bind('<Left>', left)
window.bind('<Right>', right)

window.mainloop()
