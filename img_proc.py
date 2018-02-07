from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox, tkSimpleDialog
from PIL import Image
from PIL import ImageFilter


#So it turns out I do need a new class...

class Window:
    def __init__(self):
        self.win = Tk()
        

class App(Window):
    def __init__(self, master):
        self.frame = Frame(master, width=500, height=20)
        self.frame.pack()

        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack(side=BOTTOM)

        #self.butt = Button(master, text="Window", command=Toplevel(master))
        #self.butt.pack()

        #self.new_filter = StringVar(master)
        #self.new_filter.set("Brighten") #Default value
        #self.options = OptionMenu(master, self.new_filter, "Brighten", "Darken")
        #self.options.pack(side=LEFT)

        #self.butt = Button(master, text="Apply Filter", command=self.apply_filter(self.new_filter))
        #self.butt.pack(side=LEFT)

        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)

        self.edit_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Edit Image", menu=self.edit_menu)
        
        self.edit_menu.add_command(label="Convert to Black/White", command=self.convert_b_w)
        self.edit_menu.add_command(label="Rotate Image", command=self.rotate_image)
        #self.edit_menu.add_command(label="Choose Filter", command=self.create_window(master))

        self.size_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Image Size", menu=self.size_menu)
        
        self.size_menu.add_command(label="Resize Image", command=self.resize_image)
        
        #self.toolbar = Frame(master)
        #self.toolbar.pack(side=TOP)

    def convert_b_w(self):
        #File dialog to let the user choose which image they want
        self.filename = tkFileDialog.askopenfilename(title="Select Image",
                                                     filetypes=(("jpeg files", "*.jpg"),
                                                                ("all files", "*.*")))
        
        self.image = Image.open(self.filename) #Opens image the user chose
        #self.conv_image = self.image.convert(mode='L') #Converts the image

        
        #Change filename to SaveAs instead of Open
        '''
        self.filename = tkFileDialog.asksaveasfilename(title="Save as",
                                                           filetypes=(("jpeg files", "*.jpg"),
                                                                      ("all files", "*.*")))
        '''
        
        self.image.convert(mode='L').save(self.filename) #Converts the image and saves

        tkMessageBox.showinfo("Saved", "Image saved") #Dialog to show we saved


    def rotate_image(self):
        #File choosing dialog
        self.filename = tkFileDialog.askopenfilename(title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        self.image = Image.open(self.filename) #Opens image

        self.rotation_value = tkSimpleDialog.askinteger("Rotate", "Rotate Degrees Clockwise",
                                minvalue=0, maxvalue=360)

        #Change filename to SaveAs instead of Open
        '''
        self.filename = tkFileDialog.asksaveasfilename(title="Save as",
                                                           filetypes=(("jpeg files", "*.jpg"),
                                                                      ("all files", "*.*")))
        '''
        
        #Default with Tk is to rotate counter-clockwise, so we have to make it negative
        #to flip clockwise
        self.image.rotate(self.rotation_value * -1).save(self.filename)

        tkMessageBox.showinfo("Saved", "Image saved") #User feedback for saving image

    def resize_image(self):
        #File choosing dialog
        self.filename = tkFileDialog.askopenfilename(title="Select Image",
                                                     filetypes=(("jpeg files", "*jpg"),
                                                                ("all files", "*.*")))
        self.image = Image.open(self.filename) #Opens image

        self.width_value = tkSimpleDialog.askinteger("Resize Width", "New Width Value",
                             minvalue=16, maxvalue=1280)
        
        self.height_value = tkSimpleDialog.askinteger("Resize Width", "New Height Value",
                             minvalue=16, maxvalue=1280)

        #Change filename to SaveAs instead of Open
        '''
        self.filename = tkFileDialog.asksaveasfilename(title="Save as",
                                                       filetypes=(("jpeg files", "*.jpg"),
                                                                  ("all files", "*.*")))
        '''
        #Resize
        self.new_image = self.image.resize((self.width_value, self.height_value))
        self.new_image.save(self.filename)
        
        tkMessageBox.showinfo("Saved", "Image saved") #User feedback for saving

    

       
root = Tk()
app = App(root)
root.title("Image Manipulator")
root.mainloop()
