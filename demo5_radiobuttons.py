import tkinter
import tkinter.messagebox


class MYGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')
        
        self.radio_var = tkinter.IntVar()

        

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Option 1', variable=self.radio_var,value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='Option 2', variable=self.radio_var,value=20)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text='Option 3', variable=self.radio_var,value=30)

        #set the idefault button selected
        self.rb2.select()
        
        #pack the Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #create the buttons
        self.okaybutton = tkinter.Button(self.bottom_frame, text = 'Okay', command = self.show_choice)
        self.resetbutton = tkinter.Button(self.bottom_frame, text = 'Reset', command = self.rb1.select)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        #pack the buttons
        self.okaybutton.pack(side = 'left')
        self.resetbutton.pack(side ='left')
        self.quit_button.pack(side = 'right')


        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option '+ str(self.radio_var.get()))
             

my_GUI = MYGUI()
