"""PyNumGenerator is application to generate sequential and random numbers of various bases like binary,octal,hex etc.
It can generate numbers with immense speed and has support for 64-bits,128-bits,256-bits and for higher bits aswell for big data aswell.

Features.
1.Generate bases are : BINARY,DECIMAL,OCTAL,HEXA-DECIMAL,EXPONENT,FLOAT.
2.Sequential and random modes.
3.Support for 64-bits,128-bits,256-bits and for higher bits aswell
4.Support big data aswell like big hex,big binary,big octal etc.
5.No external dependencies with any modules other than pythons internal modules.

PyNumGenerator : V 1.0
Dated 19-05-2019
written by Haseeb mir (haseebmir.hm@gmail.com)  
"""

from tkinter import *
from tkinter import messagebox
import random

SEQ_GEN = "seq_gen"
RAND_GEN = "rand_gen"
NUM_BITS = 64

#BaseList
BIN,DEC,OCT,HEX,EXP,FLT = 'b','d','o','x','e','f'

fields = ("Start range","End range","Number Bits","Generator")
#Color constants
APP_FG = "aquamarine1"
APP_BG =  "aquamarine3"
APP_UI = "green3"

#Main method to generate numbers for any base.
def py_num_generator(entries,num_base):
    generator_list = []
    file_name = ""
    
    if num_base == BIN: file_name += "binary_"
    elif num_base == DEC: file_name += "decimal_"
    elif num_base == OCT: file_name += "octal_"
    elif num_base == HEX: file_name += "hex_"        
    elif num_base == FLT: file_name += "float_"
    elif num_base == EXP: file_name += "exponent_"

    input_list = list(range(3))

    for index in range(3):
        input_list[index] = entries[fields[index]].get()

    start_range,end_range,num_bits = input_list[0],input_list[1],input_list[2]

    if not start_range or not end_range or not num_bits:
        messagebox.showinfo("ERROR","Input fields are empty")

    gen_type = ""    
    if check_var_seq.get():
        gen_type = SEQ_GEN
    elif check_var_rand.get():
        gen_type = RAND_GEN    

    try:    
        file_name += gen_type + "_" + num_bits + "_bits" + ".txt"
        
        #Error checking for range.
        start_range,end_range,num_bits = int(start_range),int(end_range),int(num_bits)
        if start_range < 0 or end_range <= start_range:
            messagebox.showinfo("ERROR","Invalid range provided") 

        else:   
            #Generate numbers in specified base. 
            if gen_type == SEQ_GEN: 
                for index in range(start_range,end_range+1):
                    generator_list.append(format(index,num_base))
            elif gen_type == RAND_GEN:
                for index in range(start_range,end_range):
                    rand_num = random.randint(1,2**num_bits)
                    generator_list.append(format(rand_num,num_base).upper())
            else:
                messagebox.showinfo("ERROR","Please select generator type") 
    
        if generator_list:
            write_file(file_name,generator_list)
            messagebox.showinfo("INFO","File generated in : " + file_name)
    except Exception as ex:
        messagebox.showinfo("ERROR",ex)  

#Method to generate binary numbers.
def generate_binary(entries):
    py_num_generator(entries,BIN)

#Method to generate decimal numbers.    
def generate_decimal(entries):
    py_num_generator(entries,DEC)

#Method to generate octal numbers. 
def generate_octal(entries):
    py_num_generator(entries,OCT)

#Method to generate hexa-decimal numbers. 
def generate_hex(entries):
    py_num_generator(entries,HEX)

#Method to generate floating numbers. 
def generate_float(entries):
    py_num_generator(entries,FLT)

#Method to generate exponent numbers. 
def generate_exponent(entries):
    py_num_generator(entries,EXP)                

#Method to write data to file.
def write_file(filename,data_list):
    with open(filename,"w") as fp:
        for data in data_list:
            fp.write(data)
            fp.write("\n")
        fp.close()    

#Clear all the entries of form.
def clear_entry(entries):
    for field in fields:
        entries[field].delete(0, "end")

#Method to make form UI fields on screen.
def make_form(root, fields):
   entries = {}
   bg = APP_BG
   for index in range(len(fields)):  
      row = Frame(root)
      ent = Entry(row)
      lab = Label(row,width=10, text=fields[index], anchor="w",background = bg)      
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[fields[index]] = ent
   return entries

#Main method to initialize and render interface items on screen.
if __name__ == "__main__":
   try:     
        root = Tk()
        root.title("PyNumGenerator V 1.0")
        root.configure(background=APP_BG)
        root.resizable(False, False)
        ents = make_form(root, fields)
        root.bind("<Return>", (lambda event, e = ents: fetch(e)))

        #Render all buttons.
        bin_btn = Button(root, text = "Binary",fg = APP_UI,command=(lambda e = ents: generate_binary(e)))
        bin_btn.pack(side = LEFT, padx = 5, pady = 5)
        
        dec_btn = Button(root, text = "Decimal",fg = APP_UI,command=(lambda e = ents: generate_decimal(e)))
        dec_btn.pack(side = LEFT, padx = 5, pady = 5)

        oct_btn = Button(root, text="Octal",fg = APP_UI,command=(lambda e = ents: generate_octal(e)))
        oct_btn.pack(side = LEFT, padx = 5, pady = 5)
        
        hex_btn = Button(root, text="Hex",fg = APP_UI,command=(lambda e = ents: generate_hex(e)))
        hex_btn.pack(side = LEFT, padx = 5, pady = 5)

        float_btn = Button(root, text="Float",fg = APP_UI,command=(lambda e = ents: generate_float(e)))
        float_btn.pack(side = LEFT, padx = 5, pady = 5)

        exp_btn = Button(root, text="Exp",fg = APP_UI,command=(lambda e = ents: generate_exponent(e)))
        exp_btn.pack(side = LEFT, padx = 5, pady = 5)

        #Render checkbox.
        check_var_rand = IntVar()
        rand_cb = Checkbutton(root, text = "Random", variable = check_var_rand,onvalue = 1, offvalue = 0, height=1,width = 10)
        rand_cb.pack(side = RIGHT)
        rand_cb.place(relx=0.45, rely=0.73,anchor=CENTER)
        rand_cb.config(background = "aquamarine3",foreground = "black")


        check_var_seq = IntVar()
        seq_cb = Checkbutton(root, text = "Sequential", variable = check_var_seq,onvalue = 1, offvalue = 0, height=1,width = 13)
        seq_cb.pack(side = RIGHT)
        seq_cb.place(relx=0.78, rely=0.73,anchor=CENTER)
        seq_cb.config(background = "aquamarine3",foreground = "black")

        root.mainloop()

   except Exception as ex:
   		messagebox.showinfo("ERROR","Exception occured : " + ex) 



