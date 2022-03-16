import tkinter
import tkinter.messagebox

class TestAvg:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title('Student Test Average')

        #frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #label
        self.label1 = tkinter.Label(self.top_frame,text = 'Enter the score for test 1:')
        self.label2 = tkinter.Label(self.mid_frame,text = 'Enter the score for test 2:')
        self.label3 = tkinter.Label(self.bottom_frame,text = 'Enter the score for test 3:')

        #entry
        self.label1_entry = tkinter.Entry(self.top_frame,width=10)
        self.label2_entry = tkinter.Entry(self.mid_frame,width=10)
        self.label3_entry = tkinter.Entry(self.bottom_frame,width=10)

        #pack
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.label1_entry.pack(side = 'left')
        self.label2_entry.pack(side = 'left')
        self.label3_entry.pack(side = 'left')

        

        self.calcbutton = tkinter.Button(self.main_window, text = 'Average', command = self.average)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.calcbutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        tkinter.mainloop()

    def average(self):
        test1 = float(self.label1_entry.get())
        test2 = float(self.label2_entry.get())
        test3 = float(self.label3_entry.get())

        avg = round(((test1+test2+test3)/3),2)

        tkinter.messagebox.showinfo('Average:', str(avg))

test_avg = TestAvg()