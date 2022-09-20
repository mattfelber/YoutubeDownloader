import tkinter
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("640x480")
root.title("Youtube Downloader")
icon = PhotoImage(file='yt.png')
root.iconphoto(True, icon)
root.config(bg='black')
root.resizable(False, False)

my_label_frame = LabelFrame(root, text="Paste video URL below:", font=('Calibre', 15))
my_label_frame.pack(pady=0)

my_entry = Entry(my_label_frame, font=("Helvetica", 18), fg="black", width=47)
my_entry.pack(pady=20, padx=20)


def download():
    link = str(my_entry.get())
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    a = tkinter.Label(root, text="Success! File saved to: /YTDownload folder.",
                      font=('Helvetica', 20), bg="black", foreground="darkorchid")
    a.pack()
    print(f'\n' + 'Downloaded: ', yt.title, '~ viewed', yt.views, 'times.')


# button-frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Two Buttons:
dlbutton = Button(button_frame, text="Download", font=("Helvetica", 33), fg="green", bg="black",
                  command=download)
dlbutton.grid(row=0, column=0, padx=0)

# use transparency level 0.1 to 1.0 (no transparency)
root.attributes("-alpha", 0.88, )

root.mainloop()
