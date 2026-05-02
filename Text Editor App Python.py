import tkinter as tk
from tkinter import filedialog,messagebox
#===Window Setup==
root = tk.Tk()
root.title("Text Editor App")
root.geometry("600x400")
#===Text Area===
text_area=tk.Text(root,undo=True,font=("Arial",12,))
text_area.pack(fill=tk.BOTH,expand=True)
#===Global Variable===
current_file=None
#===Functions===
def new_file():
    global current_file
    text_area.delete(1.0,tk.END)
    current_file=None
    root.title("Text Editor App - New File")
def open_file():
    global current_file
    file_path=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        try:
            with open(file_path,"r") as file:
                content=file.read()
            text_area.delete(1.0,tk.END)
            text_area.insert(tk.END,content)
            current_file=file_path
            root.title(f"Text Editor App - {file_path}")
        except Exception as e:
            messagebox.showerror("Error",f"file open ni hui: {e}")
def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file,"w") as file:
                file.write(text_area.get(1.0,tk.END))
            messagebox.showinfo("info","file save  hogai")
        except Exception as e:
            messagebox.showerror("Error",f"file save ni hui: {e}")
    else:
        save_as_file()
def save_as_file():
    global current_file
    file_path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        try:
            with open(file_path,"w") as file:
                file.write(text_area.get(1.0,tk.END))
                current_file=file_path
                root.title(f"Text Editor App - {file_path}")
            messagebox.showinfo("info","file save  hogai")
        except Exception as e:
            messagebox.showerror("Error",f"file save ni hui: {e}")
def exit_app():
     if messagebox.askokcancel("Exit","Kia ap exit krna chahtay ho?"):
         root.destroy()
#===Clipboard Functions===
def cut_text():
    text_area.event_generate("<<Cut>>")
def paste_text():
    text_area.event_generate("<<Paste>>")
def copy_text():
    text_area.event_generate("<<Copy>>")
#===Menu Bar===
menu_bar = tk.Menu(root)
#===File Menu===
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As.",command=save_as_file)
file_menu.add_command(label="Exit",command=exit_app)
menu_bar.add_cascade(label="File",menu=file_menu)
#===Edit Menu===
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut",command=cut_text)
edit_menu.add_command(label="Paste",command=paste_text)
edit_menu.add_command(label="Copy",command=copy_text)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
root.config(menu=menu_bar)
root.mainloop()





