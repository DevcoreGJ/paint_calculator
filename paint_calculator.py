import tkinter as tk
from tkinter import *
import tkinter as ttk
from tkinter.messagebox import showinfo

global errInvOp
errInvOp = "Not a valid operator please choose from the buttons provided."



class Paint_calculator(tk.Tk):
	def __init__(self):
		super().__init__()



		vcmd = ((self.enter_only_digits),
			'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		self.area_label= Label(self, text="Area of floor(metres)")
		self.e= Entry(self, width=35, borderwidth= 5) #area of floor

		self.paint_req_label= Label(self, text="Paint required (metres)")
		self.paint_req = Entry(self, width=35, borderwidth=5)

		self.vol_room_label= Label(self, text="Total volume of room (metres)")
		self.vol_room = Entry(self, width=35, borderwidth=5)

		self.north_width_label = Label(self, text="width of north wall")
		self.walls_width_north = Entry(self, width=10, borderwidth = 5)

		self.north_height_label = Label(self, text="height of north wall")
		self.walls_height_north = Entry(self, width=10, borderwidth = 5)

		self.east_width_label = Label(self, text="width of east wall")
		self.walls_width_east = Entry(self, width=10, borderwidth = 5)

		self.east_height_label = Label(self, text="height of east wall")
		self.walls_height_east = Entry(self, width=10, borderwidth = 5)

		self.south_width_label = Label(self, text="width of south wall")
		self.walls_width_south = Entry(self, width=10, borderwidth = 5)

		self.south_height_label = Label(self, text="height of south wall")
		self.walls_height_south = Entry(self, width=10, borderwidth = 5)

		self.west_width_label = Label(self, text="width of west wall")
		self.walls_width_west = Entry(self, width=10, borderwidth = 5)

		self.walls_height_west = Entry(self, validate = 'key', validatecommand = vcmd ,width=10, borderwidth = 5)
		self.west_height_label = Label(self, text="height of west wall")
		# define entry boxes
		#walls_width_north =tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)

		#validate the entry is a number

		# define buttons

		self.button1 = Button(self, text = "calculate area of floor", padx=40, pady=20, command=lambda: buttonClick(1))

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

	def validate(self, action, index, value_if_allowed,
		prior_value, text, validation_type, trigger_type, widget_name):
		if value_if_allowed:
			try:
				float(value_if_allowed)
				return True
			except ValueError:
				return False
		else:
			return False
	def enter_only_digits(self, entry, action_type) -> bool:
		if action_type == '1' and not entry.isdigit():
			 return False

		return True


#self.mainloop()
if __name__ == "__main__":
  app = Paint_calculator()
  app.mainloop()