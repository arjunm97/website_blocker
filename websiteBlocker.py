# -*- coding: utf-8 -*-
"""
Created on Sun Jul 8 04:14:30 2020

@author: Arjun
"""

from datetime import datetime
from tkinter import *
from tkinter import messagebox  



x=[]

##### Getting input#####
def insert_command():
   
    
    print('working')
    x.append(e1.get())
    x.append(e2.get())
    x.append(e3.get())
    x.append(e4.get())
    x.append(e5.get())
    print(x)
    messagebox.showwarning("Blocking Started","Blocking as started!Click close for the program to run!") 
        
    

window=Tk()
window.wm_title("Website Blocker[EndlessBay Studios]")
l1=Label(window,text="Website 1:")
l1.grid(row=0,column=0)

l2=Label(window,text="Website 2:")
l2.grid(row=1,column=0)

l3=Label(window,text="Website 3:")
l3.grid(row=0,column=2)

l4=Label(window,text="Website 4:")
l4.grid(row=1,column=2)

l5=Label(window,text="Website 5:")
l5.grid(row=2,column=0)

l5=Label(window,text="Websites will be blocked for 3 Hours")
l5.grid(row=2,column=2)

l6=Label(window,text="Just enter the name of the wesite eg:(facebook),(youtube).Do not include the (www,com)part..")
l6.grid(row=4,column=1)

l7=Label(window,text="Close all browsers before running the program for the program to work properly")
l7.grid(row=5,column=1)

l8=Label(window,text="After selecting the start blocking and getting the message.Click close for the program to run")
l8.grid(row=6,column=1)

e1=Entry(window)
e1.grid(row=0,column=1)

e2=Entry(window)
e2.grid(row=1,column=1)

e3=Entry(window)
e3.grid(row=0,column=3)

e4=Entry(window)
e4.grid(row=1,column=3)

e5=Entry(window)
e5.grid(row=2,column=1)


b3=Button(window,text="Start Blocking",width=12,command=insert_command)
b3.grid(row=5,column=2)


b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=2)


window.mainloop()


## X has the the websites 
websites=x


print("Starting ....")


from datetime import datetime as dt
import time
host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=[]

def spaceremove(string): 
    return string.replace(" ", "") 
      
print("Processing....")
for i in websites:
    x=spaceremove(i)
    fullname1="www."+x+".com"
    fullname2=x+".com"
    website_list.append(fullname1)
    website_list.append(fullname2)
    


### List of website ready and taken 

print("Starting block...")


##opening and blocking websites
with open(host_path,'r+') as file:
    content=file.read()
    file.truncate(0)
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect+" "+website+"\n")
  
endtime=3*60*60
#Timer
print("Blocking started...")
time.sleep(endtime)
print("Blocking done...")

print("Working on unblocking...")


##Opening and unblocking websites
       
with open(host_path,'r+') as file:
    content=file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()

print("Program done...")
