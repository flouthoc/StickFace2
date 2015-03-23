
__author__ = "flouthoc (http://github.com/flouthoc)"
__copyright__ = "Copyright 2015"
__credits__ = ["Add Your Name and GitHub Link Here"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "flouthoc"
__email__ = "gunnerar7@gmail.com"
__contributers__ = "Add Your Name Here"
#!/usr/bin/env python
import sys
from gi.repository import Gtk


class StickFace:

	follow_unfollow_status = 1
	
	def append_textview(self, data):

#		buffer_new = Gtk.TextBuffer()
		self.end_iter = self.buffer.get_end_iter() 
		self.buffer.insert(self.end_iter, data)
#		self.textpad.set_buffer(self.buffer)

	def write_db(self, widget):

		self.end_iter_2 = self.buffer.get_end_iter()
		self.start_iter = self.buffer.get_start_iter()
		content = self.buffer.get_text(self.start_iter, self.end_iter_2, False)
		filter = content.strip()
		if not filter:
			return

		with open("data_file.stick", "a") as db:
			db.write("\n")
			db.write(content)
			db.write("\n")
			db.write("--EOF--")
	
	def kill_screen(self, widget, data=None):

		#sys.exit(1)
		self.window.destroy()

	def create_instance(self, widget):

		create_new = StickFace()

	def kill_application(self, widget, data=None):
		sys.exit(1)

	def show_window_bar(self, widget, data=None):

		self.window.set_decorated(True)

	def hide_window_bar(self, widget, data=None):

		self.window.set_decorated(False)

	def show_info(self, widget):

		dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "StickFace 2.0")
		dialog.format_secondary_text("A Minimalist Sticky Widget That Follows You Around Your Work Screen\n\n\n By flouthoc(gunnerar7@gmail.com) \n https://github.com/flouthoc \n\n\nContributers \n Add Your Name Here")
        	dialog.run()
        	dialog.destroy()
	
	def change_follow_unfollow_status(self, widget, data=None):
		
		print "ahahah"

		if(self.follow_unfollow_status == 1):
			self.window.set_keep_above(False)
			self.window.set_keep_below(True)
			self.follow_unfollow_status = 0
			self.follow_button.set_label("Follow Me")
#			
		else:
			self.window.set_keep_above(True)
			self.window.set_keep_below(False)
			self.follow_unfollow_status = 1
			self.follow_button.set_label("Go To Desktop")

#	def hello(self, widget, data=None):
#		print "Hello World"

#	def delete_event(self, widget, event, data=None):
		
#		print "delete event occurred"
#		return FALSE

#	def destroy(self, widget, data=None):

#		self.window.destroy()
	
	def __init__(self):
	
		self.window = Gtk.Window()

		#connections
#		self.window.connect("destroy", self.delete_event)
#		self.window.connect("destroy", self.destroy)

		#properties
		self.window.set_border_width(10)
		self.window.set_default_size(230, 150)
		self.window.set_decorated(False)
		self.window.set_keep_above(True)

		#self.window.set_has_resize_grip(True)
		#self.window.set_has_resize_grip(True)

		#elemnts
		self.buffer = Gtk.TextBuffer()
		self.buffer.set_text("")
		self.textpad = Gtk.TextView()
		self.textpad.set_size_request(230,150)
		self.textpad.set_vexpand(True)
		self.textpad.set_hexpand(True)
		self.textpad.set_wrap_mode(3)
		self.textpad.set_buffer(self.buffer)

		self.scroll = Gtk.ScrolledWindow(None,None)
		self.scroll.set_size_request(230,150)
		self.scroll.add(self.textpad)

	
		self.toolbar1 = Gtk.Toolbar.new()
		self.toolbar2 = Gtk.Toolbar.new()
		self.toolbar1.set_style(1)
		self.toolbar2.set_style(0)
		self.grid = Gtk.Grid()
		#self.button = Gtk.ToolButton("Hello")
		#self.follow_button = Gtk.ToolButton("Go To DeskTop")
		self.exit_button = Gtk.ToolButton.new(None, "Kill All")
        	self.follow_button = Gtk.ToolButton.new(None,"Go To DeskTop")
		self.new_button = Gtk.ToolButton(Gtk.STOCK_DND,None)
		self.kill_button = Gtk.ToolButton(Gtk.STOCK_CANCEL,None)
		self.info_button = Gtk.ToolButton(Gtk.STOCK_ABOUT,None)

		
		#signals
		#self.exit_button.connect("clicked", self.kill_screen)
		self.window.connect("enter_notify_event", self.show_window_bar)
		self.follow_button.connect("clicked", self.change_follow_unfollow_status, self.window)
		self.window.connect("focus_out_event", self.hide_window_bar)
		self.window.connect("delete-event", Gtk.main_quit)
		self.kill_button.connect("clicked", self.write_db)
		self.exit_button.connect("clicked", self.kill_application)
		self.new_button.connect("clicked", self.create_instance)
		self.info_button.connect("clicked", self.show_info)
	#	self.new_button.connect("clicked", self.populate_textview,"did it")

		#merging
		self.toolbar1.insert(self.follow_button, 0)
		self.toolbar1.insert(self.exit_button, 1)
		self.toolbar2.insert(self.new_button, 0)
                self.toolbar2.insert(self.kill_button, 1)
		self.toolbar2.insert(self.info_button, 2)
		
		self.grid.attach(self.toolbar1,0,0,1,1)
		self.grid.attach(self.scroll,0,1,1,1)
		self.grid.attach(self.toolbar2,0,2,1,1)
		self.window.add(self.grid)
#		self.window.add(self.toolbar1)


		#inits
		self.toolbar2.show()
		self.toolbar1.show()
		self.grid.show()
		self.textpad.show()
		self.scroll.show()
#		self.button.show()
		self.follow_button.show()
		self.window.show_all()
	
	def main(self):

		Gtk.main()

if __name__ == "__main__":

	
#	hello = StickFace()
#	hello2 = StickFace()
#	hello.append_textview(" ")
#	hello.append_textview("d")
#	hello.append_textview("a")
#	hello2.main()
#	hello.main()



	hold_faces = list()
	faces = list()
#	faces = [StickFace() for i in range(3)]
	i = 0
#	for face in faces:
#		hold_faces.insert(j, face)
#		faces[j].main()
#		j += 1

	with open("data_file.stick", "r") as db:
		for line in db.readlines():
			line = line.strip()
			if(i == 0):
				faces.insert(i,StickFace())
				i += 1
			if(line == "--EOF--"):
				print "Loaded a Note"
				faces.insert(i,StickFace())
				i = i + 1
				
			else:
#				faces.insert(i,StickFace())
				faces[i-1].append_textview("\n")
				faces[i-1].append_textview(line)
			
	j = 0
	for face in faces:
		hold_faces.insert(j, face)
		faces[j].main()
		j += 1

				
