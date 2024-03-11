import tkinter as tk
from tkinter import filedialog as fd

#files type
filetypes = (
        ("text files" ,"*.txt"),
        ("all files" ,"*.*")
    )

#Open file button function
def open_function():
    #show open file dialog
    f = fd.askopenfile(filetypes = filetypes)
    if not f:
        return
    #read text file and show it's contents
    text_box.delete(0.0,tk.END)
    text_box.insert(tk.END ,f.read())
    window.title(f"Beta Text Editor__Dark theme - {f.name}")

#save button function
def save_function():
    #show save file dialog
    f = fd.asksaveasfile(initialfile = "Untitled.txt",
                         defaultextension = ".text",
                         filetypes = filetypes
                         )
    if not f:
        return
    #getting text written in text box
    content = text_box.get("1.0", "end-1c")
    #writing content of text box to file
    if f is not None:
        f.write(content)
        f.close()

#Creating the window of text editor
window = tk.Tk()

#Editing window
window.title(f"Beta Text Editor__Dark theme .^_^.")
window.columnconfigure(1 ,minsize = 800)
window.rowconfigure(0 ,minsize = 600)
window.configure(bg = "#1b1b1b")

#Creating text box and Frame to buttons
text_box = tk.Text(window ,bg = "#2d2d2d" ,fg = "#f3f6f4" ,font = "regular")
btns_frame = tk.Frame(window ,relief = tk.RAISED ,bg = "#1b1b1b")

#Creating buttons
btn_open = tk.Button( btns_frame ,
                      text = "Open File",
                      command = open_function,
                      fg = "#999999" ,
                      bg = "#353535"
                    )
btn_save = tk.Button( btns_frame ,
                      text = "Save As"
                      ,command = lambda:save_function()
                      ,fg = "#999999" ,
                      bg = "#353535"
                    )

#Positioning
text_box.grid(column = 1 ,row = 0 ,sticky = "nsew")
btns_frame.grid(column = 0 ,row = 0 ,sticky = "nw")
btn_open.grid(row = 0, column = 0 ,padx = 2 ,pady = 3 ,sticky = "ew")
btn_save.grid(row = 1, column = 0 ,padx = 2 ,pady = 9 ,sticky = "ew")


window.mainloop()