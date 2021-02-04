from tkinter import Tk, Label, Button, Entry, StringVar, Text
from tkinter.constants import CENTER

import discord

from dotenv import load_dotenv
import os

class DeveloperGui:
  def __init__(self, client):
    self.client = client

  def next(self, cmd, destroy=True, win=None):
    if destroy:
      win.update()
      win.destroy()

    cmd()

  def main(self):

    win = Tk()
    Button(win, text="ANNOUNCE", command=lambda: self.next(self.announcement, True, win)).place(relx=0.5, rely=0.3, anchor=CENTER)
    win.mainloop()

  def announcement(self):
    def _login():
      def _check():
        un = uname.get()
        pw = pword.get()

        load_dotenv()
        pswrd = os.getenv("gui_pass")
        usrnm = os.getenv("gui_user")

        if un == usrnm and pw == pswrd:
          login.destroy()
          _main()

      login = Tk()

      uname = StringVar()
      pword = StringVar()

      Label(login, text="USERNAME").grid(row=1, column=1)
      Label(login, text="PASSWORD").grid(row=3, column=1)

      Entry(login, textvariable=uname).grid(row=1, column=2)
      Entry(login, textvariable=pword, show="*").grid(row=3, column=2)

      Button(login, text="Submit", command=_check).grid(row=5, column=2, sticky="W")
      Button(login, text="Back", command=lambda: self.next(self.main, True, login)).grid(row=5, column=2, sticky="E")

      login.mainloop()

    def _main():
      def _tosend():
        input = text.get("1.0",'end-1c')
        _send(input)

      main = Tk()
      text = Text(main).place(relx=0.5, rely=0.5, anchor=CENTER)

      Button(main, text="SEND", command=_tosend).place(relx=0.3, rely=0.8, anchor=CENTER)
      Button(main, text="BACK", command=lambda: self.next(self.main, True, main)).place(relx=0.6, rely=0.8, anchor=CENTER)
      
      main.mainloop()

    def _send(data):
      # takes the input from _main and sends it to all the system channels or a specified channel
      print(data)

    _login()