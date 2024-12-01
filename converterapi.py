from currency_converter import CurrencyConverter
import tkinter as tk  
from tkinter import *
import tkinter.messagebox 

a=CurrencyConverter()


#Function To For Real Time Currency Conversion
 
def clicked():
 amount = float(Amount1_field.get())
 from_currency=Amount2_field.get()
 to_currency = Amount3_field.get()
 result=a.convert(amount,from_currency,to_currency)
 

 Amount4_field.delete(0, tk.END)  
 Amount4_field.insert(0, round(result, 2))
 



#GUI
window = tk.Tk()
 
window.title("Currency converter")
 
Tops = Frame(window, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency converter  ',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
 

 


     
#clearing all the data 
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
    Amount3_field.delete(0, tk.END)
    Amount4_field.delete(0, tk.END)

 #INTERFACE
window.configure(background='#e6e5e5')
window.geometry("800x600")
 
Label_1 = Label(window, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0,padx=50, sticky=W)
 
label3 = tk.Label(window, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label3.grid(row=3, column=0, padx=2, pady=2,ipadx=28,sticky=W)
tk.Entry(window)
 
label3 = tk.Label(window, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label3.grid(row=4, column=0,pady=2,  padx=2,ipadx=28,sticky=W)
tk.Entry(window)
 
Label_2 = Label(window, font=('lato black', 7, 'bold'), text="", padx=5, pady=2, bg="#e6e5e5", fg="black")
Label_2.grid(row=5, column=5, sticky=W)
 
Label_3 = Label(window, font=('lato black', 7, 'bold'), text="", padx=5, pady=2, bg="#e6e5e5", fg="black")
Label_3.grid(row=7, column=0, sticky=W)
 
label4 = tk.Label(window, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label4.grid(row=8, column=0, sticky=W ,ipadx=32)

#entry
Amount1_field = tk.Entry(window)
Amount1_field.grid(row=2, column=1, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(window)
Amount2_field.grid(row=3, column=1,ipadx=28, sticky=E)

Amount3_field = tk.Entry(window)
Amount3_field.grid(row=4, column=1 ,ipadx=28,sticky=E)

Amount4_field = tk.Entry(window)
Amount4_field.grid(row=8, column=1,ipadx=28, sticky=E)

#button
Label_6 = Button(window, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
             command=clicked  )
Label_6.grid(row=6, column=0)
 
Label_6 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_6.grid(row=9, column=0, sticky=W,ipadx=31)
 
Label_7 = Button(window, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_7.grid(row=10, column=0)

 
window.mainloop()