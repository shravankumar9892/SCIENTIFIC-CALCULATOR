################################ | PyCal | ################################### 
from tkinter import *
from easygui import ccbox
import tkinter.font as tk_Font
from tkinter import messagebox
from math import *
from functions import *
##############################################################################
dia_message = ''' PyCal is created to simplify the calculations, 
                        which normal calculators don't help with ...
                                                     


                                                             -SVNIT    '''
##### main window with permission of ccbox #### 

if ccbox(dia_message, "Pycal"):     # show a Continue/Cancel dialog
    class Application(Frame):
        """ Main class for calculator"""

        def __init__(self, master):
            """ Initialise the Frame. """
            super().__init__()    # @@@@@@@@@@@@@
            self.task=""
            self.UserIn=StringVar()
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            """ Create all the buttons for calculator. """
        # User input stored as an Entry widget.
            
            # GCD of 2 numbers
            self.button1 = Button(self,bg="#fffff0",fg='#313f4f',activebackground='#313f4f',activeforeground='#fffff0',bd=12,text="gcd()", font = 
            ("Helvetica", 20, "bold"),cursor='pencil', command = lambda : self.buttonClick('gcd(,)'))
            self.button1.grid(row = 2, column = 0, sticky = W+E)
            
            # Sum of squares bw any 2 numbers
            self.button2 = Button(self, bg="#fffff0",fg='#800000',activebackground='#800000',activeforeground='#fffff0',bd = 12, text = 
            "\u2211x\u00b2", command = lambda : self.buttonClick('sum_squares(,)'), cursor='pencil',font = ("Helvetica", 20, "bold"))
            self.button2.grid(row = 2, column = 1)

            # Button for value 9
            self.button3 = Button(self ,bg="#00ffff",fg='#000000' ,activebackground='#fffff0',activeforeground='#00ffff', bd = 12, text = "9",command = 
            lambda : self.buttonClick(9),cursor='pencil', font = ("Helvetica", 20, "bold"))
            self.button3.grid(row = 2, column = 2, sticky = W)

            # step_function
            self.button4 = Button(self, bg="#fffff0",fg='#313f4f',activebackground='#313f4f',activeforeground='#fffff0', bd = 12,text = "[x]",command 
            = lambda : self.buttonClick('floor()'), cursor='pencil',font = ("Helvetica", 20, "bold"))
            self.button4.grid(row = 3, column = 0, sticky = W+E)

            # Sum of cubes bw any 3 numbers
            self.button5 = Button(self, bg="#fffff0",fg='#800000',activebackground='#800000',activeforeground='#fffff0', bd = 12, text = 
            "\u2211x\u00b3",command = lambda : self.buttonClick('sum_cubes()'),cursor='pencil', font = ("Helvetica", 20, "bold"))
            self.button5.grid(row = 3, column = 1, sticky = W)

            # Button for value 6
            self.button6 = Button(self, bg="#fffff0",fg='#800000',activebackground='#800000',activeforeground='#fffff0', bd = 12, text = 
            "6",cursor='pencil',command = lambda : self.buttonClick(6), font = ("Helvetica", 20, "bold"))
            self.button6.grid(row = 3, column = 2, sticky = W+E)

            # factorial
            self.button7 = Button(self,bg="#fffff0",fg='#313f4f',activebackground='#313f4f',activeforeground='#fffff0', bd = 12, text = "x!", 
            cursor='pencil',command = lambda : self.buttonClick('factorial()'), font = ("Helvetica", 20, "bold"))
            self.button7.grid(row = 4, column = 0, sticky = W+E)

            # Button for value 2
            self.button8 = Button(self, bg="#fffff0",fg='#800000',activebackground='#800000',activeforeground='#fffff0',bd = 12, text = 
            "2",cursor='pencil',command = lambda : self.buttonClick(2), font = ("Helvetica", 20, "bold"))
            self.button8.grid(row = 4, column = 1, sticky = W+E)

            # Button for value 3
            self.button9 = Button(self, bg="#07d6f1",fg='#000000',activebackground='#fffff0',activeforeground='#00ffff', bd = 12, text = "3",command = lambda : self.buttonClick(3), cursor='pencil',font = ("Helvetica", 20, "bold"))
            self.button9.grid(row = 4, column = 2, sticky = W)

            # log of random base
            self.button9 = Button(self, bg="#fffff0",fg='#313f4f',activebackground='#313f4f',activeforeground='#fffff0', bd = 12, text = "log(num,base)",command = lambda : self.buttonClick('log(,)'), font = ("Helvetica", 12, "bold"))
            self.button9.grid(row = 5, column = 0, sticky = W)

            # Exponent buttons
            # Square Value
            self.Addbutton = Button(self, bg="#fffff0",fg='#f3bb1d',activebackground='#f3bb1d',activeforeground='#fffff0', bd = 12, text = "x\u00b2",
            command = lambda : self.buttonClick("()**2"), font = ("Helvetica", 20, "bold"))
            self.Addbutton.grid(row = 2, column = 3, sticky = W+E)

            # Power of a given number
            self.Subbutton = Button(self, bg="#fffff0",fg='#f3bb1d',activebackground='#f3bb1d',activeforeground='#fffff0', bd = 12, 
            text = "pow",
            command = lambda : self.buttonClick("pow(,)"), font = ("Helvetica", 20, "bold"))
            self.Subbutton.grid(row = 3, column = 3, sticky = W+E)

            # π/pi button
            self.Multbutton = Button(self, bg="#fffff0",fg='#f3bb1d',activebackground='#f3bb1d',activeforeground='#fffff0',bd = 12, text = "π",
            command = lambda : self.buttonClick("pi"), font = ("Helvetica", 20, "bold"))
            self.Multbutton.grid(row = 4, column = 3, sticky = W+E)

            # conv_degrees button
            self.Divbutton = Button(self, bg="#ffffff",fg='#800000',activebackground='#800000',activeforeground='#ffffff',bd=7, text = "\u00b0",
            command = lambda : self.buttonClick("degrees()"), font = ("Helvetica", 20, "bold"))
            self.Divbutton.grid(row = 5, column = 3, sticky = W)
            
            # conv_radians button
            self.Divbutton = Button(self, bg="#ffffff",fg='#800000',activebackground='#800000',activeforeground='#ffffff',bd=7,text = "c",
            command = lambda : self.buttonClick("radians()"), font = ("Helvetica", 20, "bold"))
            self.Divbutton.grid(row = 5, column = 3, sticky = E)

            # Equal button
            self.Equalbutton = Button(self,bg="#18e111",fg='#fffff0',activebackground='#fffff0',activeforeground='#18e111', bd = 12, text = "=",
            command = self.CalculateTask, font = ("Helvetica", 20, "bold"),width=14, padx=7)
            self.Equalbutton.grid(row = 1,sticky = E, columnspan = 4)

            # Clear Button
            self.Clearbutton = Button(self,bg="#18e111",fg='#fffff0',activebackground='#fffff0',activeforeground='#18e111', bd = 12,text = "AC",  
            font = ("Helvetica", 20, "bold"), width = 12, padx = 7,cursor='pencil', command = self.ClearDisplay)
            self.Clearbutton.grid(row = 1, columnspan = 4, sticky = W)
            
            # Input ..
            self.user_input=Entry(cursor='pencil',bg='#fffff0',fg="#18e111",bd=12, insertwidth=4,font=("Verdana", 
            20,"italic"),textvariable=self.UserIn,justify=RIGHT)    
            self.user_input.grid(row=6, sticky=E+W)
            self.user_input.insert(0, "Input...")
            
            # Help button
            #self.help = Button(self, text="\u23ff", command=self.show_help)
            #self.help.grid(row=5,column=0, sticky=W+S)
        def show_help():
            self.show = open('help.txt', 'r')
            print(show)   
        def buttonClick(self, string_input):     # @@@@@@@@@@@@@@@@@@@@@@@@
            self.temp = str(string_input)
            self.task = str(self.task) + str(string_input)
            self.UserIn.set(self.temp+self.task)
            
        def CalculateTask(self):
            self.data = self.user_input.get()
            try:
                self.answer = eval(self.data)
                self.displayText(self.answer)
                self.task = self.answer

            except SyntaxError as e:
                self.displayText("Invalid Syntax!")
                self.task = ""

        def displayText(self, value):
            self.user_input.delete(0, END)
            self.user_input.insert(0, value)

        def ClearDisplay(self):
            self.task = ""
            self.user_input.delete(0, END)
            self.user_input.insert(0, "Input ...")


    calculator = Tk()
    calculator.title("PyCal")
    calculator.config(background='green')
    app = Application(calculator)
    calculator.resizable(width = False, height = False) # Make window fixed (cannot be resized)
    

    calculator.mainloop()    
   
else:  # user choose Cancel
    sys.exit(0)

#### Background_Image ####

