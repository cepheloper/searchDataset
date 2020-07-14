import tkinter as tk 
from tkinter import messagebox
from scraper import displaySearch

class mainApp(tk.Frame):

    def __init__(self, master = None):
        if master is None: 
            self.master = tk.Tk()
        else: self.master = master  
        self.master.title("cepheloper dataset search")
        self.master.geometry("280x200")
        self.createWidgets()
        self.master.mainloop()
        
    def createWidgets(self):
        self.searchbar = tk.Entry(self.master)
        self.searchbar.grid(row=0, column=0, padx=1, pady=1,columnspan = 2)
        self.searchbtn = tk.Button(self.master, text="Search", command = self.commenceSearch)
        self.searchbtn.grid(row=0, column=2, sticky = "NSEW") 
        self.resetbtn = tk.Button(self.master, text="Clear", command = self.clearSearch)
        self.resetbtn.grid(row=0, column=3, sticky = "NSEW") 
        self.downloadbtn = tk.Button(self.master, text="Download", command = self.downloadResults)
        self.downloadbtn.grid(row=0, column=4, sticky = "NSEW")
        self.listbox = tk.Listbox(self.master)
        self.listbox.grid(row=1, column=0, columnspan=5, sticky = "NSEW")     

    def downloadResults(self):
        if self.listbox.curselection():
            downloadLink = self.listbox.get(self.listbox.curselection())
        else: messagebox.showerror(title = "Null Error",message = "Dataset not selected")

    def clearSearch(self):
        self.listbox.delete(0, tk.END)

    def commenceSearch(self): 
        keyword = "Covid"
        searchData = displaySearch(keyword)
        
        self.listbox.insert("end",*results) 
            

        

