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
		self.get_vol = ttk.Button(	self, text = "area =", padx=40, pady=20, command=lambda: buttonClick(1))

		self.get_area.grid(row = 7, column = 0, columnspan = 1)
		self.get_paint_req.grid(row = 7, column = 1, columnspan = 1)
		self.get_vol.grid(row = 7, column = 2, columnspan = 1)

		self.walls_height_north = tk.StringVar()
		self.walls_height_east = tk.StringVar()
		self.walls_height_south = tk.StringVar()
		self.walls_height_west = tk.StringVar()

		self.walls_width_north = tk.StringVar()
		self.walls_width_east = tk.StringVar()
		self.walls_width_south = tk.StringVar()
		self.walls_width_west = tk.StringVar()
		self.area = tk.StringVar()
		self.e = tk.StringVar()
		

		self.area_label= Label(self, text="Area of floor(metres)")
		
		self.e= Entry(self, textvariable=self.e, width=35, borderwidth= 5) #area of floor

		self.paint_req_label= Label(self, text="Paint required (metres)")
		self.paint_req = Entry(self, width=35, borderwidth=5)

		self.vol_room_label= Label(self, text="Total volume of room (metres)")
		self.vol_room = Entry(self, width=35, borderwidth=5)

		self.north_width_label = Label(self, text="width of north wall")
		self.walls_width_north = Entry(self,textvariable=self.walls_width_north, width=10, borderwidth = 5)

		self.north_height_label = Label(self, text="height of north wall")
		self.walls_height_north = Entry(self,textvariable=self.walls_height_north,width=10, borderwidth = 5)

		self.east_width_label = Label(self, text="width of east wall")
		self.walls_width_east = Entry(self,textvariable=self.walls_width_east,width=10, borderwidth = 5)

		self.east_height_label = Label(self, text="height of east wall")
		self.walls_height_east = Entry(self,textvariable=self.walls_height_east,width=10, borderwidth = 5)

		self.south_width_label = Label(self, text="width of south wall")
		self.walls_width_south = Entry(self,textvariable=self.walls_width_south,width=10, borderwidth = 5)

		self.south_height_label = Label(self, text="height of south wall")
		self.walls_height_south = Entry(self,textvariable=self.walls_height_south, width=10, borderwidth = 5)

		self.west_width_label = Label(self, text="width of west wall")
		self.walls_width_west = Entry(self,textvariable=self.walls_width_west, width=10, borderwidth = 5)

		self.west_height_label = Label(self, text="height of west wall")
		self.walls_height_west = Entry(self,textvariable=self.walls_height_west, width=10, borderwidth = 5)
		# define entry boxes
		#walls_width_north =tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)

		#validate the entry is a number

		# define buttons

		#self.button1 = Button(self, text = "calculate area of floor", padx=40, pady=20, command=lambda: buttonClick(1))

		#self.buttonClear = Button(self, text = "Clear",padx=31,pady=20,command= buttonClear)

		self.area_label.grid(row=0, column=0)
		self.e.grid(row = 0, column = 1, columnspan = 5, padx=10, pady=10) #area of floor

		self.paint_req_label.grid(row=1, column=0)
		self.paint_req.grid(row = 1, column = 1, columnspan = 5, padx=10, pady=10)

		self.vol_room_label.grid(row=2, column=0)
		self.vol_room.grid(row = 2, column = 1, columnspan = 5, padx=10, pady=10)
		#height*width*depth

		self.north_width_label.grid(row= 3, column= 0)
		self.walls_width_north.grid(row = 3, column = 1)

		self.north_height_label.grid(row= 4,column= 0)
		self.walls_height_north.grid(row= 4, column= 1)

		self.east_width_label.grid(row= 3, column = 2)
		self.walls_width_east.grid(row= 3, column = 3)

		self.east_height_label.grid(row= 4, column= 2)
		self.walls_height_east.grid(row= 4, column= 3)

		self.south_width_label.grid(row= 5, column= 0)
		self.walls_width_south.grid(row= 5, column= 1)

		self.south_height_label.grid(row= 6, column= 0)
		self.walls_height_south.grid(row= 6, column = 1)

		self.west_width_label.grid(row= 5, column= 2)
		self.walls_width_west.grid(row= 5, column= 3)

		self.west_height_label.grid(row= 6, column= 2)
		self.walls_height_west.grid(row= 6, column= 3)

		
	#area = height * width

	def return_area(self):

		self.avg_height = (float(self.walls_height_north.get()) + float(self.walls_height_north.get()) + float(self.walls_height_south.get()) + float(self.walls_height_west.get())) // 4
		self.avg_width = (float(self.walls_width_north.get()) + float(self.walls_width_north.get()) + float(self.walls_width_south.get()) + float(self.walls_width_west.get())) // 4
		#self.avg_width = self.walls_height_north = (float(entry_self.walls_height_north).get()+ self.walls_height_east = (float(self.entry_walls_height_east).get()+ self.walls_height_south = float(self.entry_walls_height_south).get()+ 
		
		self.area = (self.avg_height * self.avg_width)

		self.e.insert(0,float(self.area))

	def return_volume(self):

		self
		#self.e.set(self.area)
#self.mainloop()
if __name__ == "__main__":
	app = Paint_calculator()
	app.mainloop()