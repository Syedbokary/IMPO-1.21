import multiprocessing
import time
import runpy
import tkinter as tk
import importlib
from PIL import Image, ImageTk
import threading
import tkinter.font as tkFont

def start_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)

    transparent_color = '#5A0857'
    splash.configure(bg=transparent_color)
    splash.wm_attributes('-transparentcolor', transparent_color)

    img = Image.open("IMPO_Splash2.png").convert('RGBA')
    r, g, b, a = img.split()

    threshold = 180
    mask = a.point(lambda p: 255 if p > threshold else 0)
    bbox = mask.getbbox()
    if bbox:
        img = img.crop(bbox)

    img_width, img_height = img.size
    splash_img = ImageTk.PhotoImage(img)

    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width // 2) - (img_width // 2)
    y = (screen_height // 2) - (img_height // 2)
    splash.geometry(f"{img_width}x{img_height}+{x}+{y}")

    label = tk.Label(splash, image=splash_img, bd=0, bg=transparent_color)
    label.pack()

    Ver_text_font = tkFont.Font(family="Arial", size=14)
    Ver_text = tk.Label(splash, text="Version 1.20", bg='white', font=Ver_text_font)
    Ver_text.place(x=20,y=img_height - 30)
    
    def load_main():
        
        import IMPOFRONT
        IMPOFRONT.main(splash)

    splash.after(2000, lambda: load_main())
    splash.mainloop()


if __name__ == '__main__':
    start_splash()
