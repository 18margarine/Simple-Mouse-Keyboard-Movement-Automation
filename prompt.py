from tkinter import *
from tkinter import ttk, filedialog
import os
# Default path will be where the script is located
base_path = os.path.dirname(os.path.abspath(__file__))

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("File Name")
        # Prompt window will be displayed at the center of screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 320
        window_height = 100
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        self.attributes("-topmost", True)
        self.content = ttk.Frame(self, padding=(12, 20, 12, 20))
        self.file_name = StringVar()
        self.stored_file_name = None
        self.label = ttk.Label(self.content, text="File Name")
        self.inst = ttk.Label(self.content, text="Please enter file name for the generated csv file.", justify='right')
        self.name_entry = ttk.Entry(self.content, width=20, textvariable=self.file_name)
        self.ok_button = ttk.Button(self.content, text="Okay", command=self.confirm_close)

        self.content.grid(column=0, row=0)
        self.inst.grid(column=0, row=1, columnspan=3, pady=5)
        self.label.grid(column=0, row=2, padx=5)
        self.name_entry.grid(column=1, row=2, padx=5)
        self.ok_button.grid(column=2, row=2, padx=5)

    def confirm_close(self):
        self.stored_file_name = self.file_name.get()
        self.destroy()

class FileBrowse(Tk):
    def __init__(self):
        super().__init__()
        # Prompt window will be displayed at the center of screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 200
        window_height = 130
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.title("File Browser")
        self.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        self.content = ttk.Frame(self, padding=(12, 20, 12, 20))
        self.file_path = ttk.Label(self.content, text="Select generated csv", wraplength=250)
        self.browse_button = ttk.Button(self.content, text="Browse Files", command=self.browse_files)
        self.content.pack()
        self.file_path.pack(pady=5)
        self.browse_button.pack()
        self.filename = None


    def browse_files(self):
        self.filename = filedialog.askopenfilename(
            initialdir=base_path,
            title="Select a file",
            filetypes=(("CSV file", "*.csv"), ("All files", "*.*"))
        )
        if self.filename:
            self.destroy()

