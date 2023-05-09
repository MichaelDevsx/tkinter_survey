# program to do survey of bananas
import tkinter as tk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        #Creating title for the program
        self.title("Bananas Survey")
        self.geometry("640x480+300+300")
        self.resizable(False, False)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(99, weight=2)
        self.rowconfigure(100, weight=1)

        self.color_choices = ("Any","Green","Red","Green-Yellow","Red-Yellow","Blue","Bronw-Spotted","Black")


        self.name_var = tk.StringVar()

        self.eater_var = tk.BooleanVar()

        self.num_var = tk.IntVar(value=3)

        self.color_var = tk.StringVar(value="Any")

        self.plantain_var = tk.BooleanVar()

        self.output_var = tk.StringVar(value=" ")




        title = tk.Label(
            self,
            text="Please take the survey",
            font=("Arial 16 bold"),
            bg="brown",
            fg="#FF0"
        )
        name_label = tk.Label(
            self,
            text="What is your name?",
        )
        name_inp = tk.Entry(
            self,
            textvariable= self.name_var
        )
        eater_inp = tk.Checkbutton(
            self,
            text="Check this box if you eat bananas",
            variable=self.eater_var
        )
        num_label = tk.Label(
            self,
            text="How many bananas do you eat per day?"
        )
        num_inp = tk.Spinbox(
            self,
            from_=0,
            to=1000,
            increment=1,
            textvariable=self.num_var
        )
        color_label = tk.Label(
            self,
            text="What is the best color for a banana"
        )
        color_inp = tk.OptionMenu(
            self,
            self.color_var,
            *self.color_choices
        )
        
        plantain_label = tk.Label(
            self,
            text="Do you eat plantains?"
        )
        plantain_frame = tk.Frame(self)
        plantain_yes_inp = tk.Radiobutton(
            plantain_frame,
            text="Yes",
            value=True,
            variable=self.plantain_var
        )
        plantain_no_inp = tk.Radiobutton(
            plantain_frame,
            text="Ewww, no!",
            value=False,
            variable=self.plantain_var
        )
        banana_haiku_label = tk.Label(
            self,
            text="Write a haiku about bananas"
        )
        self.banana_haiku_inp = tk.Text(
            self,
            height=3
        )
        submit_btn = tk.Button(
            self,
            text="Submit Survey",
            command=self.on_submit
        )
        output_line = tk.Label(
            self,
            textvariable=self.output_var,
            anchor="w",
            justify="left"
        )
        title.grid(columnspan=2)
        name_label.grid(row=1, column=0)
        name_inp.grid(row=1, column=1)
        eater_inp.grid(row=2, columnspan=2, sticky="we")
        num_label.grid(row=3, column=0, sticky="we")
        num_inp.grid(row=3, column=1, sticky="we", padx=5)
        color_label.grid(row=4, columnspan=2, sticky="w", pady=10)
        color_inp.grid(row=5, columnspan=2, sticky="we", padx=25)
        plantain_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
        plantain_no_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
        plantain_label.grid(row=6, columnspan=2, sticky="w")
        plantain_frame.grid(row=7, columnspan=2, sticky="w")
        banana_haiku_label.grid(row=8, sticky="w")
        self.banana_haiku_inp.grid(row=9, columnspan=2, sticky="nsew")
        submit_btn.grid(row=99)
        output_line.grid(row=100, columnspan=2, sticky="nsew")

    def on_submit(self):
        name = self.name_var.get()
        number = self.num_var.get()
        color = self.color_var.get()
        banana_eater = self.eater_var.get()
        plantain_eater = self.plantain_var.get()
        haiku = self.banana_haiku_inp.get("1.0", tk.END)
        message = (f"Thanks for taking the survey {name}\n")
        if not banana_eater:
            message += "Sorry you dont like bananas"
        else:
            message += f"Enjoy your {number} {color} bananas!\n"
        if plantain_eater:
            message +="Enjoy your Plantains!"
        else:
            message += "May you successfully avoid plantains!"
        if haiku.strip():
            message += f"\n\n Your Haiku: \n {haiku}"
        self.output_var.set(message)



root = Root()
root.mainloop()