from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from PIL import Image
from PIL import ImageFilter


class App:
    def __init__(self, master):
        self.frame = Frame()
        self.frame.pack()

        #self.photo_label = Label(master, image=self.image)
        #self.photo_label.pack(side=TOP)

        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)

        self.sub_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.sub_menu)
        self.sub_menu.add_command(label="Add Image", command=self.add_image)

        self.toolbar = Frame(master)
        self.convert = Button(self.toolbar, text="Convert to Black/White", command=self.convert_b_w)
        self.convert.pack(side=LEFT)

        #self.preview = Button(self.toolbar, text="Image Preview", command=)

        self.toolbar.pack(side=TOP)

    def add_image(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="C:\Python\my_scripts",
                                                     title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        self.image = Image.open(self.filename)
        
        
        print("Added {} image".format(self.filename))

    def convert_b_w(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="C:\Python\my_scripts",
                                                     title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        
        self.image = Image.open(self.filename)
        self.image.convert(mode='L')
        print("Converted to Black and White")

root = Tk()

app = App(root)

root.mainloop()
