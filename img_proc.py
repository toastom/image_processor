from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox, tkSimpleDialog
from PIL import Image
from PIL import ImageFilter


class App:
    def __init__(self, master):
        self.frame = Frame(master, width=500, height=20)
        self.frame.pack()

        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack(side=BOTTOM)
        

        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)

        self.sub_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Edit Image", menu=self.sub_menu)
        self.sub_menu.add_command(label="Convert to Black/White", command=self.convert_b_w)

        self.sub_menu.add_command(label="Rotate Image", command=self.rotate_image)

        #self.toolbar = Frame(master)
        #self.toolbar.pack(side=TOP)

    def convert_b_w(self):
        #File dialog to let the user choose which image they want
        self.filename = tkFileDialog.askopenfilename(initialdir="C:\Python\my_scripts",
                                                     title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        
        self.image = Image.open(self.filename) #Opens image the user chose
        self.image.convert(mode='L').save(self.filename) #Converts the image and saves

        tkMessageBox.showinfo("Saved", "Image saved") #Dialog to show we saved


    def rotate_image(self):
        #File choosing dialog
        self.filename = tkFileDialog.askopenfilename(initialdir="C:\Python\my_scripts",
                                                     title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        self.image = Image.open(self.filename) #Opens image

        self.rotation_value = tkSimpleDialog.askinteger("Rotate", "Rotate Degrees Clockwise",
                                minvalue=0, maxvalue=360)
        #Default with Tk is to rotate counter-clockwise, so we have to make it negative
        #to flip clockwise
        self.image.rotate(self.rotation_value * -1).save(self.filename)

        tkMessageBox.showinfo("Saved", "Image saved") #User feedback for saving image

        
       
root = Tk()
app = App(root)
root.title("Image Manipulator")
root.mainloop()
