import tkinter
from tkinter import *
from easygui import *
import tkinter.messagebox
from PIL import Image
import tkinter.font as tk_Font
import calculator_data
### Messages ### ||||||||||||||||||||||||||||||||||||||||||
dia_message = ''' PyCal is created to simplify the calculations, 
                        which normal calculators don't help with ...
                                                     


                                                             -SVNIT    '''
##### main window with permission of ccbox #### 

class Calculator_Core:
   def __init__(self):
       # Do this yourself
       pass

class Calculator(tk.Frame):

   def __init__(self, master):
       tk.Frame.__init__(self, master)
       self.master = master 
       self.calculator_buttons_texts = calculator_data.calculator_buttons_texts

       self.configure_gui() 
       self.create_calculator_widgets()      


   def configure_gui(self):
       self.master.title('Calculator')
       self.master.resizable(False, False)

   def create_calculator_widgets(self):
       self.create_calculator_input_field()
       self.create_calculator_buttons_texts()

   def create_calculator_buttons_texts(self):
       button_column = 0
       button_row = 1
       text_buttons = ('A', '789+', '456-', '123*', '0=/')
       for button_rows in text_buttons:
           for text_button in button_rows:               
               self.configure_and_place_button(text_button, button_row, button_column)
               button_column += 1
           button_row += 1
           button_column = 0

   def configure_and_place_button(self, text_button, button_row, button_column):
       key = list(self.calculator_buttons_texts.keys())[list(self.calculator_buttons_texts.values()).index(text_button)]
       self.calculator_buttons_texts[key] = tk.Button(self.master, text=text_button, bg="#5BC8AC", bd=12)
       self.calculator_buttons_texts[key].config(padx=33, pady=25, font=("Helvetica", 20, "bold"))
       self.calculator_buttons_texts[key].grid(row=button_row,column=button_column)
       self.reconfigure_specific_buttons(key, text_button)  


   def reconfigure_specific_buttons(self, key, text_button):
       self.reconfigure_clear_button(key, text_button)
       self.reconfigure_equals_button(key, text_button)     
       self.reconfigure_divide_button(key, text_button)


   def reconfigure_clear_button(self, key, text_button):
       if text_button == 'A':
           self.calculator_buttons_texts[key].config(bg='#E6D72A', text='AC')
           self.calculator_buttons_texts[key].grid(columnspan=4, sticky=tk.W+tk.E)

   def reconfigure_equals_button(self, key, text_button):
       if text_button == '=':
           self.calculator_buttons_texts[key].config(bg='#E6D72A')
           self.calculator_buttons_texts[key].grid(columnspan=2, sticky=tk.W+tk.E)

   def reconfigure_divide_button(self, key, text_button):
       if text_button == '/':
           self.calculator_buttons_texts[key].grid(column=3)  

   def create_calculator_input_field(self):
       self.user_input = tk.Entry(self.master, justify=tk.RIGHT, width=24, insertwidth=4, bd=29)
       self.user_input.grid(row=0, column=0, columnspan=4)
       self.user_input.configure(font = ("Verdana", 20, "bold"), bg="#5BC8AC")
       self.user_input.insert(0, "0")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


