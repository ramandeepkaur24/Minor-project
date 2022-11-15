from tkinter import ttk
import tkinter as tk
class a():
	# Creating tkinter window
	window = tk.Tk()
	window.geometry('430x550')

	s=ttk.Style()
	s.theme_use('clam')
	s.configure('Treeview', rowheight=43)


	# Using treeview widget
	treev = ttk.Treeview(window,columns = ("1", "2", "3"),show = 'headings',height=60)

	# Calling pack method w.r.to treeview
	treev.pack(side ='top')

	# Assigning the width and anchor to the
	# respective columns and heading
	treev.column("1", width = 120, anchor ='center')
	treev.heading("1", text ="SR_NUMBER")
	treev.column("2", width = 190, anchor ='center')
	treev.heading("2", text ="NAME")
	treev.column("3", width = 120, anchor ='center')
	treev.heading("3", text ="CONTACT NUMBER")


	# Inserting the items and their features to the
	# columns built
	treev.insert("", 'end', text ="L1",
				values =("1", "Police", "100"))
	treev.insert("", 'end', text ="L2",
				values =("2", "Ambulance Health", "108"))
	treev.insert("", 'end', text ="L3",
				values =("3", "HelpLine for Women", "1091"))
	treev.insert("", 'end', text ="L4",
				values =("4", "Traffic HelpLine", "1073"))
	treev.insert("", 'end', text ="L5",
				values =("5", "Fire department", "101"))
	treev.insert("", 'end', text ="L6",
				values =("6", "Railway", "139"))
	treev.insert("", 'end', text ="L7",
				values =("7", "Blood Bank,Red Cross Ludhiana", "0161-2441257"))
	treev.insert("", 'end', text ="L8",
				values =("8", "Centralized Helpline Number", "112"))
	treev.insert("", 'end', text ="L10",
				values =("9", "Child Helpline", "1098"))
	treev.insert("", 'end', text ="L11",
				values =("10", "Tourism Support Helpline", "104"))
	treev.insert("", 'end', text ="L12",
				values =("11", "UNIFIED STATE HELPLINE FOR CITIZEN CENTRIC SERVICES", "1100"))
	treev.insert("", 'end', text ="L13",
				values =("12", "ANTI CORRPUTION HELPLINE", "9501200200"))

	# Calling mainloop
	window.mainloop()
obj=A()