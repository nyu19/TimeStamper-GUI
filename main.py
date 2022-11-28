import customtkinter as ctk
from tkinter import filedialog,messagebox
import os
import utils.TimeStamper as tsp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Timestamper")
app.geometry("400x240")
app.resizable(height=False,width=False)

class StampingFlow():
    def __init__(self) -> None:
        pass
    inpfolder = None
    outfolder = None

    def inp_button_called(self):
        self.inpfolder = filedialog.askdirectory(title="Select Folder of Imput images")    

    def out_button_called(self):
        self.outfolder = filedialog.askdirectory(title="Select Folder for Output")
        
    def stamp(self):
        if self.inpfolder == None or self.outfolder == None:
            messagebox.showerror("Missing Folder","No folder was selected either for input or output.")
            return

        x = tsp.placeTimeStamp(self.inpfolder,self.outfolder)
        self.inpfolder = None
        self.outfolder = None
        if x[1] == 0:
            messagebox.showinfo("Info",f"Done! TimeStamp has been Applied to {x[0]} photo(s).")
        else:
            messagebox.showerror("Info",f"Done! TimeStamp has been Applied to {x[0]} photo(s). With {x[1]} with orientation Errors")


    # print("Button Pressed!")

flow = StampingFlow()

inpButton = ctk.CTkButton(master=app,text="Select Input Folder",command=flow.inp_button_called)
inpButton.place(relx=0.5,rely=0.25,anchor=ctk.CENTER)

outButton = ctk.CTkButton(master=app,text="Select Output Folder",command=flow.out_button_called)
outButton.place(relx=0.5,rely=0.4,anchor=ctk.CENTER)

submitBtn = ctk.CTkButton(master=app,text="Start Stamping",command=flow.stamp,fg_color="green")
submitBtn.place(relx=0.5,rely=0.75,anchor=ctk.CENTER)

authorLabel = ctk.CTkLabel(master=app,text="TimeStamper by Nakul Upasani",text_color=("#c9c2c1","#383837"))
authorLabel.place(relx=0.75,rely=0.9,anchor=ctk.CENTER)

app.mainloop()


#* pyinstaller --noconfirm --onedir --windowed --add-data "C:\Users\nakul\AppData\Local\Programs\Python\Python38\Lib\site-packages\customtkinter;customtkinter\" "C:\MY DATA\Projects\Intermediate\TimeStamper-GUI\main.py"
#* pyinstaller --noconfirm --onefile --windowed --add-data "C:\Users\nakul\AppData\Local\Programs\Python\Python38\Lib\site-packages\customtkinter;customtkinter\" "C:\MY DATA\Projects\Intermediate\TimeStamper-GUI\main.py"