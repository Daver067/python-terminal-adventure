from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

# grabs current time
start_time = time.time()

# Let's sleep is basically a timer... arg is in seconds (30 mins)
time.sleep(1800)

# grabs the time after the sleep has ended
end_time = time.time()

# should be 30 minutes, just to make sure lets do some math
elapsed_time = end_time - start_time

# Brings up an alert
root = tk.Tk()
root.withdraw()
messagebox.showwarning('alert title', f'Time To Commit! {(round(elapsed_time)/60)} Minutes Ellapsed')
