from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageT

from img_stg import ImgStg
from file_handler import fileHandler
from utils import compatible_path
from queue import Queue



# GUI - TKINTER
window = Tk()
window.title("STEG") # title of the window
window.geometry("800x780") # size of the window
window.configure(bg = "#ffffff") # background color of the window

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = compatible_path(RESOURCES + "bg.png"))
background = canvas.create_image(
    344.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = compatible_path(RESOURCES + "img0.png"))

b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = reset_btn,
    relief = "flat")

b0.place(
    x = 606, y = 227,
    width = 69,
    height = 72)

img1 = PhotoImage(file= compatible_path(RESOURCES + "img1.png"))

b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = embed_btn,
    activebackground="#E8CCCC",
    relief = "flat")

b1.place(
    x = 56, y = 670,
    width = 108,
    height = 100)

img2 = PhotoImage(file = compatible_path(RESOURCES + "img2.png"))

b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = extract_btn,
    activebackground="#E6C7C7",
    relief = "flat")

b2.place(
    x = 260, y = 670,
    width = 108,
    height = 100)

img3 = PhotoImage(file = compatible_path(RESOURCES + "file.png"))

b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_dest_btn,
    activebackground="#EAD1D1",
    relief = "flat")

b3.place(
    x = 21, y = 316,
    width = 74,
    height = 75)

img4 = PhotoImage(file = compatible_path(RESOURCES + "image.png"))

b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_img_btn,
    activebackground="#EBD3D3",
    relief = "flat")

b4.place(
    x = 21, y = 230,
    width = 74,
    height = 75)

img5 = PhotoImage(file = compatible_path(RESOURCES + "folder.png"))

b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_text_btn,
    activebackground="#ECD6D6",
    relief = "flat")

b5.place(
    x = 21, y = 144,
    width = 74,
    height = 75)

img6 = PhotoImage(file = compatible_path(RESOURCES + "audio.png"))

b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_audio_btn,
    activebackground="#EBD3D3",
    relief = "flat")

b6.place(
    x = 21, y = 535,
    width = 74,
    height = 75)

msg1 = Label(text="SELECT TEXT FILE",font=("Arial", 14))
msg1.place(x=100, y=163, width=300, height=40)
msg2 = Label(text="SELECT IMAGE FILE",font=("Arial", 14))
msg2.place(x=100, y=249, width=300, height=40)
msg3 = Label(text="SELECT DEST FOLDER",font=("Arial", 14))
msg3.place(x=100, y=335, width=300, height=40)
msg6 = Label(text="Enter Message:",font=("Arial", 14))
msg6.place(x=21, y=402, width=380, height=40)
msg7_text = Text(window, height=3, width=40, font=("Arial", 12))
msg7_text.place(x=21, y=450, width=372, height=75)
scrollbar = Scrollbar(window, command=msg7_text.yview)
scrollbar.place(x=384, y=450, height=75)
msg7_text.config(yscrollcommand=scrollbar.set)

msg8 = Label(text="SELECT AUDIO FILE",font=("Arial", 14))
msg8.place(x=100, y=555, width=300, height=40)

msg9 = Label(text="EMBED DATA",font=("Arial", 14))
msg9.place(x=21, y=625, width=180, height=40)
msg9 = Label(text="EXTRACT DATA",font=("Arial", 14))
msg9.place(x=220, y=625, width=180, height=40)
msg10 = Label(text="RESET",font=("Arial", 14))
msg10.place(x=590, y=300, width=100, height=40)


IMAGE = ImageTk.PhotoImage(Image.open(compatible_path(RESOURCES) + "no_image.png").resize((295,279)))

p1 = PhotoImage(file = compatible_path(RESOURCES + "ico_menu.png"))
window.iconphoto(False, p1)

label1 = Label()
label1.place(x=470, y=450)
label1.configure(image=IMAGE)
label1.image=IMAGE

T = Text(window, height = 5, width = 65)
T.insert(END, "...")
T.place(x=55, y=35)
T.config(borderwidth=0,state=DISABLED)

window.resizable(False, False)
window.mainloop()
