import tkinter as tk
from tkinter import *
import tkinter as ttk
from tkinter.messagebox import showinfo

#I decided for the design typing would be better.

#Below are commented out OOP refactoring

'''
class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title('Paint Calculator')
		self.resizable(False, False)
		#self.geometry('400x300')

class Find_Volume:
	@staticmethod
	def return_volume(walls_width, walls_length, walls_depth):
   		#self.volume_val = ((float(self.walls_width.get())) * (float(self.walls_length.get())) * (float(self.walls_depth.get())))
   		vol_val = ((float(walls_width)) * (float(walls_length)) * (float(walls_depth)))
'''
class Paint_calculator(tk.Tk):
	def __init__(self):
		super().__init__()

		#These are my buttons

		self.get_area = ttk.Button(self, text = "area =", padx=40, pady=20, command= self.return_area)
		self.paint_req = ttk.Button(self, text = "paint ml/m2' =", padx=40, pady=20,command= self.return_paint)
		self.get_vol = ttk.Button(self, text = "volume=", padx=40, pady=20, command= self.return_volume)
		
		#These are my button locations

		self.get_area.grid(row = 7, column = 0, columnspan = 1)
		self.paint_req.grid(row = 7, column = 1, columnspan = 1)
		self.get_vol.grid(row = 7, column = 2, columnspan = 1)

		#stringvars allow me to convert vars to floats
		self.walls_length = tk.StringVar()
		self.walls_depth = tk.StringVar()
		self.walls_width = tk.StringVar()
		
		self.perimeter = tk.StringVar()
		self.perimeter_val = tk.StringVar()
		self.area = tk.StringVar()
		self.volume = tk.StringVar()
		
		self.area_val = tk.StringVar()
		self.volume_val = tk.StringVar()
		self.paint_val = tk.StringVar()
		self.paint_req = tk.StringVar()


		#labels and entry fields below
		self.area_label= Label(self, text="Area of floor(metres)")
		
		self.area_val= Entry(self, textvariable=self.area, width=35, borderwidth= 5) #area of floor
		self.perimeter_label= Label(self, text="Perimeter")
		self.perimeter= Entry(self, textvariable=self.perimeter, width=10, borderwidth= 5)
		
		self.paint_req_label= Label(self, text="Paint required ml/m^2")
		self.paint_req = Entry(self, textvariable=self.paint_req, width=35, borderwidth=5)

		self.vol_room_label= Label(self, text="Total volume of room (metres)")
		self.vol_room = Entry(self,textvariable=self.volume, width=35, borderwidth=5)

		self.length_label = Label(self, text="length wall")
		self.walls_length = Entry(self,textvariable=self.walls_length,width=10, borderwidth = 5)

		self.width_label = Label(self, text="width of wall")
		self.walls_width = Entry(self,textvariable=self.walls_width,width=10, borderwidth = 5)

		self.depth_label = Label(self, text="depth of wall")
		self.walls_depth = Entry(self,textvariable=self.walls_depth,width=10, borderwidth = 5)

		self.area_label.grid(row=0, column=0)
		self.area_val.grid(row = 0, column = 1, columnspan = 5, padx=10, pady=10) #area of floor

		self.paint_req_label.grid(row=1, column=0)
		self.paint_req.grid(row = 1, column = 1, columnspan = 5, padx=10, pady=10)

		self.vol_room_label.grid(row=2, column=0)
		self.vol_room.grid(row = 2, column = 1, columnspan = 5, padx=10, pady=10)
		#length*width*depth

		self.width_label.grid(row= 3, column= 0)
		self.walls_width.grid(row = 3, column = 1)

		self.length_label.grid(row= 4,column= 0)
		self.walls_length.grid(row= 4, column= 1)

		self.depth_label.grid(row= 3, column = 2)
		self.walls_depth.grid(row= 3, column = 3)

		self.perimeter_label.grid(row= 4, column=2)
		self.perimeter.grid(row=4, column=3)

		#my methods
#this button function below did work but I broke it and ran out of time.

#when paint ml/m^2 button is clicked do:		
	def return_area(self):
		self.area_val.delete(0, END)#clears previous values for user friendiness.
		self.perimeter.delete(0, END) #as coding in a rush some of variable names got switched about. Would definitely keep the naming convention in check
		self.perimeter_val = ((float(self.walls_width.get())) + (float(self.walls_length.get()))) * 2 #thought it would make sense to get the perimter if we are getting the area.
		self.perimeter.insert(0,float(self.perimeter_val)) 
		
		self.area = ((float(self.walls_width.get())) * (float(self.walls_length.get())))

		self.area_val.insert(0,float(self.area))

#when volume = button is clicked do:

	def return_volume(self):

		self.vol_room.delete(0, END)#clears previous values for user friendiness.
		self.volume_val = ((float(self.walls_width.get())) * (float(self.walls_length.get())) * (float(self.walls_depth.get()))) *1
		
		self.vol_room.insert(0,float(self.volume_val))

#when paint ml/m^2 button is clicked do:

	def return_paint(self):
		self.paint_req.delete(0, END) #clears previous values for user friendiness.
		self.paint_val = ((float(self.walls_width.get())) * (float(self.walls_length.get()))) * 10
		
		self.paint_req.insert(0,float(self.paint_val))


#more oop refactoring below was going to try use the volume class as demo.

'''
def return_volume(self):
		"""  Handle button click event
		"""
		try:
			walls_width = float((self.walls_width.get()))
			walls_length = float((self.walls_length.get()))
			walls_depth = float((self.walls_depth.get()))
			#vol_val = Find_Volume.return_volume(float(w),float(l),float(d))
			#result = '{width} Volume = 
			#result = Find_Volume.return_volume(self.volume_val)
			#Find_Volume.return_volume(self.walls_width,self.walls_length,self.walls_depth)

			self.vol_room.insert(0,float(Find_Volume.return_volume(walls_width,walls_length,walls_depth)))
			#self.result_label.config(text=result)
		except ValueError as error:
			showerror(title='Error', message=error)
'''

#self.mainloop()
if __name__ == "__main__":
	#ConverterFrame(app)
	app = Paint_calculator()
	app.mainloop()