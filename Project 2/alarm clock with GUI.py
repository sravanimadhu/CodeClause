from tkinter import *
import datetime
import time
from playsound import playsound

def Alarm(set_alarm):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%y")
        msg = "Current Time: "+str(cur_time)
        print(msg+" "+cur_date)
        if cur_time == set_alarm:
            playsound(r'C:\Users\SREEVALLI REDDY\OneDrive\Desktop\Alarm\alarma.mp3')
            break

def get_alarm():
    alarm_set = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set)

window = Tk()
window.title("Alarm Clock")
window.geometry("400x160")
window.config(bg="skyblue")
window.resizable(width=False,height=False)

time_format = Label(window, text="Set Time In 24 Hour Format Only!", fg="black", bg="#CDC0B0", font=("Poppins",15)).place(x=25,y=120)
add_time = Label(window, text="  Hr        Min      Sec ", font=90, fg="white", bg="black").place(x=210)
set_your_alarm = Label(window, text="Set Time For Alarm: ", fg="black", bg="#CDC0B0", relief="solid", font=("Helevetica",12,"bold")).place(x=10,y=41)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(window, textvariable= hour, fg="black", bg="white", width=4, font=(20)).place(x=210,y=40)
minTime = Entry(window, textvariable= min, fg="black", bg="white", width=4, font=(20)).place(x=270,y=40)
secTime = Entry(window, textvariable= sec, fg="black", bg="white", width=4, font=(20)).place(x=330,y=40)

submit = Button(window, text="Set Your Alarm", fg="black", bg="#D4AC0D", width=15, command=get_alarm, font=(20)).place(x=100,y=80)

window.mainloop()