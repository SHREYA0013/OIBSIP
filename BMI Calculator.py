# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 01:08:19 2023

@author: shreya
"""

#BMI Calculator::
#BODY MASS INDEX is a measure of relative weight based on the mass and height of an individual.
#We can categorize people based on their height,weight.
#these categories are UNDERWEIGHT,HEALTHY,OVERWEIGHT
#BMI can be direct measurement of body fat.

name=input("Enter your name: ")
height_of_the_person= float(input("\nEnter your height in cm: "))
weight_of_the_person= float(input("\nEnter your weight in kg: "))
#we take the inputs from the user as a float variable

#the equation to calculate BMI=weight(kg)/{height(cm)}^2

BMI= weight_of_the_person/((height_of_the_person/100)**2)
#we divide height by 100 to convert it to meters from centimeters

print(name + ",Your Body Mass Index is:",BMI)

if BMI>0:
    
    if BMI<=18.5:
        print(name +",Oh no!You are underweight!")
    elif 18.5<BMI<=24.9:  #we can also write elif BMI<=24.9:
        print(name +",Awesome!You are healthy")
    elif BMI<=29.9:
        print(name +",Oops!You are overweight")
    else:
        print("\nSorry!You are obese")
else:
    print("Invalid Input")



#Develop a graphical BMI calculator with a user-friendly interface (GUI) using libraries like Tkinter or PyQt.

#import the necessary library like Tkinter along with all the widget classes, including the messagebox module.

from tkinter import *
from tkinter import messagebox
import tkinter as tk
#for LINUX,UBUNTU we need to install Tkinter otherwise this comes with Python software

def reset_entry():
    age_tf.delete(0,'end')
    weight_tf.delete(0,'end')
    height_tf.delete(0,'end')
    
def calculate_bmi():
    weight= float(weight_tf.get())
    height= float(height_tf.get())
    
    bmi= weight/((height/100)**2)
    #we transform height from centimeters to meters
    #result_label.config(text=f"Your BMI: {bmi:.2f}")
    bmi=round(bmi,2) #round off the multiple decimal values to 2
    bmi_index(bmi)
#first take the inputs weight and height as float.then calculate BMI of the person
#bmi_index is a function to display the result depending upon value and category
    
def bmi_index(bmi):
    if bmi>0:
        if bmi<=18.5:
            messagebox.showinfo('bmi_guidlines',f'BMI={bmi}is Underweight')
            #messagebox.NameOfTheFunction(title, message, **options)  
        elif 18.5<bmi<=24.9:
            messagebox.showinfo('bmi_guidlines',f'BMI={bmi}is Normal')
        elif 24.9<bmi<=29.9:
            messagebox.showinfo('bmi_guidlines',f'BMI={bmi} is Overweight')
        elif bmi>29.9:
            messagebox.showinfo('bmi_guidlines',f'BMI={bmi}is Obsesity')

    else:
        messagebox.showinfo('bmi_guidlines','Invalid input')
 
#creating a new tkinter window and assign it into variable=ws   
ws=Tk()
ws.title('BMI_PythonGuide')
ws.geometry('800x500')
ws.config(bg='#679fce')

var = IntVar()
#creating a Tkinter 'Frame' widget as a child of main window('ws').
#padx & pady is the horizontal and verticle padding,respectively.
#20 pixel of padding on all sides- left,right,top,bottom
frame=Frame(
    ws,
    padx=20,
    pady=20
    )
frame.pack(expand=True)

age_label=Label(
    frame,
    text="Enter your Age(between 2 and 120): ")
age_label.grid(row=1,column=1)

age_tf=Entry(
    frame
    )

#grid geometry manager to place a Tkinter Entry widget within a grid layout
age_tf.grid(row=1,column=2,pady=5)

#entry should be placed in 2nd row and 3rd column
#pady=5 specifies vertical padding (space) around the widget in pixels,there will be 5 pixels of padding on the top and bottom of the widget.

gen_label=Label(
    frame,
    text='Select your Gender')
gen_label.grid(row=2,column=1)

frame_2nd=Frame(
    frame)
frame_2nd.grid(row=2,column=2,pady=5)

#Radiobuttons are used to represent a set of mutually exclusive options, where the user can choose only one option from the set.
#Radiobuttons in the same group (i.e., those that share the same variable) are mutually exclusive, meaning that selecting one automatically deselects the others in the group.
#Radiobutton should be placed on the left and right side of its parent container.

male_rb=Radiobutton(
    frame_2nd,
    text='Male', #label is male
    variable=var,
    value=1
    )
male_rb.pack(side=LEFT)

female_rb=Radiobutton(
    frame_2nd,
    text='Female',
    variable=var,
    value=2
    )
female_rb.pack(side=RIGHT)

height_label=Label(
    frame,
    text="Enter your Height(in cm.)"
    )
height_label.grid(row=3,column=1)

weight_label=Label(
    frame,
    text="Enter your weight(in kg.)"
    )
weight_label.grid(row=4,column=1)

height_tf=Entry(
    frame
    )
height_tf.grid(row=3,column=2,pady=5)

weight_tf=Entry(
    frame
    )
weight_tf.grid(row=4,column=2,pady=5)
    

frame_3rd=Frame(
    frame
    )
frame_3rd.grid(row=5,columnspan=3,pady=10)


calculator_button=Button(
    frame_3rd,
    text='Calculation',
    command=calculate_bmi
    )
calculator_button.pack(side=RIGHT)

reset_button=Button(
    frame_3rd,
    text='Reset',
    command=reset_entry
    )
calculator_button.pack(side=RIGHT)

exit_button=Button(
    frame_3rd,
    text='Quit',
    command=ws.quit()
    )
exit_button.pack(side=RIGHT)

bmi = tk.Label(ws, text="")
bmi.pack()

ws.mainloop()

#VISUALIZATION:
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

#sample historical data:
data= {
       'year':[2015,2016,2017,2018,2019,2020,2021,2022,2023],
       'bmi':[23,24,25,26,27,28,29,30,31]}

df=pd.DataFrame(data)

plt.figure(figsize=(20,10))
plt.plot(df['year'],df['bmi'],marker='o',linestyle='dotted', color='red')

plt.title('Historical BMI data over Years')
plt.xlabel('year')
plt.ylabel('bmi')

plt.grid(True)
plt.show()
           












