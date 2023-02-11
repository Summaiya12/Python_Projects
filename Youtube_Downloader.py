from tkinter import *
from tkinter import filedialog
from pytube import  YouTube
import shutil
def select_video_path():
    path  = filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    shutil.move(mp4_video , user_path)
    screen.title('Download Completed! Download Another Video....')

screen = Tk()
title = screen.title("YouTube Video Downloader")
canvas = Canvas(screen, width=500 , height=800)
canvas.pack()
logo_img = PhotoImage(file='you.png')
logo_img = logo_img.subsample(2,2)
canvas.create_image(250 , 80 , image = logo_img)
link_field = Entry(screen , width=40 , font=('Arial' , 15))
link_label = Label(screen, text="Enter Video Link Below: " , font=('Arial' , 15))


link_fieldPL = Entry(screen , width=40 , font=('Arial' , 15))
link_labelPL = Label(screen, text="Enter Playlist Link Below: " , font=('Arial' , 15))


path_label = Label(screen , text="Select path for download" , font=('Arial' , 15))
select_btn =Button(screen , text="Select Path" , bg='crimson' , padx='22' , pady='5' , font=('Arial' , 15),command=select_video_path)

canvas.create_window(250 , 280 , window=path_label)
canvas.create_window(250 , 330 , window=select_btn)

canvas.create_window(250 , 170 , window=link_label)
canvas.create_window(250 , 220 , window=link_field)


download_btn =Button(screen , text="Download Video" , bg='green' , padx='22' , pady='5' , font=('Arial' , 15),command=download_video)
canvas.create_window(250 , 390 , window=download_btn)


screen.mainloop()