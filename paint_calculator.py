import tkinter as tk
from tkinter import *
import tkinter as ttk
from tkinter.messagebox import showinfo

global errInvOp
errInvOp = "Not a valid operator please choose from the buttons provided."

class Paint_calculator(tk.Tk):
	def __init__(self):
		super().__init__()

		#validation checker referenced for def validate
		# basically prevents the use of anything but numbers

		self.get_area = ttk.Button(self, text = "area =", padx=40, pady=20, command= self.return_area)
		self.get_paint_req = ttk.Button(self, text = "paint req' =", padx=40, pady=20, command=lambda: buttonClick(1))
		self.get_vol = ttk.Button(self, text = "volume=", padx=40, pady=20, command= self.return_volume)

		self.get_area.grid(row = 7, column = 0, columnspan = 1)
		self.get_paint_req.grid(row = 7, column = 1, columnspan = 1)
		self.get_vol.grid(row = 7, column = 2, columnspan = 1)

		self.walls_length = tk.StringVar()
		self.walls_depth = tk.StringVar()
		self.walls_width = tk.StringVar()
		
		#self.walls_length_west = tk.StringVar()

		#self.walls_width_north = tk.StringVar()
		#self.walls_width_east = tk.StringVar()
		#self.walls_width_south = tk.StringVar()
		#self.walls_width_west = tk.StringVar()
		self.perimeter = tk.StringVar()
		self.perimeter_val = tk.StringVar()
		self.area = tk.StringVar()
		self.volume = tk.StringVar()
		
		self.area_val = tk.StringVar()
		self.volume_val = tk.StringVar()


		self.area_label= Label(self, text="Area of floor(metres)")
		
		self.area_val= Entry(self, textvariable=self.area, width=35, borderwidth= 5) #area of floor
		self.perimeter_label= Label(self, text="Perimeter")
		self.perimeter= Entry(self, textvariable=self.perimeter, width=10, borderwidth= 5, )
		
		self.paint_req_label= Label(self, text="Paint required (metres)")
		self.paint_req = Entry(self, width=35, borderwidth=5)

		self.vol_room_label= Label(self, text="Total volume of room (metres)")
		self.vol_room = Entry(self,textvariable=self.volume, width=35, borderwidth=5)

		self.length_label = Label(self, text="length wall")
		self.walls_length = Entry(self,textvariable=self.walls_length,width=10, borderwidth = 5)

		self.width_label = Label(self, text="width of wall")
		self.walls_width = Entry(self,textvariable=self.walls_width,width=10, borderwidth = 5)

		self.depth_label = Label(self, text="depth of wall")
		self.walls_depth = Entry(self,textvariable=self.walls_depth,width=10, borderwidth = 5)

		
		# define entry boxes
		#walls_width_north =tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)

		#validate the entry is a number

		# define buttons

		#self.button1 = Button(self, text = "calculate area of floor", padx=40, pady=20, command=lambda: buttonClick(1))

		#self.buttonClear = Button(self, text = "Clear",padx=31,pady=20,command= buttonClear)

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

	def return_perimeter(self):
		self.perimeter_val = ((float(self.walls_width.get())) + (float(self.walls_length.get()))) * 2
		self.perimeter.insert(0,float(self.perimeter_val))

		
	def return_area(self):

		
		#self.avg_width = (float(self.walls_width_north.get()) + float(self.walls_width_north.get()) + float(self.walls_width_south.get()) + float(self.walls_width_west.get())) // 4
		#self.avg_width = self.walls_length_north = (float(entry_self.walls_length_north).get()+ self.walls_length_east = (float(self.area_valntry_walls_length_east).get()+ self.walls_length_south = float(self.area_valntry_walls_length_south).get()+ 
		
		self.area = ((float(self.walls_width.get())) * (float(self.walls_length.get())))
		#self.perimeter_val = ((float(self.walls_width.get())) + (float(self.walls_length.get()))) * 2

		self.area_val.insert(0,float(self.area))

		#return_perimeter()
		

		#self.avg_length = (float(self.walls_length_north.get()) + float(self.walls_length_north.get()) + float(self.walls_length_south.get()) + float(self.walls_length_west.get()))
		#self.avg_width = (float(self.walls_width_north.get()) + float(self.walls_width_north.get()) + float(self.walls_width_south.get()) + float(self.walls_width_west.get())) // 4
		 
		#self.perimeter_val = ((float(self.walls_width.get())) + (float(self.walls_length.get()))) * 2
		
		#self.area_val.set(self.area)

	def return_volume(self):
		self.volume_val = ((float(self.walls_width.get())) * (float(self.walls_length.get())) * (float(self.walls_depth.get()))) *1
		
		self.vol_room.insert(0,float(self.volume_val))

#self.mainloop()
if __name__ == "__main__":
	app = Paint_calculator()
	app.mainloop()