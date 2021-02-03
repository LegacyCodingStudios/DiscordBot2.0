from tkinter import Tk, Label, Button, Entry, StringVar
from tkinter.constants import CENTER

import discord

from dotenv import load_dotenv
import os

class DeveloperGui:
  def __init__(self, client):
    self.client = client

  def next(self, cmd, destroy=True, win=None):
    if destroy:
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
        creds = os.getenv("gui_creds")

        if un == creds[0] and pword == creds[1]:
          #login.destroy()
          _main()

      login = Tk()

      uname = StringVar()
      pword = StringVar()

      Label(login, text="USERNAME").grid(row=1, column=1)
      Label(login, text="PASSWORD").grid(row=3, column=1)

      Entry(login, textvariable=uname).grid(row=1, column=2)
      Entry(login, textvariable=pword, show="*").grid(row=3, column=2)

      Button(login, text="Submit", command=_check).grid(row=5, column=2, sticky="W")
      Button(login, text="Back", command=self.next(self.main, True, login)).grid(row=5, column=2, sticky="E")

      pass

    def _main():
      # only do this once logged in so not everone can do this thru the web link
      print("main")
      pass

    def _send():
      # takes the input from _main and sends it to all the system channels or a specified channel
      pass

    _login()