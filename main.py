from tkinter import *
from tkinter import messagebox

# Messagebox for closing
def close():
	if messagebox.askquestion("Shop BK", "Do you really want to exit?") == 'yes':
		root.destroy()

# Logo
def logo(scr, cl):
	# global cv
	cv = Canvas(scr, width = 1200, height = 200)
	cv.create_image(70, 75, image = lg)
	cv.create_text(650, 50, text = "SHOP BK", font = ("MV Boli", 50), fill = "blue")
	cv.create_text(650, 120, text = "Best Key for your costumes!", font = ("Arial", 30))
	cv.create_line(0, 160, 1200, 160, width = 5)
	cv.create_line(0, 170, 1200, 170, width = 2)
	cv.grid(row = 0, columnspan = cl)

###---------------------###
###-------BOSS----------###
###---------------------###

## CUSTOMER ##
def customer1(*arg):
	global scr11
	global fr111
	global fr112
	global name_entry11
	global phone_entry11
	global agemin_entry11
	global agemax_entry11
	global gender11
	global rs11
	global icon_name11
	global icon_phone11
	global icon_age11
	global icon_true11
	global icon_false11
	global icon_bg11
	global results11
	global results11_name
	global results11_phone
	global results11_age
	global results11_gender
	global results11_price
	global btn_first11
	global btn_prev11
	global btn_next11
	global btn_end11
	global text_results11
	global back11
	global icon_page11

	scr01.withdraw()
	scr11 = Toplevel(scr01)
	x0 = scr01.winfo_x()
	y0 = scr01.winfo_y()
	scr11.geometry("1200x700+%d+%d" %(x0, y0))
	scr11.title("Customer")
	scr11.resizable(width = False, height = False)
	scr11.protocol("WM_DELETE_WINDOW", close)
	logo(scr11, 12)
	
	## Info
	fr = Frame(scr11)
	fr111 = Frame(fr)
	# Name
	Label(fr111, text = "Name", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr111).grid(row = 1)
	name11 = StringVar()
	name_entry11 = Entry(fr111, textvariable = name11, width = 20, font = 30)
	name_entry11.grid(row = 0, column = 1, columnspan = 3, sticky = W)
	
	# Phone
	Label(fr111, text = "Phone", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr111).grid(row = 3)
	phone11 = StringVar()
	phone_entry11 = Entry(fr111, textvariable = phone11, width = 20, font = 30)
	phone_entry11.grid(row = 2, column = 1, columnspan = 3, sticky = W)

	# Age
	Label(fr111, text = "Age", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr111).grid(row = 5)
	agemin11 = StringVar()
	agemin_entry11 = Entry(fr111, textvariable = agemin11, width = 5, font = 30)
	agemin_entry11.grid(row = 4, column = 1, sticky = W)

	Label(fr111, text = "-", font = ("Tahoma", 20)).grid(row = 4, column = 2)
	
	agemax11 = StringVar()
	agemax_entry11 = Entry(fr111, textvariable = agemax11, width = 5, font = 30)
	agemax_entry11.grid(row = 4, column = 3, sticky = E)

	# Gender
	Label(fr111, text = "Gender", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr111).grid(row = 7)
	gender11 = StringVar()
	OptionMenu(fr111, gender11, "All", "Male", "Female").grid(row = 6, column = 1, columnspan = 2, sticky = W)
	# Radiobutton(fr111, text = "All", font = 14, variable = gender11, value = 3).grid(row = 6, column = 1, sticky = W)
	# Radiobutton(fr111, text = "Male", font = 14, variable = gender11, value = 1).grid(row = 7, column = 1, sticky = W)
	# Radiobutton(fr111, text = "Female", font = 14, variable = gender11, value = 2).grid(row = 8, column = 1, sticky = W)
	gender11.set("All")

	# Reset
	rs11 = PhotoImage(file = "reset.png")
	Button(fr111, image = rs11, relief = FLAT, command = reset11).grid(row = 9, column = 1, sticky = W)
	# scr11.bind("r", reset)
	
	# SEARCH
	Button(fr111, text = "SEARCH", font = ("Tahoma", 16), command = search11).grid(row = 9, column = 2, columnspan = 2, sticky = E)
	scr11.bind("<Return>", search11)
	Label(fr111).grid(row = 10)

	text_results11 = Label(fr111, font = ("Arial", 15))
	text_results11.grid(row = 11, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back11 = PhotoImage(file = "left.png")
	Label(fr111).grid(row = 12)
	Button(fr111, image = back11, relief = FLAT, command = cus2log11).grid(row = 13, column = 0)

	# Check icons
	icon_true11 = PhotoImage(file = "true.png")
	icon_false11 = PhotoImage(file = "false.png")
	icon_bg11 =  PhotoImage(file = "bg.png")

	icon_name11 = Label(fr111, image = icon_bg11)
	icon_name11.grid(row = 0, column = 4, padx = 20)
	icon_phone11 = Label(fr111, image = icon_bg11)
	icon_phone11.grid(row = 2, column = 4, padx = 20)
	icon_age11 = Label(fr111, image = icon_bg11)
	icon_age11.grid(row = 4, column = 4, padx = 20)

	## Results
	fr112 = Frame(fr)
	Label(fr112, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr112, text = "Name", font = ("Tahoma", 20)).grid(row = 0, column = 6, columnspan = 2, padx = 50)
	Label(fr112, text = "Phone", font = ("Tahoma", 20)).grid(row = 0, column = 8, columnspan = 2, padx = 40)
	Label(fr112, text = "Age", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 20)
	Label(fr112, text = "Gen.", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	Label(fr112, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 12, padx = 20)
	
	# No.
	results11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11[i] = Label(fr112, font = ("Tahoma", 20))
		results11[i].grid(row = i, column = 5)

	# Name
	results11_name = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11_name[i] = Label(fr112, font = ("Arial", 15))
		results11_name[i].grid(row = i, column = 6, columnspan = 2)

	# Phone
	results11_phone = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11_phone[i] = Label(fr112, font = ("Arial", 15))
		results11_phone[i].grid(row = i, column = 8, columnspan = 2)
	# Age
	results11_age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11_age[i] = Label(fr112, font = ("Arial", 15))
		results11_age[i].grid(row = i, column = 10)

	# Gender
	results11_gender = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11_gender[i] = Label(fr112, font = ("Arial", 15))
		results11_gender[i].grid(row = i, column = 11)

	# Price
	results11_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results11_price[i] = Label(fr112, font = ("Arial", 15))
		results11_price[i].grid(row = i, column = 12)

	btn_first11 = Button(fr112, font = ("Arial", 15), relief = FLAT)
	btn_first11.grid(row = 11, column = 6)
	btn_prev11 = Button(fr112, font = ("Arial", 15), relief = FLAT)
	btn_prev11.grid(row = 11, column = 7)
	btn_next11 = Button(fr112, font = ("Arial", 15), relief = FLAT)
	btn_next11.grid(row = 11, column = 8)
	btn_end11 = Button(fr112, font = ("Arial", 15), relief = FLAT)
	btn_end11.grid(row = 11, column = 9)
	icon_page11 = Label(fr112, font = ("Arial", 15))
	icon_page11.grid(row = 11, column = 12)
	
	fr111.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr112.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def cus2log11():
	x0 = scr11.winfo_x()
	y0 = scr11.winfo_y()
	scr11.destroy()
	scr01.deiconify()
	scr01.geometry("1200x700+%d+%d" %(x0, y0))

def reset11(*arg):
	name_entry11.delete(0, END)
	phone_entry11.delete(0, END)
	agemin_entry11.delete(0, END)
	agemax_entry11.delete(0, END)
	gender11.set("All")
	icon_name11.configure(image = icon_bg11)
	icon_phone11.configure(image = icon_bg11)
	icon_age11.configure(image = icon_bg11)
	text_results11.configure(text = "")
	for i in range(1, 11):
		results11[i].configure(text = "")
		results11_name[i].configure(text = "")
		results11_phone[i].configure(text = "")
		results11_age[i].configure(text = "")
		results11_gender[i].configure(text = "")
		results11_price[i].configure(text = "")
	btn_first11.configure(text = "", command = donothing)
	btn_prev11.configure(text = "", command = donothing)
	btn_next11.configure(text = "", command = donothing)
	btn_end11.configure(text = "", command = donothing)
	icon_page11.configure(text = "", relief = FLAT)

def donothing():
	pass

def search11(*arg):
	global numOfresults11
	global numOfpages11
	global page11
	global name111
	global phone111
	global age111
	global gender111
	global price111
	name110 = name_entry11.get()
	phone110 = phone_entry11.get()
	agemin110 = agemin_entry11.get()
	agemax110 = agemax_entry11.get()
	gender110 = gender11.get()

	# Check name
	check_name = True
	name110 = name110.upper()  # Capitalize all letters11 of name
	for i in range (0, len(name110)):
		if (ord(name110[i]) != 32) and ((ord(name110[i]) < 65) or (ord(name110[i]) > 90)):
			check_name = False
	
	if check_name:
		# global icon_name11
		# icon_name11.grid_forget()
		# icon_name11 = Label(fr111, image = icon_true11)
		# icon_name11.grid(row = 0, column = 4, padx = 20)
		icon_name11.configure(image = icon_true11)
	else:
		# icon_name11.grid_forget()
		# icon_name11 = Label(fr111, image = icon_false11)
		# icon_name11.grid(row = 0, column = 4, padx = 20)
		icon_name11.configure(image = icon_false11)

	# Check phone
	check_phone = True
	if phone110 != "":
		check_phone = phone110.isdigit()
	
	if check_phone:
		icon_phone11.configure(image = icon_true11)
	else:
		icon_phone11.configure(image = icon_false11)

	# Check age
	check_age = True
	if agemin110 != "":
		check_age = agemin110.isdigit()
	if agemax110 != "":
		check_age = agemax110.isdigit()
	if (agemin110 != "") and (agemax110 != ""):
		if (agemin110.isdigit() == False) or (agemax110.isdigit() == False):
			check_age = False
		elif int(agemin110) > int(agemax110):
			check_age = False
	
	if check_age:
		icon_age11.configure(image = icon_true11)
	else:
		icon_age11.configure(image = icon_false11)

	# Convert gender
	if gender110 == "Male":
		gender110 = "M"
	elif gender110 == "Female":
		gender110 = "F"

	# All checks are true
	if check_name and check_phone and check_age:
		file = open("customer.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; name111 = []; phone111 = []; age111 = []; gender111 = []; price111 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			name111.append(sub[0].replace(".", " ", 10))
			phone111.append(sub[1])
			age111.append(sub[2])
			gender111.append(sub[3])
			price111.append(sub[4])

		name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []
		if name110 != "":
			for i in range(0, len(name111)):
				if name111[i].find(name110) != -1:
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []
		
		if phone110 != "":
			for i in range(0, len(phone111)):
				if phone111[i].find(phone110) != -1:
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []
		
		if agemin110 != "" and agemax110 == "":
			for i in range(0, len(age111)):
				if int(age111[i]) >= int(agemin110):
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []

		if agemin110 == "" and agemax110 != "":
			for i in range(0, len(age111)):
				if int(age111[i]) <= int(agemax110):
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []

		if agemin110 != "" and agemax110 != "":
			for i in range(0, len(age111)):
				if int(agemin110) <= int(age111[i]) <= int(agemax110):
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []

		if gender110 != "All":
			for i in range(0, len(gender111)):
				if gender111[i] == gender110:
					name2.append(name111[i])
					phone2.append(phone111[i])
					age2.append(age111[i])
					gender2.append(gender111[i])
					price2.append(price111[i])
			name111 = name2; phone111 = phone2; age111 = age2; gender111 = gender2; price111 = price2
			name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []

		# Sort
		for i in range(0, len(name111)):
			name111[i] = name111[i].lower()
			name111[i] = name111[i].title()
			price111[i] = int(price111[i])

		name111 = [x for _, x in sorted(zip(price111, name111))]; name111.reverse()
		phone111 = [x for _, x in sorted(zip(price111, phone111))]; phone111.reverse()
		age111 = [x for _, x in sorted(zip(price111, age111))]; age111.reverse()
		gender111 = [x for _, x in sorted(zip(price111, gender111))]; gender111.reverse()
		price111.sort(reverse = True)
		for i in range(0, len(price111)):
			price111[i] = str(price111[i])

		# Show
		numOfresults11 = len(name111)
		if (numOfresults11 == 0) or (numOfresults11 == 1):
			text_results11.configure(text = "%d result found" %numOfresults11)
		else:
			text_results11.configure(text = "%d results found" %numOfresults11)

		if numOfresults11 != 0:
			numOfpages11 = ((numOfresults11 - 1) // 10) + 1
			btn_first11.configure(text = "1", command = first11)
			btn_prev11.configure(text = "<", command = prev11)
			btn_next11.configure(text = ">", command = next11)
			btn_end11.configure(text = "End", command = end11)
			page11 = 1
			showResults11(page11)
	else:
		text_results11.configure(text = "")
		for i in range(1, 11):
			results11[i].configure(text = "")
			results11_name[i].configure(text = "")
			results11_phone[i].configure(text = "")
			results11_age[i].configure(text = "")
			results11_gender[i].configure(text = "")
			results11_price[i].configure(text = "")
		btn_first11.configure(text = "", command = donothing)
		btn_prev11.configure(text = "", command = donothing)
		btn_next11.configure(text = "", command = donothing)
		btn_end11.configure(text = "", command = donothing)
		icon_page11.configure(text = "", relief = FLAT)

def showResults11(index):
	icon_page11.configure(text = index, relief = GROOVE)
	if index == numOfpages11:
		for i in range(1, numOfresults11 - 10*(numOfpages11 - 1) + 1):
			results11[i].configure(text = 10*(numOfpages11 - 1) + i)
			results11_name[i].configure(text = name111[10*(numOfpages11 - 1) + i - 1])
			results11_phone[i].configure(text = phone111[10*(numOfpages11 - 1) + i - 1])
			results11_age[i].configure(text = age111[10*(numOfpages11 - 1) + i - 1])
			results11_gender[i].configure(text = gender111[10*(numOfpages11 - 1) + i - 1])
			results11_price[i].configure(text = price111[10*(numOfpages11 - 1) + i - 1])
		if (numOfresults11 % 10) != 0:
			for i in range((numOfresults11 % 10) + 1, 11):
				results11[i].configure(text = "")
				results11_name[i].configure(text = "")
				results11_phone[i].configure(text = "")
				results11_age[i].configure(text = "")
				results11_gender[i].configure(text = "")
				results11_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results11[j].configure(text = 10*(index - 1) + j)
			results11_name[j].configure(text = name111[10*(index - 1) + j - 1])
			results11_phone[j].configure(text = phone111[10*(index - 1) + j - 1])
			results11_age[j].configure(text = age111[10*(index - 1) + j - 1])
			results11_gender[j].configure(text = gender111[10*(index - 1) + j - 1])
			results11_price[j].configure(text = price111[10*(index - 1) + j - 1])

# Buttons for showing results
def first11():
	global page11
	page11 = 1
	showResults11(page11)

def prev11():
	global page11
	if page11 != 1:
		page11 -= 1
		showResults11(page11)

def next11():
	global page11
	if page11 != numOfpages11:
		page11 += 1
		showResults11(page11)

def end11():
	global page11
	page11 = numOfpages11
	showResults11(page11)

###---------------------###

## PRODUCT ##
def product1(*arg):
	global scr12
	global fr121
	global fr122
	global id_entry12
	global type_entry12
	global size_entry12
	global brand_entry12
	global pricemin_entry12
	global pricemax_entry12
	global rs12
	global icon_id12
	global icon_type12
	global icon_size12
	global icon_brand12
	global icon_price12
	global icon_true12
	global icon_false12
	global icon_bg12
	global results12
	global results12_id
	global results12_type
	global results12_size
	global results12_brand
	global results12_quantity
	global results12_price
	global btn_first12
	global btn_prev12
	global btn_next12
	global btn_end12
	global text_results12
	global icon_page12
	global back12

	scr01.withdraw()
	scr12 = Toplevel(scr01)
	x0 = scr01.winfo_x()
	y0 = scr01.winfo_y()
	scr12.geometry("1200x700+%d+%d" %(x0, y0))
	scr12.title("Product")
	scr12.resizable(width = False, height = False)
	scr12.protocol("WM_DELETE_WINDOW", close)
	logo(scr12, 12)

	## Info
	fr = Frame(scr12)
	fr121 = Frame(fr)

	# ID
	Label(fr121, text = "ID", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr121).grid(row = 1)
	id12 = StringVar()
	id_entry12 = Entry(fr121, textvariable = id12, width = 20, font = 30)
	id_entry12.grid(row = 0, column = 1, columnspan = 3, sticky = W)
	
	# Type
	Label(fr121, text = "Type", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr121).grid(row = 3)
	type12 = StringVar()
	type_entry12 = Entry(fr121, textvariable = type12, width = 20, font = 30)
	type_entry12.grid(row = 2, column = 1, columnspan = 3, sticky = W)

	# Size
	Label(fr121, text = "Size", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr121).grid(row = 5)
	size12 = StringVar()
	size_entry12 = Entry(fr121, textvariable = size12, width = 20, font = 30)
	size_entry12.grid(row = 4, column = 1, columnspan = 3, sticky = W)

	# Brand
	Label(fr121, text = "Brand", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr121).grid(row = 7)
	brand12 = StringVar()
	brand_entry12 = Entry(fr121, textvariable = brand12, width = 20, font = 30)
	brand_entry12.grid(row = 6, column = 1, columnspan = 3, sticky = W)

	# Price
	Label(fr121, text = "Price", font = ("Tahoma", 20)).grid(row = 8, column = 0, sticky = W, padx = 30)
	Label(fr121).grid(row = 9)
	pricemin12 = StringVar()
	pricemin_entry12 = Entry(fr121, textvariable = pricemin12, width = 7, font = 30)
	pricemin_entry12.grid(row = 8, column = 1, sticky = W)

	Label(fr121, text = "-", font = ("Tahoma", 20)).grid(row = 8, column = 2)
	
	pricemax12 = StringVar()
	pricemax_entry12 = Entry(fr121, textvariable = pricemax12, width = 7, font = 30)
	pricemax_entry12.grid(row = 8, column = 3, sticky = E)

	# Reset
	rs12 = PhotoImage(file = "reset.png")
	Button(fr121, image = rs12, relief = FLAT, command = reset12).grid(row = 10, column = 1, sticky = W)
	# scr12.bind("F1", reset)

	# SEARCH
	Button(fr121, text = "SEARCH", font = ("Tahoma", 16), command = search12).grid(row = 10, column = 2, columnspan = 2, sticky = E)
	scr12.bind("<Return>", search12)
	Label(fr121).grid(row = 11)

	text_results12 = Label(fr121, font = ("Arial", 15))
	text_results12.grid(row = 12, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back12 = PhotoImage(file = "left.png")
	# Label(fr121).grid(row = 13)
	Button(fr121, image = back12, relief = FLAT, command = pro2log12).grid(row = 12, column = 0)

	# Check icons
	icon_true12 = PhotoImage(file = "true.png")
	icon_false12 = PhotoImage(file = "false.png")
	icon_bg12 =  PhotoImage(file = "bg.png")

	icon_id12 = Label(fr121, image = icon_bg12)
	icon_id12.grid(row = 0, column = 4, padx = 20)
	icon_type12 = Label(fr121, image = icon_bg12)
	icon_type12.grid(row = 2, column = 4, padx = 20)
	icon_size12 = Label(fr121, image = icon_bg12)
	icon_size12.grid(row = 4, column = 4, padx = 20)
	icon_brand12 = Label(fr121, image = icon_bg12)
	icon_brand12.grid(row = 6, column = 4, padx = 20)
	icon_price12 = Label(fr121, image = icon_bg12)
	icon_price12.grid(row = 8, column = 4, padx = 20)

	## Results
	fr122 = Frame(fr)
	Label(fr122, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr122, text = "ID", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 20)
	Label(fr122, text = "Type", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 20)
	Label(fr122, text = "Size", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 20)
	Label(fr122, text = "Brand", font = ("Tahoma", 20)).grid(row = 0, column = 9, columnspan = 2, padx = 20)
	Label(fr122, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	Label(fr122, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 12, padx = 20)
	
	# No.
	results12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12[i] = Label(fr122, font = ("Tahoma", 20))
		results12[i].grid(row = i, column = 5)

	# ID
	results12_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_id[i] = Label(fr122, font = ("Arial", 15))
		results12_id[i].grid(row = i, column = 6)

	# Type
	results12_type = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_type[i] = Label(fr122, font = ("Arial", 15))
		results12_type[i].grid(row = i, column = 7)

	# Size
	results12_size = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_size[i] = Label(fr122, font = ("Arial", 15))
		results12_size[i].grid(row = i, column = 8)

	# Brand
	results12_brand = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_brand[i] = Label(fr122, font = ("Arial", 15))
		results12_brand[i].grid(row = i, column = 9, columnspan = 2)

	# Quantity
	results12_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_quantity[i] = Label(fr122, font = ("Arial", 15))
		results12_quantity[i].grid(row = i, column = 11)

	# Price
	results12_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results12_price[i] = Label(fr122, font = ("Arial", 15))
		results12_price[i].grid(row = i, column = 12)

	btn_first12 = Button(fr122, font = ("Arial", 15), relief = FLAT)
	btn_first12.grid(row = 11, column = 6)
	btn_prev12 = Button(fr122, font = ("Arial", 15), relief = FLAT)
	btn_prev12.grid(row = 11, column = 7)
	btn_next12 = Button(fr122, font = ("Arial", 15), relief = FLAT)
	btn_next12.grid(row = 11, column = 8)
	btn_end12 = Button(fr122, font = ("Arial", 15), relief = FLAT)
	btn_end12.grid(row = 11, column = 9)
	icon_page12 = Label(fr122, font = ("Arial", 15))
	icon_page12.grid(row = 11, column = 12)
	
	fr121.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr122.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def pro2log12():
	x0 = scr12.winfo_x()
	y0 = scr12.winfo_y()
	scr12.destroy()
	scr01.deiconify()
	scr01.geometry("1200x700+%d+%d" %(x0, y0))

def reset12():
	id_entry12.delete(0, END)
	type_entry12.delete(0, END)
	size_entry12.delete(0, END)
	brand_entry12.delete(0, END)
	pricemin_entry12.delete(0, END)
	pricemax_entry12.delete(0, END)
	icon_id12.configure(image = icon_bg12)
	icon_type12.configure(image = icon_bg12)
	icon_size12.configure(image = icon_bg12)
	icon_brand12.configure(image = icon_bg12)
	icon_price12.configure(image = icon_bg12)
	text_results12.configure(text = "")

	for i in range(1, 11):
		results12[i].configure(text = "")
		results12_id[i].configure(text = "")
		results12_type[i].configure(text = "")
		results12_size[i].configure(text = "")
		results12_brand[i].configure(text = "")
		results12_quantity[i].configure(text = "")
		results12_price[i].configure(text = "")

	btn_first12.configure(text = "", command = donothing)
	btn_prev12.configure(text = "", command = donothing)
	btn_next12.configure(text = "", command = donothing)
	btn_end12.configure(text = "", command = donothing)
	icon_page12.configure(text = "", relief = FLAT)

def search12(*arg):
	global numOfresults12
	global numOfpages12
	global page12
	global id121
	global type121
	global size121
	global brand121
	global quantity121
	global price121

	id120 = id_entry12.get()
	type120 = type_entry12.get()
	size120 = size_entry12.get()
	brand120 = brand_entry12.get()
	pricemin120 = pricemin_entry12.get()
	pricemax120 = pricemax_entry12.get()

	# Check ID
	check_id = True
	if id120 != "":
		check_id = id120.isdigit()
	
	if check_id:
		icon_id12.configure(image = icon_true12)
	else:
		icon_id12.configure(image = icon_false12)

	# Check type
	check_type = True
	type120 = type120.upper()  # Capitalize all letters of name
	for i in range (0, len(type120)):
		if (ord(type120[i]) != 32) and ((ord(type120[i]) < 65) or (ord(type120[i]) > 90)):
			check_type = False

	if check_type:
		icon_type12.configure(image = icon_true12)
	else:
		icon_type12.configure(image = icon_false12)

	# Check size
	check_size = True
	if size120 != "":
		check_size = size120.isdigit()
	
	if check_size:
		icon_size12.configure(image = icon_true12)
	else:
		icon_size12.configure(image = icon_false12)

	# Check brand
	icon_brand12.configure(image = icon_true12)
	brand120 = brand120.upper()

	# Check price
	check_price = True
	if pricemin120 != "":
		check_price = pricemin120.isdigit()
	if pricemax120 != "":
		check_price = pricemax120.isdigit()
	if (pricemin120 != "") and (pricemax120 != ""):
		if (pricemin120.isdigit() == False) or (pricemax120.isdigit() == False):
			check_price = False
		elif int(pricemin120) > int(pricemax120):
			check_price = False
	
	if check_price:
		icon_price12.configure(image = icon_true12)
	else:
		icon_price12.configure(image = icon_false12)

	# All checks are true 
	if check_id and check_type and check_size and check_price:
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id121 = []; type121 = []; size121 = []; brand121 = []; quantity121 = []; price121 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			id121.append(sub[0])
			type121.append(sub[1].replace(".", " ", 10))
			size121.append(sub[2])
			brand121.append(sub[3].replace(".", " ", 10))
			quantity121.append(sub[4])
			price121.append(sub[5])

		id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []
		if id120 != "":
			for i in range(0, len(id121)):
				if id121[i].find(id120) != -1:
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		if type120 != "":
			for i in range(0, len(type121)):
				if type121[i].find(type120) != -1:
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		if size120 != "":
			for i in range(0, len(size121)):
				if size121[i].find(size120) != -1:
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		if brand120 != "":
			for i in range(0, len(brand121)):
				if brand121[i].find(brand120) != -1:
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		if pricemin120 != "" and pricemax120 == "":
			for i in range(0, len(price121)):
				if int(price121[i]) >= int(pricemin120):
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		elif pricemin120 == "" and pricemax120 != "":
			for i in range(0, len(price121)):
				if int(price121[i]) <= int(pricemax120):
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		elif pricemin120 != "" and pricemax120 != "":
			for i in range(0, len(price121)):
				if int(pricemin120) <= int(price121[i]) <= int(pricemax120):
					id2.append(id121[i])
					type2.append(type121[i])
					size2.append(size121[i])
					brand2.append(brand121[i])
					quantity2.append(quantity121[i])
					price2.append(price121[i])
			id121 = id2; type121 = type2; size121 = size2; brand121 = brand2; quantity121 = quantity2; price121 = price2
			id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

		# Sort
		for i in range(0, len(id121)):
			type121[i] = type121[i].lower()
			type121[i] = type121[i].title()
			brand121[i] = brand121[i].lower()
			brand121[i] = brand121[i].title()
			price121[i] = int(price121[i])

		id121 = [x for _, x in sorted(zip(price121, id121))]; id121.reverse()
		type121 = [x for _, x in sorted(zip(price121, type121))]; type121.reverse()
		size121 = [x for _, x in sorted(zip(price121, size121))]; size121.reverse()
		brand121 = [x for _, x in sorted(zip(price121, brand121))]; brand121.reverse()
		quantity121 = [x for _, x in sorted(zip(price121, quantity121))]; quantity121.reverse()
		price121.sort(reverse = True)
		for i in range(0, len(price121)):
			price121[i] = str(price121[i])

		# Show
		numOfresults12 = len(id121)
		if (numOfresults12 == 0) or (numOfresults12 == 1):
			text_results12.configure(text = "%d result found" %numOfresults12)
		else:
			text_results12.configure(text = "%d results found" %numOfresults12)

		if numOfresults12 != 0:
			numOfpages12 = ((numOfresults12 - 1) // 10) + 1
			btn_first12.configure(text = "1", command = first12)
			btn_prev12.configure(text = "<", command = prev12)
			btn_next12.configure(text = ">", command = next12)
			btn_end12.configure(text = "End", command = end12)
			page12 = 1
			showResults12(page12)
	else:
		text_results12.configure(text = "")
		for i in range(1, 11):
			results12[i].configure(text = "")
			results12_id[i].configure(text = "")
			results12_type[i].configure(text = "")
			results12_size[i].configure(text = "")
			results12_brand[i].configure(text = "")
			results12_quantity[i].configure(text = "")
			results12_price[i].configure(text = "")

		btn_first12.configure(text = "", command = donothing)
		btn_prev12.configure(text = "", command = donothing)
		btn_next12.configure(text = "", command = donothing)
		btn_end12.configure(text = "", command = donothing)
		icon_page12.configure(text = "", relief = FLAT)

def showResults12(index):
	icon_page12.configure(text = index, relief = GROOVE)
	if index == numOfpages12:
		for i in range(1, numOfresults12 - 10*(numOfpages12 - 1) + 1):
			results12[i].configure(text = 10*(numOfpages12 - 1) + i)
			results12_id[i].configure(text = id121[10*(numOfpages12 - 1) + i - 1])
			results12_type[i].configure(text = type121[10*(numOfpages12 - 1) + i - 1])
			results12_size[i].configure(text = size121[10*(numOfpages12 - 1) + i - 1])
			results12_brand[i].configure(text = brand121[10*(numOfpages12 - 1) + i - 1])
			results12_quantity[i].configure(text = quantity121[10*(numOfpages12 - 1) + i - 1])
			results12_price[i].configure(text = price121[10*(numOfpages12 - 1) + i - 1])
		if (numOfresults12 % 10) != 0:
			for i in range((numOfresults12 % 10) + 1, 11):
				results12[i].configure(text = "")
				results12_id[i].configure(text = "")
				results12_type[i].configure(text = "")
				results12_size[i].configure(text = "")
				results12_brand[i].configure(text = "")
				results12_quantity[i].configure(text = "")
				results12_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results12[j].configure(text = 10*(index - 1) + j)
			results12_id[j].configure(text = id121[10*(index - 1) + j - 1])
			results12_type[j].configure(text = type121[10*(index - 1) + j - 1])
			results12_size[j].configure(text = size121[10*(index - 1) + j - 1])
			results12_brand[j].configure(text = brand121[10*(index - 1) + j - 1])
			results12_quantity[j].configure(text = quantity121[10*(index - 1) + j - 1])
			results12_price[j].configure(text = price121[10*(index - 1) + j - 1])

# Button for showing results
def first12():
	global page12
	page12 = 1
	showResults12(page12)

def prev12():
	global page12
	if page12 != 1:
		page12 -= 1
		showResults12(page12)

def next12():
	global page12
	if page12 != numOfpages12:
		page12 += 1
		showResults12(page12)

def end12():
	global page12
	page12 = numOfpages12
	showResults12(page12)

###---------------------###

## TRANSACTION ##
def transaction1(*arg):
	global scr013
	global back013
	
	scr01.withdraw()
	scr013 = Toplevel(scr01)
	x0 = scr01.winfo_x()
	y0 = scr01.winfo_y()
	scr013.geometry("1200x700+%d+%d" %(x0, y0))
	scr013.title("Function")
	scr013.resizable(width = False, height = False)
	logo(scr013, 1)
	scr013.protocol("WM_DELETE_WINDOW", close)

	fr = Frame(scr013)
	Label(fr, text = "Hi Boss", font = 30, fg = "red").grid(row = 0, pady = 10)
	Button(fr, text = "3.1 Buy", width = 20, font = ("Tahoma", 20), command = buy1).grid(row = 1, pady = 30)
	scr013.bind("1", buy1)
	
	Button(fr, text = "3.2 Sell", width = 20, font = ("Tahoma", 20), command = sell1).grid(row = 2, pady = 30)
	scr013.bind("2", sell1)

	Button(fr, text = "3.3 Revenue", width = 20, font = ("Tahoma", 20), command = revenue1).grid(row = 3, pady = 30)
	scr013.bind("3", revenue1)
	
	back013 = PhotoImage(file = "left.png")
	Button(fr, image = back013, relief = FLAT, command = trans2func1).grid(row = 4, pady = 10)

	fr.grid(row = 1, pady = 20)

def trans2func1():
	x0 = scr013.winfo_x()
	y0 = scr013.winfo_y()
	scr013.destroy()
	scr01.deiconify()
	scr01.geometry("1200x700+%d+%d" %(x0, y0))

## Buy
def buy1():
	global scr13
	global fr131
	global fr132
	global day1_entry13
	global month1_entry13
	global day2_entry13
	global month2_entry13
	global rs13
	global icon_date131
	global icon_date132
	global icon_range13
	global icon_true13
	global icon_false13
	global icon_bg13
	global results13
	global results13_date
	global results13_orderid
	global results13_cusid
	global results13_prodid
	global results13_quantity
	global results13_price
	global btn_first13
	global btn_prev13
	global btn_next13
	global btn_end13
	global text_results13
	global back13
	global icon_page13

	scr013.withdraw()
	scr13 = Toplevel(scr013)
	x0 = scr013.winfo_x()
	y0 = scr013.winfo_y()
	scr13.geometry("1200x700+%d+%d" %(x0, y0))
	scr13.title("Buy")
	scr13.resizable(width = False, height = False)
	scr13.protocol("WM_DELETE_WINDOW", close)
	logo(scr13, 12)
	
	## Info
	fr = Frame(scr13)
	fr131 = Frame(fr)
	
	# BUY 
	Label(fr131, text = "BUY", font = ("Tahoma", 20)).grid(row = 0, column = 1, sticky = W, padx = 10)
	Label(fr131).grid(row = 1)

	# Date
	Label(fr131, text = "Date", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	day1 = StringVar()
	day1_entry13 = Entry(fr131, textvariable = day1, width = 3, font = 30)
	day1_entry13.grid(row = 2, column = 1, sticky = W)

	Label(fr131, text = "/", font = ("Tahoma", 20)).grid(row = 2, column = 2, sticky = W)
	
	month1 = StringVar()
	month1_entry13 = Entry(fr131, textvariable = month1, width = 3, font = 30)
	month1_entry13.grid(row = 2, column = 3)

	Label(fr131, text = "to", font = ("Tahoma", 20)).grid(row = 3, column = 2, sticky = W)
	day2 = StringVar()
	day2_entry13 = Entry(fr131, textvariable = day2, width = 3, font = 30)
	day2_entry13.grid(row = 4, column = 1, sticky = W)

	Label(fr131, text = "/", font = ("Tahoma", 20)).grid(row = 4, column = 2, sticky = W)
	
	month2 = StringVar()
	month2_entry13 = Entry(fr131, textvariable = month2, width = 3, font = 30)
	month2_entry13.grid(row = 4, column = 3)

	# Reset
	Label(fr131).grid(row = 5)
	rs13 = PhotoImage(file = "reset.png")
	Button(fr131, image = rs13, relief = FLAT, command = reset13).grid(row = 6, column = 1, sticky = W)
	# scr13.bind("r", reset13)
	
	# SEARCH
	Button(fr131, text = "SEARCH", font = ("Tahoma", 16), command = search13).grid(row = 6, column = 2, columnspan = 2, sticky = E)
	scr13.bind("<Return>", search13)
	# Label(fr131).grid(row = 10)

	text_results13 = Label(fr131, font = ("Arial", 15))
	text_results13.grid(row = 7, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back13 = PhotoImage(file = "left.png")
	Label(fr131).grid(row = 8)
	Label(fr131).grid(row = 9)
	Label(fr131).grid(row = 10)
	Label(fr131).grid(row = 11)
	Button(fr131, image = back13, relief = FLAT, command = buy2trans13).grid(row = 12, column = 0)

	# Check icons
	icon_true13 = PhotoImage(file = "true.png")
	icon_false13 = PhotoImage(file = "false.png")
	icon_bg13 =  PhotoImage(file = "bg.png")

	icon_date131 = Label(fr131, image = icon_bg13)
	icon_date131.grid(row = 2, column = 6, padx = 20)
	icon_date132 = Label(fr131, image = icon_bg13)
	icon_date132.grid(row = 4, column = 6, padx = 20)
	icon_range13 = Label(fr131, image = icon_bg13)
	icon_range13.grid(row = 3, column = 6, padx = 20)

	## Results
	fr132 = Frame(fr)
	Label(fr132, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr132, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 20)
	Label(fr132, text = "OrderID", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 20)
	Label(fr132, text = "CusID", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 30)
	Label(fr132, text = "ProdID", font = ("Tahoma", 20)).grid(row = 0, column = 9, padx = 20)
	Label(fr132, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 20)
	Label(fr132, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	
	# No.
	results13 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13[i] = Label(fr132, font = ("Tahoma", 20))
		results13[i].grid(row = i, column = 5)

	# Date
	results13_date = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_date[i] = Label(fr132, font = ("Arial", 15))
		results13_date[i].grid(row = i, column = 6)

	# OrderID
	results13_orderid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_orderid[i] = Label(fr132, font = ("Arial", 15))
		results13_orderid[i].grid(row = i, column = 7)

	# CusID
	results13_cusid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_cusid[i] = Label(fr132, font = ("Arial", 15))
		results13_cusid[i].grid(row = i, column = 8)

	# ProdID
	results13_prodid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_prodid[i] = Label(fr132, font = ("Arial", 15))
		results13_prodid[i].grid(row = i, column = 9)

	# Quantity
	results13_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_quantity[i] = Label(fr132, font = ("Arial", 15))
		results13_quantity[i].grid(row = i, column = 10)

	# Price
	results13_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results13_price[i] = Label(fr132, font = ("Arial", 15))
		results13_price[i].grid(row = i, column = 11)

	btn_first13 = Button(fr132, font = ("Arial", 15), relief = FLAT)
	btn_first13.grid(row = 11, column = 6)
	btn_prev13 = Button(fr132, font = ("Arial", 15), relief = FLAT)
	btn_prev13.grid(row = 11, column = 7)
	btn_next13 = Button(fr132, font = ("Arial", 15), relief = FLAT)
	btn_next13.grid(row = 11, column = 8)
	btn_end13 = Button(fr132, font = ("Arial", 15), relief = FLAT)
	btn_end13.grid(row = 11, column = 9)
	icon_page13 = Label(fr132, font = ("Arial", 15), relief = GROOVE)
	icon_page13.grid(row = 11, column = 11)
	
	fr131.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr132.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def buy2trans13():
	x0 = scr13.winfo_x()
	y0 = scr13.winfo_y()
	scr13.destroy()
	scr013.deiconify()
	scr013.geometry("1200x700+%d+%d" %(x0, y0))

def reset13():
	day1_entry13.delete(0, END)
	month1_entry13.delete(0, END)
	day2_entry13.delete(0, END)
	month2_entry13.delete(0, END)
	icon_date131.configure(image = icon_bg13)
	icon_date132.configure(image = icon_bg13)
	icon_range13.configure(image - icon_bg13)
	text_results13.configure(text = "")
	for i in range(1, 11):
		results13[i].configure(text = "")
		results13_date[i].configure(text = "")
		results13_orderid[i].configure(text = "")
		results13_cusid[i].configure(text = "")
		results13_prodid[i].configure(text = "")
		results13_quantity[i].configure(text = "")
		results13_price[i].configure(text = "")

	btn_first13.configure(text = "", command = donothing)
	btn_prev13.configure(text = "", command = donothing)
	btn_next13.configure(text = "", command = donothing)
	btn_end13.configure(text = "", command = donothing)
	icon_page13.configure(text = "", relief = FLAT)

def search13():
	global numOfresults13
	global numOfpages13
	global page13
	global date131
	global orderid131
	global cusid131
	global prodid131
	global quantity131
	global price131

	day1310 = day1_entry13.get()
	month1310 = month1_entry13.get()
	day1320 = day2_entry13.get()
	month1320 = month2_entry13.get()

	# Check date1
	check_date1 = True
	flag1 = False
	if (day1310 == "" and month1310 != "") or (day1310 != "" and month1310 == ""):
		check_date1 = False
	elif (day1310 != "" and month1310 != ""):
		if (day1310.isdigit() == False or month1310.isdigit() == False):
			check_date1 = False
		else:
			d1310 = int(day1310)
			m1310 = int(month1310)
			flag1 = True
			if m1310 not in range(1, 13):
				check_date1 = False
				flag1 = False
			else:
				if m1310 in [1, 3, 5, 7, 8, 10, 12] and d1310 not in range(1, 32):
					check_date1 = False
					flag1 = False
				elif m1310 in [4, 6, 9, 11] and d1310 not in range(1, 31):
					check_date1 = False
					flag1 = False
				elif m1310 == 2 and d1310 not in range(1, 30):
					check_date1 = False
					flag1 = False
	
	if check_date1:
		icon_date131.configure(image = icon_true13)
	else:
		icon_date131.configure(image = icon_false13)

	# Check date2
	check_date2 = True
	flag2 = False
	if (day1320 == "" and month1320 != "") or (day1320 != "" and month1320 == ""):
		check_date2 = False
	elif (day1320 != "" and month1320 != ""):
		if (day1320.isdigit() == False or month1320.isdigit() == False):
			check_date2 = False
		else:
			d1320 = int(day1320)
			m1320 = int(month1320)
			flag2 = True
			if m1320 not in range(1, 13):
				check_date2 = False
				flag2 = False
			else:
				if m1320 in [1, 3, 5, 7, 8, 10, 12] and d1320 not in range(1, 32):
					check_date2 = False
					flag2 = False
				elif m1320 in [4, 6, 9, 11] and d1320 not in range(1, 31):
					check_date2 = False
					flag2 = False
				elif m1320 == 2 and d1320 not in range(1, 30):
					check_date2 = False
					flag2 = False
	
	if check_date2:
		icon_date132.configure(image = icon_true13)
	else:
		icon_date132.configure(image = icon_false13)

	# Check range
	check_range = flag1 and flag2
	if check_range:
		if m1310 > m1320:
			check_range = False
		elif m1310 == m1320 and d1310 > d1320:
			check_range = False

	if (day1310 == "" and month1310 == "") and flag2:
		check_range = True
	elif flag1 and (day1320 == "" and month1320 == ""):
		check_range = True
	elif (day1310 == "" and month1310 == "") and (day1320 == "" and month1320 == ""):
		check_range = True
			
	if check_range:
		icon_range13.configure(image = icon_true13)
	else:
		icon_range13.configure(image = icon_false13)

	# All check are true	
	if check_date1 and check_date2 and check_range:
		file = open("hoadon_mua.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; date131 = []; day131 = []; month131 = []; orderid131 = []; cusid131 = []; prodid131 = []; quantity131 = []; price131 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			date131.append(sub[0].replace(".", " ", 10))
			sub2 = date131[i].split()
			day131.append(sub2[0])
			month131.append(sub2[1])
			orderid131.append(sub[1])
			cusid131.append(sub[2])
			prodid131.append(sub[3])
			quantity131.append(sub[4])
			price131.append(sub[5])

		date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		if flag1 and (day1320 == "" and month1320 == ""):
			for i in range(0, len(date131)):
				if (int(month131[i]) > m1310) or (int(month131[i]) == m1310 and int(day131[i]) >= d1310):
					date2.append(date131[i])
					day2.append(day131[i])
					month2.append(month131[i])
					orderid2.append(orderid131[i])
					cusid2.append(cusid131[i])
					prodid2.append(prodid131[i])
					quantity2.append(quantity131[i])
					price2.append(price131[i])
			date131 = date2; day131 = day2; month131 = month2; orderid131 = orderid2; cusid131 = cusid2; prodid131 = prodid2; quantity131 = quantity2; price131 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []
		
		elif (day1310 == "" and month1310 == "") and flag2:
			for i in range(0, len(date131)):
				if (int(month131[i]) < m1320) or (int(month131[i]) == m1320 and int(day131[i]) <= d1320):
					date2.append(date131[i])
					day2.append(day131[i])
					month2.append(month131[i])
					orderid2.append(orderid131[i])
					cusid2.append(cusid131[i])
					prodid2.append(prodid131[i])
					quantity2.append(quantity131[i])
					price2.append(price131[i])
			date131 = date2; day131 = day2; month131 = month2; orderid131 = orderid2; cusid131 = cusid2; prodid131 = prodid2; quantity131 = quantity2; price131 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		elif flag1 and flag2:
			for i in range(0, len(date131)):
				if (m1310 < int(month131[i]) < m1320) or (m1310 == int(month131[i]) < m1320 and int(day131[i]) >= d1310) or (m1310 < int(month131[i]) == m1320 and int(day131[i]) <= d1320) or (m1310 == int(month131[i]) == m1320 and d1310 <= int(day131[i]) <= d1320):
					date2.append(date131[i])
					day2.append(day131[i])
					month2.append(month131[i])
					orderid2.append(orderid131[i])
					cusid2.append(cusid131[i])
					prodid2.append(prodid131[i])
					quantity2.append(quantity131[i])
					price2.append(price131[i])
			date131 = date2; day131 = day2; month131 = month2; orderid131 = orderid2; cusid131 = cusid2; prodid131 = prodid2; quantity131 = quantity2; price131 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		# Sort
		for i in range(0, len(day131)):
			date131[i] = date131[i].replace(" ", "/", 10)

		# Show
		numOfresults13 = len(day131)
		if (numOfresults13 == 0) or (numOfresults13 == 1):
			text_results13.configure(text = "%d result found" %numOfresults13)
		else:
			text_results13.configure(text = "%d results found" %numOfresults13)

		if numOfresults13 != 0:
			numOfpages13 = ((numOfresults13 - 1) // 10) + 1
			btn_first13.configure(text = "1", command = first13)
			btn_prev13.configure(text = "<", command = prev13)
			btn_next13.configure(text = ">", command = next13)
			btn_end13.configure(text = "End", command = end13)
			page13 = 1
			showResults13(page13)
	else:
		text_results13.configure(text = "")
		for i in range(1, 11):
			results13[i].configure(text = "")
			results13_date[i].configure(text = "")
			results13_orderid[i].configure(text = "")
			results13_cusid[i].configure(text = "")
			results13_prodid[i].configure(text = "")
			results13_quantity[i].configure(text = "")
			results13_price[i].configure(text = "")
		btn_first13.configure(text = "", command = donothing)
		btn_prev13.configure(text = "", command = donothing)
		btn_next13.configure(text = "", command = donothing)
		btn_end13.configure(text = "", command = donothing)
		icon_page13.configure(text = "", relief = FLAT)

def showResults13(index):
	icon_page13.configure(text = index, relief = GROOVE)
	if index == numOfpages13:
		for i in range(1, numOfresults13 - 10*(numOfpages13 - 1) + 1):
			results13[i].configure(text = 10*(numOfpages13 - 1) + i)
			results13_date[i].configure(text = date131[10*(numOfpages13 - 1) + i - 1])
			results13_orderid[i].configure(text = orderid131[10*(numOfpages13 - 1) + i - 1])
			results13_cusid[i].configure(text = cusid131[10*(numOfpages13 - 1) + i - 1])
			results13_prodid[i].configure(text = prodid131[10*(numOfpages13 - 1) + i - 1])
			results13_quantity[i].configure(text = quantity131[10*(numOfpages13 - 1) + i - 1])
			results13_price[i].configure(text = price131[10*(numOfpages13 - 1) + i - 1])
		if (numOfresults13 % 10) != 0:
			for i in range((numOfresults13 % 10) + 1, 11):
				results13[i].configure(text = "")
				results13_date[i].configure(text = "")
				results13_orderid[i].configure(text = "")
				results13_cusid[i].configure(text = "")
				results13_prodid[i].configure(text = "")
				results13_quantity[i].configure(text = "")
				results13_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results13[j].configure(text = 10*(index - 1) + j)
			results13_date[j].configure(text = date131[10*(index - 1) + j - 1])
			results13_orderid[j].configure(text = orderid131[10*(index - 1) + j - 1])
			results13_cusid[j].configure(text = cusid131[10*(index - 1) + j - 1])
			results13_prodid[j].configure(text = prodid131[10*(index - 1) + j - 1])
			results13_quantity[j].configure(text = quantity131[10*(index - 1) + j - 1])
			results13_price[j].configure(text = price131[10*(index - 1) + j - 1])

# Buttons for showing results
def first13():
	global page13
	page13 = 1
	showResults13(page13)

def prev13():
	global page13
	if page13 != 1:
		page13 -= 1
		showResults13(page13)

def next13():
	global page13
	if page13 != numOfpages13:
		page13 += 1
		showResults13(page13)

def end13():
	global page13
	page13 = numOfpages13
	showResults13(page13)

# Sell
def sell1():
	global scr14
	global fr141
	global fr142
	global day1_entry14
	global month1_entry14
	global day2_entry14
	global month2_entry14
	global rs14
	global icon_date141
	global icon_date142
	global icon_range14
	global icon_true14
	global icon_false14
	global icon_bg14
	global results14
	global results14_date
	global results14_orderid
	global results14_cusid
	global results14_prodid
	global results14_quantity
	global results14_price
	global btn_first14
	global btn_prev14
	global btn_next14
	global btn_end14
	global text_results14
	global back14
	global icon_page14

	scr013.withdraw()
	scr14 = Toplevel(scr013)
	x0 = scr013.winfo_x()
	y0 = scr013.winfo_y()
	scr14.geometry("1200x700+%d+%d" %(x0, y0))
	scr14.title("Sell")
	scr14.resizable(width = False, height = False)
	scr14.protocol("WM_DELETE_WINDOW", close)
	logo(scr14, 12)
	
	## Info
	fr = Frame(scr14)
	fr141 = Frame(fr)
	
	# SELL
	Label(fr141, text = "SELL", font = ("Tahoma", 20)).grid(row = 0, column = 1, sticky = W, padx = 10)
	Label(fr141).grid(row = 1)

	# Date
	Label(fr141, text = "Date", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	day1 = StringVar()
	day1_entry14 = Entry(fr141, textvariable = day1, width = 3, font = 30)
	day1_entry14.grid(row = 2, column = 1, sticky = W)

	Label(fr141, text = "/", font = ("Tahoma", 20)).grid(row = 2, column = 2, sticky = W)
	
	month1 = StringVar()
	month1_entry14 = Entry(fr141, textvariable = month1, width = 3, font = 30)
	month1_entry14.grid(row = 2, column = 3)

	Label(fr141, text = "to", font = ("Tahoma", 20)).grid(row = 3, column = 2, sticky = W)
	day2 = StringVar()
	day2_entry14 = Entry(fr141, textvariable = day2, width = 3, font = 30)
	day2_entry14.grid(row = 4, column = 1, sticky = W)

	Label(fr141, text = "/", font = ("Tahoma", 20)).grid(row = 4, column = 2, sticky = W)
	
	month2 = StringVar()
	month2_entry14 = Entry(fr141, textvariable = month2, width = 3, font = 30)
	month2_entry14.grid(row = 4, column = 3)

	# Reset
	Label(fr141).grid(row = 5)
	rs14 = PhotoImage(file = "reset.png")
	Button(fr141, image = rs14, relief = FLAT, command = reset14).grid(row = 6, column = 1, sticky = W)
	# scr14.bind("r", reset14)
	
	# SEARCH
	Button(fr141, text = "SEARCH", font = ("Tahoma", 16), command = search14).grid(row = 6, column = 2, columnspan = 2, sticky = E)
	scr14.bind("<Return>", search14)
	# Label(fr141).grid(row = 10)

	text_results14 = Label(fr141, font = ("Arial", 15))
	text_results14.grid(row = 7, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back14 = PhotoImage(file = "left.png")
	Label(fr141).grid(row = 8)
	Label(fr141).grid(row = 9)
	Label(fr141).grid(row = 10)
	Label(fr141).grid(row = 11)
	Button(fr141, image = back14, relief = FLAT, command = sell2trans14).grid(row = 12, column = 0)

	# Check icons
	icon_true14 = PhotoImage(file = "true.png")
	icon_false14 = PhotoImage(file = "false.png")
	icon_bg14 =  PhotoImage(file = "bg.png")

	icon_date141 = Label(fr141, image = icon_bg14)
	icon_date141.grid(row = 2, column = 6, padx = 20)
	icon_date142 = Label(fr141, image = icon_bg14)
	icon_date142.grid(row = 4, column = 6, padx = 20)
	icon_range14 = Label(fr141, image = icon_bg14)
	icon_range14.grid(row = 3, column = 6, padx = 20)

	## Results
	fr142 = Frame(fr)
	Label(fr142, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr142, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 20)
	Label(fr142, text = "OrderID", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 20)
	Label(fr142, text = "CusID", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 30)
	Label(fr142, text = "ProdID", font = ("Tahoma", 20)).grid(row = 0, column = 9, padx = 20)
	Label(fr142, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 20)
	Label(fr142, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	
	# No.
	results14 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14[i] = Label(fr142, font = ("Tahoma", 20))
		results14[i].grid(row = i, column = 5)

	# Date
	results14_date = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_date[i] = Label(fr142, font = ("Arial", 15))
		results14_date[i].grid(row = i, column = 6)

	# OrderID
	results14_orderid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_orderid[i] = Label(fr142, font = ("Arial", 15))
		results14_orderid[i].grid(row = i, column = 7)

	# CusID
	results14_cusid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_cusid[i] = Label(fr142, font = ("Arial", 15))
		results14_cusid[i].grid(row = i, column = 8)

	# ProdID
	results14_prodid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_prodid[i] = Label(fr142, font = ("Arial", 15))
		results14_prodid[i].grid(row = i, column = 9)

	# Quantity
	results14_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_quantity[i] = Label(fr142, font = ("Arial", 15))
		results14_quantity[i].grid(row = i, column = 10)

	# Price
	results14_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results14_price[i] = Label(fr142, font = ("Arial", 15))
		results14_price[i].grid(row = i, column = 11)

	btn_first14 = Button(fr142, font = ("Arial", 15), relief = FLAT)
	btn_first14.grid(row = 11, column = 6)
	btn_prev14 = Button(fr142, font = ("Arial", 15), relief = FLAT)
	btn_prev14.grid(row = 11, column = 7)
	btn_next14 = Button(fr142, font = ("Arial", 15), relief = FLAT)
	btn_next14.grid(row = 11, column = 8)
	btn_end14 = Button(fr142, font = ("Arial", 15), relief = FLAT)
	btn_end14.grid(row = 11, column = 9)
	icon_page14 = Label(fr142, font = ("Arial", 15))
	icon_page14.grid(row = 11, column = 11)
	
	fr141.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr142.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def sell2trans14():
	x0 = scr14.winfo_x()
	y0 = scr14.winfo_y()
	scr14.destroy()
	scr013.deiconify()
	scr013.geometry("1200x700+%d+%d" %(x0, y0))

def reset14():
	day1_entry14.delete(0, END)
	month1_entry14.delete(0, END)
	day2_entry14.delete(0, END)
	month2_entry14.delete(0, END)
	icon_date141.configure(image = icon_bg14)
	icon_date142.configure(image = icon_bg14)
	icon_range14.configure(image = icon_bg14)
	text_results14.configure(text = "")
	for i in range(1, 11):
		results14[i].configure(text = "")
		results14_date[i].configure(text = "")
		results14_orderid[i].configure(text = "")
		results14_cusid[i].configure(text = "")
		results14_prodid[i].configure(text = "")
		results14_quantity[i].configure(text = "")
		results14_price[i].configure(text = "")
	btn_first14.configure(text = "", command = donothing)
	btn_prev14.configure(text = "", command = donothing)
	btn_next14.configure(text = "", command = donothing)
	btn_end14.configure(text = "", command = donothing)
	icon_page14.configure(text = "", relief = FLAT)

def search14():
	global numOfresults14
	global numOfpages14
	global page14
	global date141
	global orderid141
	global cusid141
	global prodid141
	global quantity141
	global price141

	day1410 = day1_entry14.get()
	month1410 = month1_entry14.get()
	day1420 = day2_entry14.get()
	month1420 = month2_entry14.get()

	# Check date1
	check_date1 = True
	flag1 = False
	if (day1410 == "" and month1410 != "") or (day1410 != "" and month1410 == ""):
		check_date1 = False
	elif (day1410 != "" and month1410 != ""):
		if (day1410.isdigit() == False or month1410.isdigit() == False):
			check_date1 = False
		else:
			d1410 = int(day1410)
			m1410 = int(month1410)
			flag1 = True
			if m1410 not in range(1, 13):
				check_date1 = False
				flag1 = False
			else:
				if m1410 in [1, 3, 5, 7, 8, 10, 12] and d1410 not in range(1, 32):
					check_date1 = False
					flag1 = False
				elif m1410 in [4, 6, 9, 11] and d1410 not in range(1, 31):
					check_date1 = False
					flag1 = False
				elif m1410 == 2 and d1410 not in range(1, 30):
					check_date1 = False
					flag1 = False
	
	if check_date1:
		icon_date141.configure(image = icon_true14)
	else:
		icon_date141.configure(image = icon_false14)

	# Check date2
	check_date2 = True
	flag2 = False
	if (day1420 == "" and month1420 != "") or (day1420 != "" and month1420 == ""):
		check_date2 = False
	elif (day1420 != "" and month1420 != ""):
		if (day1420.isdigit() == False or month1420.isdigit() == False):
			check_date2 = False
		else:
			d1420 = int(day1420)
			m1420 = int(month1420)
			flag2 = True
			if m1420 not in range(1, 13):
				check_date2 = False
				flag2 = False
			else:
				if m1420 in [1, 3, 5, 7, 8, 10, 12] and d1420 not in range(1, 32):
					check_date2 = False
					flag2 = False
				elif m1420 in [4, 6, 9, 11] and d1420 not in range(1, 31):
					check_date2 = False
					flag2 = False
				elif m1420 == 2 and d1420 not in range(1, 30):
					check_date2 = False
					flag2 = False
	
	if check_date2:
		icon_date142.configure(image = icon_true14)
	else:
		icon_date142.configure(image = icon_false14)

	# Check range
	check_range = flag1 and flag2
	if check_range:
		if m1410 > m1420:
			check_range = False
		elif m1410 == m1420 and d1410 > d1420:
			check_range = False

	if (day1410 == "" and month1410 == "") and flag2:
		check_range = True
	elif (day1420 == "" and month1420 == "") and flag1:
		check_range = True
	elif (day1410 == "" and month1410 == "") and (day1420 == "" and month1420 == ""):
		check_range = True
			
	if check_range:
		icon_range14.configure(image = icon_true14)
	else:
		icon_range14.configure(image = icon_false14)

	# All check are true	
	if check_date1 and check_date2 and check_range:
		file = open("hoadon_ban.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; date141 = []; day141 = []; month141 = []; orderid141 = []; cusid141 = []; prodid141 = []; quantity141 = []; price141 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			date141.append(sub[0].replace(".", " ", 10))
			sub2 = date141[i].split()
			day141.append(sub2[0])
			month141.append(sub2[1])
			orderid141.append(sub[1])
			cusid141.append(sub[2])
			prodid141.append(sub[3])
			quantity141.append(sub[4])
			price141.append(sub[5])

		date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		if flag1 and (day1420 == "" and month1420 == ""):
			for i in range(0, len(date141)):
				if (int(month141[i]) > m1410) or (int(month141[i]) == m1410 and int(day141[i]) >= d1410):
					date2.append(date141[i])
					day2.append(day141[i])
					month2.append(month141[i])
					orderid2.append(orderid141[i])
					cusid2.append(cusid141[i])
					prodid2.append(prodid141[i])
					quantity2.append(quantity141[i])
					price2.append(price141[i])
			date141 = date2; day141 = day2; month141 = month2; orderid141 = orderid2; cusid141 = cusid2; prodid141 = prodid2; quantity141 = quantity2; price141 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []
		
		elif (day1410 == "" and month1410 == "") and flag2:
			for i in range(0, len(date141)):
				if (int(month141[i]) < m1420) or (int(month141[i]) == m1420 and int(day141[i]) <= d1420):
					date2.append(date141[i])
					day2.append(day141[i])
					month2.append(month141[i])
					orderid2.append(orderid141[i])
					cusid2.append(cusid141[i])
					prodid2.append(prodid141[i])
					quantity2.append(quantity141[i])
					price2.append(price141[i])
			date141 = date2; day141 = day2; month141 = month2; orderid141 = orderid2; cusid141 = cusid2; prodid141 = prodid2; quantity141 = quantity2; price141 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		elif flag1 and flag2:
			for i in range(0, len(date141)):
				if (m1410 < int(month141[i]) < m1420) or (m1410 == int(month141[i]) < m1420 and int(day141[i]) >= d1410) or (m1410 < int(month141[i]) == m1420 and int(day141[i]) <= d1420) or (m1410 == int(month141[i]) == m1420 and d1410 <= int(day141[i]) <= d1420):
					date2.append(date141[i])
					day2.append(day141[i])
					month2.append(month141[i])
					orderid2.append(orderid141[i])
					cusid2.append(cusid141[i])
					prodid2.append(prodid141[i])
					quantity2.append(quantity141[i])
					price2.append(price141[i])
			date141 = date2; day141 = day2; month141 = month2; orderid141 = orderid2; cusid141 = cusid2; prodid141 = prodid2; quantity141 = quantity2; price141 = price2
			date2 = []; day2 = []; month2 = []; orderid2 = []; cusid2 = []; prodid2 = []; quantity2 = []; price2 = []

		# Sort
		for i in range(0, len(day141)):
			date141[i] = date141[i].replace(" ", "/", 10)

		# Show
		numOfresults14 = len(day141)
		if (numOfresults14 == 0) or (numOfresults14 == 1):
			text_results14.configure(text = "%d result found" %numOfresults14)
		else:
			text_results14.configure(text = "%d results found" %numOfresults14)

		if numOfresults14 != 0:
			numOfpages14 = ((numOfresults14 - 1) // 10) + 1
			btn_first14.configure(text = "1", command = first14)
			btn_prev14.configure(text = "<", command = prev14)
			btn_next14.configure(text = ">", command = next14)
			btn_end14.configure(text = "End", command = end14)
			page14 = 1
			showResults14(page14)
	else:
		text_results14.configure(text = "")
		for i in range(1, 11):
			results14[i].configure(text = "")
			results14_date[i].configure(text = "")
			results14_orderid[i].configure(text = "")
			results14_cusid[i].configure(text = "")
			results14_prodid[i].configure(text = "")
			results14_quantity[i].configure(text = "")
			results14_price[i].configure(text = "")

		btn_first14.configure(text = "", command = donothing)
		btn_prev14.configure(text = "", command = donothing)
		btn_next14.configure(text = "", command = donothing)
		btn_end14.configure(text = "", command = donothing)
		icon_page14.configure(text = "", relief = FLAT)

def showResults14(index):
	icon_page14.configure(text = index, relief = GROOVE)
	if index == numOfpages14:
		for i in range(1, numOfresults14 - 10*(numOfpages14 - 1) + 1):
			results14[i].configure(text = 10*(numOfpages14 - 1) + i)
			results14_date[i].configure(text = date141[10*(numOfpages14 - 1) + i - 1])
			results14_orderid[i].configure(text = orderid141[10*(numOfpages14 - 1) + i - 1])
			results14_cusid[i].configure(text = cusid141[10*(numOfpages14 - 1) + i - 1])
			results14_prodid[i].configure(text = prodid141[10*(numOfpages14 - 1) + i - 1])
			results14_quantity[i].configure(text = quantity141[10*(numOfpages14 - 1) + i - 1])
			results14_price[i].configure(text = price141[10*(numOfpages14 - 1) + i - 1])
		if (numOfresults14 % 10) != 0:
			for i in range((numOfresults14 % 10) + 1, 11):
				results14[i].configure(text = "")
				results14_date[i].configure(text = "")
				results14_orderid[i].configure(text = "")
				results14_cusid[i].configure(text = "")
				results14_prodid[i].configure(text = "")
				results14_quantity[i].configure(text = "")
				results14_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results14[j].configure(text = 10*(index - 1) + j)
			results14_date[j].configure(text = date141[10*(index - 1) + j - 1])
			results14_orderid[j].configure(text = orderid141[10*(index - 1) + j - 1])
			results14_cusid[j].configure(text = cusid141[10*(index - 1) + j - 1])
			results14_prodid[j].configure(text = prodid141[10*(index - 1) + j - 1])
			results14_quantity[j].configure(text = quantity141[10*(index - 1) + j - 1])
			results14_price[j].configure(text = price141[10*(index - 1) + j - 1])

# Buttons for showing results
def first14():
	global page14
	page14 = 1
	showResults14(page14)

def prev14():
	global page14
	if page14 != 1:
		page14 -= 1
		showResults14(page14)

def next14():
	global page14
	if page14 != numOfpages14:
		page14 += 1
		showResults14(page14)

def end14():
	global page14
	page14 = numOfpages14
	showResults14(page14)

# Revenue
def revenue1():
	global scr15
	global fr151
	global fr152
	global day1_entry15
	global month1_entry15
	global day2_entry15
	global month2_entry15
	global rs15
	global results15_expenditure
	global results15_sale
	global results15_revenue
	global icon_date151
	global icon_date152
	global icon_range15
	global icon_true15
	global icon_false15
	global icon_laugh15
	global icon_cry15
	global icon_laughcry15
	global icon_emotion15
	global icon_bg15
	global icon_emobg15
	global back15

	scr013.withdraw()
	scr15 = Toplevel(scr013)
	x0 = scr013.winfo_x()
	y0 = scr013.winfo_y()
	scr15.geometry("1200x700+%d+%d" %(x0, y0))
	scr15.title("Revenue")
	scr15.resizable(width = False, height = False)
	scr15.protocol("WM_DELETE_WINDOW", close)
	logo(scr15, 12)
	
	## Info
	fr = Frame(scr15)
	fr151 = Frame(fr)
	
	# SELL
	Label(fr151, text = "REVENUE", font = ("Tahoma", 20)).grid(row = 0, column = 1, columnspan = 3, sticky = W, padx = 10)
	Label(fr151).grid(row = 1)

	# Date
	Label(fr151, text = "Date", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	day1 = StringVar()
	day1_entry15 = Entry(fr151, textvariable = day1, width = 3, font = 30)
	day1_entry15.grid(row = 2, column = 1, sticky = W)

	Label(fr151, text = "/", font = ("Tahoma", 20)).grid(row = 2, column = 2, sticky = W)
	
	month1 = StringVar()
	month1_entry15 = Entry(fr151, textvariable = month1, width = 3, font = 30)
	month1_entry15.grid(row = 2, column = 3)

	Label(fr151, text = "to", font = ("Tahoma", 20)).grid(row = 3, column = 2, sticky = W)
	day2 = StringVar()
	day2_entry15 = Entry(fr151, textvariable = day2, width = 3, font = 30)
	day2_entry15.grid(row = 4, column = 1, sticky = W)

	Label(fr151, text = "/", font = ("Tahoma", 20)).grid(row = 4, column = 2, sticky = W)
	
	month2 = StringVar()
	month2_entry15 = Entry(fr151, textvariable = month2, width = 3, font = 30)
	month2_entry15.grid(row = 4, column = 3)

	# Reset
	Label(fr151).grid(row = 5)
	rs15 = PhotoImage(file = "reset.png")
	Button(fr151, image = rs15, relief = FLAT, command = reset15).grid(row = 6, column = 1, sticky = W)
	# scr15.bind("r", reset14)
	
	# CALCULATION
	Button(fr151, text = "CALC", font = ("Tahoma", 16), command = calc15).grid(row = 6, column = 2, columnspan = 2, sticky = E)
	scr15.bind("<Return>", search14)
	# Label(fr151).grid(row = 10)

	# Back to login
	back15 = PhotoImage(file = "left.png")
	Label(fr151).grid(row = 8)
	Label(fr151).grid(row = 9)
	Label(fr151).grid(row = 10)
	Label(fr151).grid(row = 11)
	Button(fr151, image = back15, relief = FLAT, command = rev2trans15).grid(row = 12, column = 0, pady = 30)

	# Check icons
	icon_true15 = PhotoImage(file = "true.png")
	icon_false15 = PhotoImage(file = "false.png")
	icon_bg15 =  PhotoImage(file = "bg.png")

	icon_date151 = Label(fr151, image = icon_bg15)
	icon_date151.grid(row = 2, column = 6, padx = 20)
	icon_date152 = Label(fr151, image = icon_bg15)
	icon_date152.grid(row = 4, column = 6, padx = 20)
	icon_range15 = Label(fr151, image = icon_bg15)
	icon_range15.grid(row = 3, column = 6, padx = 20)

	## Results
	fr152 = Frame(fr)
	Label(fr152).grid(row = 0)
	Label(fr152).grid(row = 1)
	Label(fr152, text = "Total expenditure", font = ("Tahoma", 20)).grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 10, sticky = W)
	Label(fr152).grid(row = 3)
	results15_expenditure = Label(fr152, font = ("Arial", 30))
	results15_expenditure.grid(row = 2, column = 3, columnspan = 3, padx = 20, pady = 10, sticky = W)

	Label(fr152, text = "Total sale", font = ("Tahoma", 20)).grid(row = 4, column = 0, columnspan = 3, padx = 20, pady = 10, sticky = W)
	Label(fr152).grid(row = 5)
	results15_sale = Label(fr152, font = ("Arial", 30))
	results15_sale.grid(row = 4, column = 3, columnspan = 3, padx = 20, pady = 10, sticky = W)

	Label(fr152, text = "Revenue", font = ("Tahoma", 20)).grid(row = 6, column = 0, columnspan = 3, padx = 20, pady = 10, sticky = W)
	Label(fr152).grid(row = 7)
	results15_revenue = Label(fr152, font = ("Arial", 40), fg = "red")
	results15_revenue.grid(row = 6, column = 3, columnspan = 3, padx = 20, pady = 10, sticky = W)

	# Emotion
	icon_laugh15 = PhotoImage(file = "laugh.png")
	icon_cry15 = PhotoImage(file = "cry.png")
	icon_laughcry15 = PhotoImage(file = "laughcry.png")
	icon_emobg15 = PhotoImage(file = "emo_bg.png")

	icon_emotion15 = Label(fr152, image = icon_emobg15)
	icon_emotion15.grid(row = 8, column = 3)

	fr151.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr152.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def rev2trans15():
	x0 = scr15.winfo_x()
	y0 = scr15.winfo_y()
	scr15.destroy()
	scr013.deiconify()
	scr013.geometry("1200x700+%d+%d" %(x0, y0))

def reset15():
	day1_entry15.delete(0, END)
	month1_entry15.delete(0, END)
	day2_entry15.delete(0, END)
	month2_entry15.delete(0, END)
	icon_date151.configure(image = icon_bg15)
	icon_date152.configure(image = icon_bg15)
	icon_range15.configure(image = icon_bg15)
	icon_emotion15.configure(image = icon_emobg15)
	results15_expenditure.configure(text = "")
	results15_sale.configure(text = "")
	results15_revenue.configure(text = "", relief = FLAT)

def calc15():
	day1510 = day1_entry15.get()
	month1510 = month1_entry15.get()
	day1520 = day2_entry15.get()
	month1520 = month2_entry15.get()

	# Check date1
	check_date1 = True
	flag1 = False
	if (day1510 == "" and month1510 != "") or (day1510 != "" and month1510 == ""):
		check_date1 = False
	elif (day1510 != "" and month1510 != ""):
		if (day1510.isdigit() == False or month1510.isdigit() == False):
			check_date1 = False
		else:
			d1510 = int(day1510)
			m1510 = int(month1510)
			flag1 = True
			if m1510 not in range(1, 13):
				check_date1 = False
				flag1 = False
			else:
				if m1510 in [1, 3, 5, 7, 8, 10, 12] and d1510 not in range(1, 32):
					check_date1 = False
					flag1 = False
				elif m1510 in [4, 6, 9, 11] and d1510 not in range(1, 31):
					check_date1 = False
					flag1 = False
				elif m1510 == 2 and d1510 not in range(1, 30):
					check_date1 = False
					flag1 = False
	
	if check_date1:
		icon_date151.configure(image = icon_true15)
	else:
		icon_date151.configure(image = icon_false15)

	# Check date2
	check_date2 = True
	flag2 = False
	if (day1520 == "" and month1520 != "") or (day1520 != "" and month1520 == ""):
		check_date2 = False
	elif (day1520 != "" and month1520 != ""):
		if (day1520.isdigit() == False or month1520.isdigit() == False):
			check_date2 = False
		else:
			d1520 = int(day1520)
			m1520 = int(month1520)
			flag2 = True
			if m1520 not in range(1, 13):
				check_date2 = False
				flag2 = False
			else:
				if m1520 in [1, 3, 5, 7, 8, 10, 12] and d1520 not in range(1, 32):
					check_date2 = False
					flag2 = False
				elif m1520 in [4, 6, 9, 11] and d1520 not in range(1, 31):
					check_date2 = False
					flag2 = False
				elif m1520 == 2 and d1520 not in range(1, 30):
					check_date2 = False
					flag2 = False
	
	if check_date2:
		icon_date152.configure(image = icon_true15)
	else:
		icon_date152.configure(image = icon_false15)

	# Check range
	check_range = flag1 and flag2
	if check_range:
		if m1510 > m1520:
			check_range = False
		elif m1510 == m1520 and d1510 > d1520:
			check_range = False

	if (day1510 == "" and month1510 == "") and flag2:
		check_range = True
	elif (day1520 == "" and month1520 == "") and flag1:
		check_range = True
	elif (day1510 == "" and month1510 == "") and (day1520 == "" and month1520 == ""):
		check_range = True
			
	if check_range:
		icon_range15.configure(image = icon_true15)
	else:
		icon_range15.configure(image = icon_false15)

	# All check are true	
	if check_date1 and check_date2 and check_range:
		# From hoadonmua
		file = open("hoadon_mua.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; date151 = []; day151 = []; month151 = []; quantity151 = []; price151 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			date151.append(sub[0].replace(".", " ", 10))
			sub2 = date151[i].split()
			day151.append(sub2[0])
			month151.append(sub2[1])
			quantity151.append(sub[4])
			price151.append(sub[5])

		date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		if flag1 and (day1520 == "" and month1520 == ""):
			for i in range(0, len(date151)):
				if (int(month151[i]) > m1510) or (int(month151[i]) == m1510 and int(day151[i]) >= d1510):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []
		
		elif (day1510 == "" and month1510 == "") and flag2:
			for i in range(0, len(date151)):
				if (int(month151[i]) < m1520) or (int(month151[i]) == m1520 and int(day151[i]) <= d1520):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		elif flag1 and flag2:
			for i in range(0, len(date151)):
				if (m1510 < int(month151[i]) < m1520) or (m1510 == int(month151[i]) < m1520 and int(day151[i]) >= d1510) or (m1510 < int(month151[i]) == m1520 and int(day151[i]) <= d1520) or (m1510 == int(month151[i]) == m1520 and d1510 <= int(day151[i]) <= d1520):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		expenditure = 0
		for i in range(0, len(day151)):
			expenditure += int(quantity151[i])*int(price151[i])
		results15_expenditure.configure(text = expenditure)

		# From hoadonban
		file = open("hoadon_ban.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; date151 = []; day151 = []; month151 = []; quantity151 = []; price151 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			date151.append(sub[0].replace(".", " ", 10))
			sub2 = date151[i].split()
			day151.append(sub2[0])
			month151.append(sub2[1])
			quantity151.append(sub[4])
			price151.append(sub[5])

		date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		if flag1 and (day1520 == "" and month1520 == ""):
			for i in range(0, len(date151)):
				if (int(month151[i]) > m1510) or (int(month151[i]) == m1510 and int(day151[i]) >= d1510):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []
		
		elif (day1510 == "" and month1510 == "") and flag2:
			for i in range(0, len(date151)):
				if (int(month151[i]) < m1520) or (int(month151[i]) == m1520 and int(day151[i]) <= d1520):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		elif flag1 and flag2:
			for i in range(0, len(date151)):
				if (m1510 < int(month151[i]) < m1520) or (m1510 == int(month151[i]) < m1520 and int(day151[i]) >= d1510) or (m1510 < int(month151[i]) == m1520 and int(day151[i]) <= d1520) or (m1510 == int(month151[i]) == m1520 and d1510 <= int(day151[i]) <= d1520):
					date2.append(date151[i])
					day2.append(day151[i])
					month2.append(month151[i])
					quantity2.append(quantity151[i])
					price2.append(price151[i])
			date151 = date2; day151 = day2; month151 = month2; quantity151 = quantity2; price151 = price2
			date2 = []; day2 = []; month2 = []; quantity2 = []; price2 = []

		sale = 0
		for i in range(0, len(day151)):
			sale += int(quantity151[i])*int(price151[i])
		results15_sale.configure(text = sale)

		# Revenue
		revenue = sale - expenditure
		results15_revenue.configure(text = revenue, relief = GROOVE)
		if revenue > 0:
			icon_emotion15.configure(image = icon_laugh15)
		elif revenue == 0:
			icon_emotion15.configure(image = icon_laughcry15)
		elif revenue < 0:
			icon_emotion15.configure(image = icon_cry15)
	else:
		results15_expenditure.configure(text = "")
		results15_sale.configure(text = "")
		results15_revenue.configure(text = "", relief = FLAT)
		icon_emotion15.configure(image = icon_emobg15)

###---------------------###
###-------EMPLOYEE----------###
###---------------------###

## CUSTOMER ##
def customer2(*arg):
	global scr21
	global fr211
	global fr212
	global name_entry21
	global phone_entry21
	global agemin_entry21
	global agemax_entry21
	global gender21
	global rs21
	global icon_name21
	global icon_phone21
	global icon_age21
	global icon_gender21
	global icon_true21
	global icon_false21
	global icon_notexist212
	global icon_bg21
	global results21
	global results21_name
	global results21_phone
	global results21_age
	global results21_gender
	global results21_price
	global btn_first21
	global btn_prev21
	global btn_next21
	global btn_end21
	global text_results21
	global back21
	global icon_page21

	scr02.withdraw()
	scr21 = Toplevel(scr02)
	x0 = scr02.winfo_x()
	y0 = scr02.winfo_y()
	scr21.geometry("1200x700+%d+%d" %(x0, y0))
	scr21.title("Customer")
	scr21.resizable(width = False, height = False)
	scr21.protocol("WM_DELETE_WINDOW", close)
	logo(scr21, 12)
	
	## Info
	fr = Frame(scr21)
	fr211 = Frame(fr)
	# Name
	Label(fr211, text = "Name", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr211).grid(row = 1)
	name21 = StringVar()
	name_entry21 = Entry(fr211, textvariable = name21, width = 20, font = 30)
	name_entry21.grid(row = 0, column = 1, columnspan = 3, sticky = W)
	
	# Phone
	Label(fr211, text = "Phone", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr211).grid(row = 3)
	phone21 = StringVar()
	phone_entry21 = Entry(fr211, textvariable = phone21, width = 20, font = 30)
	phone_entry21.grid(row = 2, column = 1, columnspan = 3, sticky = W)

	# Age
	Label(fr211, text = "Age", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr211).grid(row = 5)
	agemin21 = StringVar()
	agemin_entry21 = Entry(fr211, textvariable = agemin21, width = 5, font = 30)
	agemin_entry21.grid(row = 4, column = 1, sticky = W)

	Label(fr211, text = "-", font = ("Tahoma", 20)).grid(row = 4, column = 2)
	
	agemax21 = StringVar()
	agemax_entry21 = Entry(fr211, textvariable = agemax21, width = 5, font = 30)
	agemax_entry21.grid(row = 4, column = 3, sticky = E)

	# Gender
	Label(fr211, text = "Gender", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr211).grid(row = 7)
	gender21 = StringVar()
	OptionMenu(fr211, gender21, "All", "Male", "Female").grid(row = 6, column = 1, columnspan = 2, sticky = W)
	# Radiobutton(fr211, text = "All", font = 14, variable = gender21, value = 3).grid(row = 6, column = 1, sticky = W)
	# Radiobutton(fr211, text = "Male", font = 14, variable = gender21, value = 1).grid(row = 7, column = 1, sticky = W)
	# Radiobutton(fr211, text = "Female", font = 14, variable = gender21, value = 2).grid(row = 8, column = 1, sticky = W)
	gender21.set("All")

	# Reset
	rs21 = PhotoImage(file = "reset.png")
	Button(fr211, image = rs21, relief = FLAT, command = reset21).grid(row = 9, column = 1, sticky = W)
	# scr21.bind("r", reset)
	
	# SEARCH
	Button(fr211, text = "SEARCH", font = ("Tahoma", 16), command = search21).grid(row = 9, column = 2, columnspan = 2, sticky = E)
	scr21.bind("<Return>", search21)
	Label(fr211).grid(row = 10)

	# ADD
	Button(fr211, text = "UPDATE", font = ("Tahoma", 16), command = update21).grid(row = 10, column = 1, columnspan = 2, sticky = W)

	# DELETE
	Button(fr211, text = "DELETE", font = ("Tahoma", 16), command = delete21).grid(row = 10, column = 3, sticky = E)

	text_results21 = Label(fr211, font = ("Arial", 15))
	text_results21.grid(row = 11, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back21 = PhotoImage(file = "left.png")
	Label(fr211).grid(row = 12)
	Button(fr211, image = back21, relief = FLAT, command = cus2log21).grid(row = 13, column = 0)

	# Check icons
	icon_true21 = PhotoImage(file = "true.png")
	icon_false21 = PhotoImage(file = "false.png")
	icon_notexist212 = PhotoImage(file = "notexist2.png")
	icon_bg21 =  PhotoImage(file = "bg.png")

	icon_name21 = Label(fr211, image = icon_bg21)
	icon_name21.grid(row = 0, column = 4, padx = 20)
	icon_phone21 = Label(fr211, image = icon_bg21)
	icon_phone21.grid(row = 2, column = 4, padx = 20)
	icon_age21 = Label(fr211, image = icon_bg21)
	icon_age21.grid(row = 4, column = 4, padx = 20)
	icon_gender21 = Label(fr211, image = icon_bg21)
	icon_gender21.grid(row = 6, column = 4, padx = 20)

	## Results
	fr212 = Frame(fr)
	Label(fr212, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr212, text = "Name", font = ("Tahoma", 20)).grid(row = 0, column = 6, columnspan = 2, padx = 50)
	Label(fr212, text = "Phone", font = ("Tahoma", 20)).grid(row = 0, column = 8, columnspan = 2, padx = 40)
	Label(fr212, text = "Age", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 20)
	Label(fr212, text = "Gen.", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	Label(fr212, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 12, padx = 20)
	
	# No.
	results21 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21[i] = Label(fr212, font = ("Tahoma", 20))
		results21[i].grid(row = i, column = 5)

	# Name
	results21_name = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21_name[i] = Label(fr212, font = ("Arial", 15))
		results21_name[i].grid(row = i, column = 6, columnspan = 2)

	# Phone
	results21_phone = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21_phone[i] = Label(fr212, font = ("Arial", 15))
		results21_phone[i].grid(row = i, column = 8, columnspan = 2)
	# Age
	results21_age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21_age[i] = Label(fr212, font = ("Arial", 15))
		results21_age[i].grid(row = i, column = 10)

	# Gender
	results21_gender = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21_gender[i] = Label(fr212, font = ("Arial", 15))
		results21_gender[i].grid(row = i, column = 11)

	# Price
	results21_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results21_price[i] = Label(fr212, font = ("Arial", 15))
		results21_price[i].grid(row = i, column = 12)
		
	btn_first21 = Button(fr212, font = ("Arial", 15), relief = FLAT)
	btn_first21.grid(row = 11, column = 6)
	btn_prev21 = Button(fr212, font = ("Arial", 15), relief = FLAT)
	btn_prev21.grid(row = 11, column = 7)
	btn_next21 = Button(fr212, font = ("Arial", 15), relief = FLAT)
	btn_next21.grid(row = 11, column = 8)
	btn_end21 = Button(fr212, font = ("Arial", 15), relief = FLAT)
	btn_end21.grid(row = 11, column = 9)
	icon_page21 = Label(fr212, font = ("Arial", 15))
	icon_page21.grid(row = 11, column = 12)
	
	fr211.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr212.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def cus2log21():
	x0 = scr21.winfo_x()
	y0 = scr21.winfo_y()
	scr21.destroy()
	scr02.deiconify()
	scr02.geometry("1200x700+%d+%d" %(x0, y0))

def reset21(*arg):
	name_entry21.delete(0, END)
	phone_entry21.delete(0, END)
	agemin_entry21.delete(0, END)
	agemax_entry21.delete(0, END)
	gender21.set("All")
	icon_name21.configure(image = icon_bg21)
	icon_phone21.configure(image = icon_bg21)
	icon_age21.configure(image = icon_bg21)
	text_results21.configure(text = "")
	for i in range(1, 11):
		results21[i].configure(text = "")
		results21_name[i].configure(text = "")
		results21_phone[i].configure(text = "")
		results21_age[i].configure(text = "")
		results21_gender[i].configure(text = "")
		results21_price[i].configure(text = "")
	btn_first21.configure(text = "", command = donothing)
	btn_prev21.configure(text = "", command = donothing)
	btn_next21.configure(text = "", command = donothing)
	btn_end21.configure(text = "", command = donothing)
	icon_page21.configure(text = "", relief = FLAT)

def search21(*arg):
	global numOfresults21
	global numOfpages21
	global page21
	global name211
	global phone211
	global age211
	global gender211
	global price211
	
	file = open("customer.txt")
	lines = sum(1 for line in file)
	file.seek(0)
	data = []; name211 = []; phone211 = []; age211 = []; gender211 = []; price211 = []
	for i in range(0, lines):
		data.append(file.readline()) 
	file.close()

	for i in range(0, lines):
		sub = data[i].split()
		name211.append(sub[0])
		phone211.append(sub[1])
		age211.append(sub[2])
		gender211.append(sub[3])
		price211.append(sub[4])

	name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []	
	for i in range(0, len(name211)):
		if name211[i] == "x":
			name2.append(name211[i])
			phone2.append(phone211[i])
			age2.append(age211[i])
			gender2.append(gender211[i])
			price2.append(price211[i])
	name211 = name2; phone211 = phone2; age211 = age2; gender211 = gender2; price211 = price2
	name2 = []; phone2 = []; age2 = []; gender2 = []; price2 = []

	numOfresults21 = len(name211)
	if (numOfresults21 == 0) or (numOfresults21 == 1):
		text_results21.configure(text = "%d result found" %numOfresults21)
	else:
		text_results21.configure(text = "%d results found" %numOfresults21)
	if numOfresults21 == 0:
		for i in range(1, 11):
			results21[i].configure(text = "")
			results21_name[i].configure(text = "")
			results21_phone[i].configure(text = "")
			results21_age[i].configure(text = "")
			results21_gender[i].configure(text = "")
			results21_price[i].configure(text = "")
	else:
		numOfpages21 = ((numOfresults21 - 1) // 10) + 1
		btn_first21.configure(text = "1", command = first21)
		btn_prev21.configure(text = "<", command = prev21)
		btn_next21.configure(text = ">", command = next21)
		btn_end21.configure(text = "End", command = end21)
		page21 = 1
		showResults21(page21)

def showResults21(index):
	icon_page21.configure(text = index, relief = GROOVE)
	if index == numOfpages21:
		for i in range(1, numOfresults21 - 10*(numOfpages21 - 1) + 1):
			results21[i].configure(text = 10*(numOfpages21 - 1) + i)
			results21_name[i].configure(text = name211[10*(numOfpages21 - 1) + i - 1])
			results21_phone[i].configure(text = phone211[10*(numOfpages21 - 1) + i - 1])
			results21_age[i].configure(text = age211[10*(numOfpages21 - 1) + i - 1])
			results21_gender[i].configure(text = gender211[10*(numOfpages21 - 1) + i - 1])
			results21_price[i].configure(text = price211[10*(numOfpages21 - 1) + i - 1])
		if (numOfresults21 % 10) != 0:
			for i in range((numOfresults21 % 10) + 1, 11):
				results21[i].configure(text = "")
				results21_name[i].configure(text = "")
				results21_phone[i].configure(text = "")
				results21_age[i].configure(text = "")
				results21_gender[i].configure(text = "")
				results21_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results21[j].configure(text = 10*(index - 1) + j)
			results21_name[j].configure(text = name211[10*(index - 1) + j - 1])
			results21_phone[j].configure(text = phone211[10*(index - 1) + j - 1])
			results21_age[j].configure(text = age211[10*(index - 1) + j - 1])
			results21_gender[j].configure(text = gender211[10*(index - 1) + j - 1])
			results21_price[j].configure(text = price211[10*(index - 1) + j - 1])

# Buttons for showing results
def first21():
	global page21
	page21 = 1
	showResults21(page21)

def prev21():
	global page21
	if page21 != 1:
		page21 -= 1
		showResults21(page21)

def next21():
	global page21
	if page21 != numOfpages21:
		page21 += 1
		showResults21(page21)

def end21():
	global page21
	page21 = numOfpages21
	showResults21(page21)

# UPDATE
def update21():
	name210 = name_entry21.get()
	phone210 = phone_entry21.get()
	agemin210 = agemin_entry21.get()
	agemax210 = agemax_entry21.get()
	gender210 = gender21.get()

	btn_first21.configure(text = "", command = donothing)
	btn_prev21.configure(text = "", command = donothing)
	btn_next21.configure(text = "", command = donothing)
	btn_end21.configure(text = "", command = donothing)
	icon_page21.configure(text = "", relief = FLAT)

	# Check name
	check_name = True
	if name210 == "":
		check_name = False
	else:
		name210 = name210.upper()  # Capitalize all letters11 of name
		for i in range (0, len(name210)):
			if (ord(name210[i]) != 32) and ((ord(name210[i]) < 65) or (ord(name210[i]) > 90)):
				check_name = False
	
	if check_name:
		icon_name21.configure(image = icon_true21)
	else:
		icon_name21.configure(image = icon_false21)

	# Check phone
	check_phone = True
	if phone210 == "":
		check_phone = False
	else:
		check_phone = phone210.isdigit()
	
	f_phone = False
	if check_phone:
		f_phone = True
		file = open("customer.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; name211 = []; phone211 = []; price211 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			name211.append(sub[0])
			phone211.append(sub[1])
			price211.append(sub[4])

		name2 = []; phone2 = []; price2 = []	
		for i in range(0, len(name211)):
			if name211[i] == "x":
				name2.append(name211[i])
				phone2.append(phone211[i])
				price2.append(price211[i])
		name211 = name2; phone211 = phone2; price211 = price2
		name2 = []; phone2 = []; price2 = []

		for i in range(0, len(phone211)):
			if phone211[i] == phone210:
				name2.append(name211[i])
				phone2.append(phone211[i])
				price2.append(price211[i])
				price210 = price211[i]
		name211 = name2; phone211 = phone2; price211 = price2
		name2 = []; phone2 = []; price2 = []

		if len(name211) > 0:
			icon_phone21.configure(image = icon_true21)
		else:
			f_phone = False
			icon_phone21.configure(image = icon_notexist212)
	else:
		icon_phone21.configure(image = icon_false21)

	# Check age
	check_age = True
	if agemin210 == "" or agemax210 == "":
		check_age = False
	else:
		check_age = agemin210.isdigit() and agemax210.isdigit() and agemin210 == agemax210

	if check_age:
		icon_age21.configure(image = icon_true21)
	else:
		icon_age21.configure(image = icon_false21)

	# Check gender
	check_gender = True
	if gender210 == "All":
		check_gender = False
	elif gender210 == "Male":
		check_gender = True
		gender210 = "M"
	elif gender210 == "Female":
		check_gender = True
		gender210 = "F"

	if check_gender:
		icon_gender21.configure(image = icon_true21)
	else:
		icon_gender21.configure(image = icon_false21)

	# All checks are true
	if check_name and f_phone and check_age and check_gender:
		text_results21.configure(text = "1 result found")
		results21[1].configure(text = "1")
		results21_name[1].configure(text = "x")
		results21_phone[1].configure(text = phone210)
		results21_age[1].configure(text = "0")
		results21_gender[1].configure(text = "x")
		results21_price[1].configure(text = price210)
		for i in range(2, 11):
			results21[i].configure(text = "")
			results21_name[i].configure(text = "")
			results21_phone[i].configure(text = "")
			results21_age[i].configure(text = "")
			results21_gender[i].configure(text = "")
			results21_price[i].configure(text = "")

		file = open("customer.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; name212 = []; phone212 = []; age212 = []; gender212 = []; price212 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			name212.append(sub[0])
			phone212.append(sub[1])
			age212.append(sub[2])
			gender212.append(sub[3])
			price212.append(sub[4])

		for i in range(0, len(phone212)):
			if phone212[i] == phone210:
				name210 = name210.upper()
				name210 = name210.replace(" ", ".", 10)
				data[i] = name210 + " " + phone210 + " " + agemin210 + " " + gender210 + " " + price210 + "\n"
				break
		if messagebox.askquestion("Shop BK", "Do you really want to update this customer?") == 'yes':
			file = open("customer.txt", "r+")
			file.writelines(["%s" %item for item in data])
			file.close()

			# Show
			name210 = name210.lower()
			name210 = name210.replace(".", " ", 10)
			name210 = name210.title()
			results21_name[1].configure(text = name210)
			results21_phone[1].configure(text = phone210)
			results21_age[1].configure(text = agemin210)
			results21_gender[1].configure(text = gender210)
			results21_price[1].configure(text = price210)
	else:
		text_results21.configure(text = "")
		for i in range(1, 11):
			results21[i].configure(text = "")
			results21_name[i].configure(text = "")
			results21_phone[i].configure(text = "")
			results21_age[i].configure(text = "")
			results21_gender[i].configure(text = "")
			results21_price[i].configure(text = "")
			
def delete21():
	btn_first21.configure(text = "", command = donothing)
	btn_prev21.configure(text = "", command = donothing)
	btn_next21.configure(text = "", command = donothing)
	btn_end21.configure(text = "", command = donothing)
	icon_page21.configure(text = "", relief = FLAT)

	icon_name21.configure(image = icon_bg21)
	icon_age21.configure(image = icon_bg21)
	icon_gender21.configure(image = icon_bg21)
	phone210 = phone_entry21.get()
	# Check phone
	check_phone = True
	if phone210 == "":
		check_phone = False
	else:
		check_phone = phone210.isdigit()

	f_phone = False
	if check_phone:
		f_phone = True
		file = open("customer.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; phone211 = []; sub2 = ""; name211 = ""; age211 = ""; gender = ""; price211 = "" 
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			phone211.append(sub[1])
		
		for i in range(0, len(phone211)):
			if phone211[i] == phone210:
				sub2 = data[i]
				sub3 = sub2.split()
				name211 = sub3[0]
				phone211 = sub3[1]
				age211 = sub3[2]
				gender211 = sub3[3]
				price211 = sub3[4]
				break

		if sub2 != "":
			icon_phone21.configure(image = icon_true21)
			data.remove(sub2)
		else:
			f_phone = False
			icon_phone21.configure(image = icon_notexist212)
	else:
		icon_phone21.configure(image = icon_false21)

	if f_phone:
		text_results21.configure(text = "1 result found")
		results21[1].configure(text = "1")
		results21_name[1].configure(text = name211)
		results21_phone[1].configure(text = phone211)
		results21_age[1].configure(text = age211)
		results21_gender[1].configure(text = gender211)
		results21_price[1].configure(text = price211)

		print(data)
		if messagebox.askquestion("Shop BK", "Do you really want to delete this customer?") == 'yes':
			file = open("customer.txt", "w")
			file.writelines(["%s" %item for item in data])
			file.close()

			# Show
			text_results21.configure(text = "")
			icon_phone21.configure(image = icon_bg21)
			results21[1].configure(text = "")
			results21_name[1].configure(text = "")
			results21_phone[1].configure(text = "")
			results21_age[1].configure(text = "")
			results21_gender[1].configure(text = "")
			results21_price[1].configure(text = "")
	else:
		text_results21.configure(text = "")
		for i in range(1, 11):
			results21[i].configure(text = "")
			results21_name[i].configure(text = "")
			results21_phone[i].configure(text = "")
			results21_age[i].configure(text = "")
			results21_gender[i].configure(text = "")
			results21_price[i].configure(text = "")

## PRODUCT ##
def product2(*arg):
	global scr22
	global fr221
	global fr222
	global id_entry22
	global type_entry22
	global size_entry22
	global brand_entry22
	global rs22
	global icon_id22
	global icon_type22
	global icon_size22
	global icon_brand22
	global icon_price22
	global icon_true22
	global icon_false22
	global icon_notexist222
	global icon_bg22
	global results22
	global results22_id
	global results22_type
	global results22_size
	global results22_brand
	global results22_quantity
	global results22_price
	global btn_first22
	global btn_prev22
	global btn_next22
	global btn_end22
	global text_results22
	global icon_page22
	global back22

	scr02.withdraw()
	scr22 = Toplevel(scr02)
	x0 = scr02.winfo_x()
	y0 = scr02.winfo_y()
	scr22.geometry("1200x700+%d+%d" %(x0, y0))
	scr22.title("Product")
	scr22.resizable(width = False, height = False)
	scr22.protocol("WM_DELETE_WINDOW", close)
	logo(scr22, 12)

	## Info
	fr = Frame(scr22)
	fr221 = Frame(fr)

	# ID
	Label(fr221, text = "ID", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr221).grid(row = 1)
	id22 = StringVar()
	id_entry22 = Entry(fr221, textvariable = id22, width = 20, font = 30)
	id_entry22.grid(row = 0, column = 1, columnspan = 3, sticky = W)
	
	# Type
	Label(fr221, text = "Type", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr221).grid(row = 3)
	type22 = StringVar()
	type_entry22 = Entry(fr221, textvariable = type22, width = 20, font = 30)
	type_entry22.grid(row = 2, column = 1, columnspan = 3, sticky = W)

	# Size
	Label(fr221, text = "Size", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr221).grid(row = 5)
	size22 = StringVar()
	size_entry22 = Entry(fr221, textvariable = size22, width = 20, font = 30)
	size_entry22.grid(row = 4, column = 1, columnspan = 3, sticky = W)

	# Brand
	Label(fr221, text = "Brand", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr221).grid(row = 7)
	brand22 = StringVar()
	brand_entry22 = Entry(fr221, textvariable = brand22, width = 20, font = 30)
	brand_entry22.grid(row = 6, column = 1, columnspan = 3, sticky = W)

	# Reset
	rs22 = PhotoImage(file = "reset.png")
	Button(fr221, image = rs22, relief = FLAT, command = reset22).grid(row = 8, column = 1, sticky = W)
	# scr22.bind("F1", reset)

	# SEARCH
	Button(fr221, text = "SEARCH", font = ("Tahoma", 16), command = search22).grid(row = 8, column = 2, columnspan = 2, sticky = E)
	scr22.bind("<Return>", search22)

	# UPDATE
	Button(fr221, text = "UPDATE", font = ("Tahoma", 16), command = update22).grid(row = 9, column = 1, columnspan = 2, sticky = W)

	# DELETE
	Button(fr221, text = "DELETE", font = ("Tahoma", 16), command = delete22).grid(row = 9, column = 3, sticky = E)

	text_results22 = Label(fr221, font = ("Arial", 15))
	text_results22.grid(row = 10, column = 1, columnspan = 4, sticky = W)

	# Back to login
	back22 = PhotoImage(file = "left.png")
	Button(fr221, image = back22, relief = FLAT, command = pro2log22).grid(row = 11, column = 0)

	# Check icons
	icon_true22 = PhotoImage(file = "true.png")
	icon_false22 = PhotoImage(file = "false.png")
	icon_notexist222 = PhotoImage(file = "notexist2.png")
	icon_bg22 =  PhotoImage(file = "bg.png")

	icon_id22 = Label(fr221, image = icon_bg22)
	icon_id22.grid(row = 0, column = 4, padx = 20)
	icon_type22 = Label(fr221, image = icon_bg22)
	icon_type22.grid(row = 2, column = 4, padx = 20)
	icon_size22 = Label(fr221, image = icon_bg22)
	icon_size22.grid(row = 4, column = 4, padx = 20)
	icon_brand22 = Label(fr221, image = icon_bg22)
	icon_brand22.grid(row = 6, column = 4, padx = 20)
	icon_price22 = Label(fr221, image = icon_bg22)
	icon_price22.grid(row = 8, column = 4, padx = 20)

	## Results
	fr222 = Frame(fr)
	Label(fr222, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 20)
	Label(fr222, text = "ID", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 20)
	Label(fr222, text = "Type", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 20)
	Label(fr222, text = "Size", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 20)
	Label(fr222, text = "Brand", font = ("Tahoma", 20)).grid(row = 0, column = 9, columnspan = 2, padx = 20)
	Label(fr222, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 20)
	Label(fr222, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 12, padx = 20)
	
	# No.
	results22 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22[i] = Label(fr222, font = ("Tahoma", 20))
		results22[i].grid(row = i, column = 5)

	# ID
	results22_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_id[i] = Label(fr222, font = ("Arial", 15))
		results22_id[i].grid(row = i, column = 6)

	# Type
	results22_type = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_type[i] = Label(fr222, font = ("Arial", 15))
		results22_type[i].grid(row = i, column = 7)

	# Size
	results22_size = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_size[i] = Label(fr222, font = ("Arial", 15))
		results22_size[i].grid(row = i, column = 8)

	# Brand
	results22_brand = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_brand[i] = Label(fr222, font = ("Arial", 15))
		results22_brand[i].grid(row = i, column = 9, columnspan = 2)

	# Quantity
	results22_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_quantity[i] = Label(fr222, font = ("Arial", 15))
		results22_quantity[i].grid(row = i, column = 11)

	# Price
	results22_price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for i in range(1, 11):
		results22_price[i] = Label(fr222, font = ("Arial", 15))
		results22_price[i].grid(row = i, column = 12)

	btn_first22 = Button(fr222, font = ("Arial", 15), relief = FLAT)
	btn_first22.grid(row = 11, column = 6)
	btn_prev22 = Button(fr222, font = ("Arial", 15), relief = FLAT)
	btn_prev22.grid(row = 11, column = 7)
	btn_next22 = Button(fr222, font = ("Arial", 15), relief = FLAT)
	btn_next22.grid(row = 11, column = 8)
	btn_end22 = Button(fr222, font = ("Arial", 15), relief = FLAT)
	btn_end22.grid(row = 11, column = 9)
	icon_page22 = Label(fr222, font = ("Arial", 15))
	icon_page22.grid(row = 11, column = 12)
	
	fr221.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr222.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def pro2log22():
	x0 = scr22.winfo_x()
	y0 = scr22.winfo_y()
	scr22.destroy()
	scr02.deiconify()
	scr02.geometry("1200x700+%d+%d" %(x0, y0))

def reset22():
	id_entry22.delete(0, END)
	type_entry22.delete(0, END)
	size_entry22.delete(0, END)
	brand_entry22.delete(0, END)
	icon_id22.configure(image = icon_bg22)
	icon_type22.configure(image = icon_bg22)
	icon_size22.configure(image = icon_bg22)
	icon_brand22.configure(image = icon_bg22)
	icon_price22.configure(image = icon_bg22)
	text_results22.configure(text = "")

	for i in range(1, 11):
		results22[i].configure(text = "")
		results22_id[i].configure(text = "")
		results22_type[i].configure(text = "")
		results22_size[i].configure(text = "")
		results22_brand[i].configure(text = "")
		results22_quantity[i].configure(text = "")
		results22_price[i].configure(text = "")

	btn_first22.configure(text = "", command = donothing)
	btn_prev22.configure(text = "", command = donothing)
	btn_next22.configure(text = "", command = donothing)
	btn_end22.configure(text = "", command = donothing)
	icon_page22.configure(text = "", relief = FLAT)

def search22(*arg):
	global numOfresults22
	global numOfpages22
	global page22
	global id221
	global type221
	global size221
	global brand221
	global quantity221
	global price221
	
	file = open("product.txt")
	lines = sum(1 for line in file)
	file.seek(0)
	data = []; id221 = []; type221 = []; size221 = []; brand221 = []; quantity221 = []; price221 = []
	for i in range(0, lines):
		data.append(file.readline()) 
	file.close()

	for i in range(0, lines):
		sub = data[i].split()
		id221.append(sub[0])
		type221.append(sub[1])
		size221.append(sub[2])
		brand221.append(sub[3])
		quantity221.append(sub[4])
		price221.append(sub[5])

	id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []	
	for i in range(0, len(type221)):
		if type221[i] == "x":
			id2.append(id221[i])
			type2.append(type221[i])
			size2.append(size221[i])
			brand2.append(brand221[i])
			quantity2.append(quantity221[i])
			price2.append(price221[i])
	id221 = id2; type221 = type2; size221 = size2; brand221 = brand2; quantity221 = quantity2; price221 = price2
	id2 = []; type2 = []; size2 = []; brand2 = []; quantity2 = []; price2 = []

	numOfresults22 = len(type221)
	if (numOfresults22 == 0) or (numOfresults22 == 1):
		text_results22.configure(text = "%d result found" %numOfresults22)
	else:
		text_results22.configure(text = "%d results found" %numOfresults22)
	if numOfresults22 == 0:
		for i in range(1, 11):
			results22[i].configure(text = "")
			results22_id[i].configure(text = "")
			results22_type[i].configure(text = "")
			results22_size[i].configure(text = "")
			results22_brand[i].configure(text = "")
			results22_quantity[i].configure(text = "")
			results22_price[i].configure(text = "")
	else:
		numOfpages22 = ((numOfresults22 - 1) // 10) + 1
		btn_first22.configure(text = "1", command = first22)
		btn_prev22.configure(text = "<", command = prev22)
		btn_next22.configure(text = ">", command = next22)
		btn_end22.configure(text = "End", command = end22)
		page22 = 1
		showResults22(page22)

def showResults22(index):
	icon_page22.configure(text = index, relief = GROOVE)
	if index == numOfpages22:
		for i in range(1, numOfresults22 - 10*(numOfpages22 - 1) + 1):
			results22[i].configure(text = 10*(numOfpages22 - 1) + i)
			results22_id[i].configure(text = id221[10*(numOfpages22 - 1) + i - 1])
			results22_type[i].configure(text = type221[10*(numOfpages22 - 1) + i - 1])
			results22_size[i].configure(text = size221[10*(numOfpages22 - 1) + i - 1])
			results22_brand[i].configure(text = brand221[10*(numOfpages22 - 1) + i - 1])
			results22_quantity[i].configure(text = quantity221[10*(numOfpages22 - 1) + i - 1])
			results22_price[i].configure(text = price221[10*(numOfpages22 - 1) + i - 1])
		if (numOfresults22 % 10) != 0:
			for i in range((numOfresults22 % 10) + 1, 11):
				results22[i].configure(text = "")
				results22_id[i].configure(text = "")
				results22_type[i].configure(text = "")
				results22_size[i].configure(text = "")
				results22_brand[i].configure(text = "")
				results22_quantity[i].configure(text = "")
				results22_price[i].configure(text = "")
	else:
		for j in range(1, 11):
			results22[j].configure(text = 10*(index - 1) + j)
			results22_id[j].configure(text = id221[10*(index - 1) + j - 1])
			results22_type[j].configure(text = type221[10*(index - 1) + j - 1])
			results22_size[j].configure(text = size221[10*(index - 1) + j - 1])
			results22_brand[j].configure(text = brand221[10*(index - 1) + j - 1])
			results22_quantity[j].configure(text = quantity221[10*(index - 1) + j - 1])
			results22_price[j].configure(text = price221[10*(index - 1) + j - 1])

# Button for showing results
def first22():
	global page22
	page22 = 1
	showResults22(page22)

def prev22():
	global page22
	if page22 != 1:
		page22 -= 1
		showResults22(page22)

def next22():
	global page22
	if page22 != numOfpages22:
		page22 += 1
		showResults22(page22)

def end22():
	global page22
	page22 = numOfpages22
	showResults22(page22)

# UPDATE
def update22():
	id220 = id_entry22.get()
	type220 = type_entry22.get()
	size220 = size_entry22.get()
	brand220 = brand_entry22.get()

	btn_first22.configure(text = "", command = donothing)
	btn_prev22.configure(text = "", command = donothing)
	btn_next22.configure(text = "", command = donothing)
	btn_end22.configure(text = "", command = donothing)
	icon_page22.configure(text = "", relief = FLAT)

	# Check ID
	check_id = True
	if id220 == "":
		check_id = False
	else:
		check_id = id220.isdigit()
	
	f_id = False
	if check_id:
		f_id = True
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id221 = []; type221 = []; quantity221 = []; price221 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			id221.append(sub[0])
			type221.append(sub[1])
			quantity221.append(sub[4])
			price221.append(sub[5])
		id2 = []; type2 = []; quantity2 = []; price2 = []
		for i in range(0, len(id221)):
			if type221[i] == "x":
				id2.append(id221[i])
				type2.append(type221[i])
				quantity2.append(quantity221[i])
				price2.append(price221[i])
		id221 = id2; type221 = type2; quantity221 = quantity2; price221 = price2
		id2 = []; type2 = []; quantity2 = []; price2 = []

		for i in range(0, len(id221)):
			if id221[i] == id220:
				id2.append(id221[i])
				type2.append(type221[i])
				quantity2.append(quantity221[i])
				price2.append(price221[i])
				quantity220 = quantity221[i]
				price220 = price221[i]
		id221 = id2; type221 = type2; quantity221 = quantity2; price221 = price2
		id2 = []; type2 = []; quantity2 = []; price2 = []

		if len(id221) > 0:
			icon_id22.configure(image = icon_true22)
		else:
			f_id = False
			icon_id22.configure(image = icon_notexist222)
	else:
		icon_id22.configure(image = icon_false22)

	# Check type
	check_type = True
	if type220 == "":
		check_type = False
	else:
		type220 = type220.upper()  # Capitalize all letters of name
		for i in range (0, len(type220)):
			if (ord(type220[i]) != 32) and ((ord(type220[i]) < 65) or (ord(type220[i]) > 90)):
				check_type = False

	if check_type:
		icon_type22.configure(image = icon_true22)
	else:
		icon_type22.configure(image = icon_false22)

	# Check size
	check_size = True
	if size220 == "":
		check_size = False
	else:
		check_size = size220.isdigit()

	if check_size:
		icon_size22.configure(image = icon_true22)
	else:
		icon_size22.configure(image = icon_false22)

	# Check brand
	check_brand = True
	if brand220 == "":
		check_brand = False
	
	if check_brand:
		icon_brand22.configure(image = icon_true22)
	else:
		icon_brand22.configure(image = icon_false22)

	# All checks are true 
	if f_id and check_type and check_size and check_brand:
		text_results22.configure(text = "1 result found")
		results22[1].configure(text = "1")
		results22_id[1].configure(text = id220)
		results22_type[1].configure(text = "x")
		results22_size[1].configure(text = "0")
		results22_brand[1].configure(text = "x")
		results22_quantity[1].configure(text = quantity220)
		results22_price[1].configure(text = price220)
		for i in range(2, 11):
			results22[i].configure(text = "")
			results22_id[i].configure(text = "")
			results22_type[i].configure(text = "")
			results22_size[i].configure(text = "")
			results22_brand[i].configure(text = "")
			results22_quantity[i].configure(text = "")
			results22_price[i].configure(text = "")

		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id222 = []; type222 = []; size222 = []; brand222 = []; quantity222 = []; price222 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			id222.append(sub[0])
			type222.append(sub[1])
			size222.append(sub[2])
			brand222.append(sub[3])
			quantity222.append(sub[4])
			price222.append(sub[5])

		for i in range(0, len(id222)):
			if id222[i] == id220:
				type220 = type220.upper()
				type220 = type220.replace(" ", ".", 10)
				brand220 = brand220.upper()
				brand220 = brand220.replace(" ", ".", 10)
				data[i] = id220 + " " + type220 + " " + size220 + " " + brand220 + " " + quantity220 + " " + price220 + "\n"
				break

		if messagebox.askquestion("Shop BK", "Do you really want to update this product's info?") == 'yes':
			file = open("product.txt", "r+")
			file.writelines(["%s" %item for item in data])
			file.close()

			# Show
			type220 = type220.lower()
			type220 = type220.replace(".", " ", 10)
			type220 = type220.title()
			brand220 = brand220.lower()
			brand220 = brand220.replace(".", " ", 10)
			brand220 = brand220.title()
			results22_id[1].configure(text = id220)
			results22_type[1].configure(text = type220)
			results22_size[1].configure(text = size220)
			results22_brand[1].configure(text = brand220)
			results22_quantity[1].configure(text = quantity220)
			results22_price[1].configure(text = price220)
	else:
		text_results22.configure(text = "")
		for i in range(1, 11):
			results22[i].configure(text = "")
			results22_id[i].configure(text = "")
			results22_type[i].configure(text = "")
			results22_size[i].configure(text = "")
			results22_brand[i].configure(text = "")
			results22_quantity[i].configure(text = "")
			results22_price[i].configure(text = "")

def delete22():
	btn_first22.configure(text = "", command = donothing)
	btn_prev22.configure(text = "", command = donothing)
	btn_next22.configure(text = "", command = donothing)
	btn_end22.configure(text = "", command = donothing)
	icon_page22.configure(text = "", relief = FLAT)

	icon_type22.configure(image = icon_bg22)
	icon_size22.configure(image = icon_bg22)
	icon_brand22.configure(image = icon_bg22)

	id220 = id_entry22.get()
	# Check_id
	check_id = True
	if id220 == "":
		check_id = False
	else:
		check_id = id220.isdigit()
	
	f_id = False
	if check_id:
		f_id = True
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id221 = []; sub2 = ""; type221 = ""; size221 = ""; brand221 = ""; quantity221 = ""; price221 = ""
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			id221.append(sub[0])
			
		for i in range(0, len(id221)):
			if id221[i] == id220:
				sub2 = data[i]
				sub3 = sub2.split()
				id221 = sub3[0]
				type221 = sub3[1]
				size221 = sub3[2]
				brand221 = sub3[3]
				quantity221 = sub3[4]
				price221 = sub3[5]
				break
		
		if sub2 != "":
			icon_id22.configure(image = icon_true22)
			data.remove(sub2)
		else:
			f_id = False
			icon_id22.configure(image = icon_notexist222)
	else:
		icon_id22.configure(image = icon_false22)

	if f_id:
		text_results22.configure(text = "1 result found")
		results22[1].configure(text = "1")
		results22_id[1].configure(text = id221)
		results22_type[1].configure(text = type221)
		results22_size[1].configure(text = size221)
		results22_brand[1].configure(text = brand221)
		results22_quantity[1].configure(text = quantity221)
		results22_price[1].configure(text = price221)

		if messagebox.askquestion("Shop BK", "Do you really want to delete this product's info?") == 'yes':
			file = open("product.txt", "w")
			file.writelines(["%s" %item for item in data])
			file.close()

			# Show
			text_results22.configure(text = "")
			icon_id22.configure(image = icon_bg22)
			results22[1].configure(text = "")
			results22_id[1].configure(text = "")
			results22_type[1].configure(text = "")
			results22_size[1].configure(text = "")
			results22_brand[1].configure(text = "")
			results22_quantity[1].configure(text = "")
			results22_price[1].configure(text = "")
	else:
		text_results22.configure(text = "")
		for i in range(1, 11):
			results22[i].configure(text = "")
			results22_id[i].configure(text = "")
			results22_type[i].configure(text = "")
			results22_size[i].configure(text = "")
			results22_brand[i].configure(text = "")
			results22_quantity[i].configure(text = "")
			results22_price[i].configure(text = "")

## TRANSACTION ##
def transaction2(*arg):
	global scr023
	global back023

	scr02.withdraw()
	scr023 = Toplevel(scr02)
	x0 = scr02.winfo_x()
	y0 = scr02.winfo_y()
	scr023.geometry("1200x700+%d+%d" %(x0, y0))
	scr023.title("Function")
	scr023.resizable(width = False, height = False)
	logo(scr023, 1)
	scr023.protocol("WM_DELETE_WINDOW", close)

	fr = Frame(scr023)
	Label(fr, text = "Hi Boss", font = 30, fg = "red").grid(row = 0, pady = 10)
	Button(fr, text = "3.1 Buy", width = 20, font = ("Tahoma", 20), command = buy2).grid(row = 1, pady = 30)
	scr023.bind("1", buy2)
	
	Button(fr, text = "3.2 Sell", width = 20, font = ("Tahoma", 20), command = sell2).grid(row = 2, pady = 30)
	scr023.bind("2", sell2)

	back023 = PhotoImage(file = "left.png")
	Button(fr, image = back023, relief = FLAT, command = trans2func2).grid(row = 3, pady = 40)
		
	fr.grid(row = 1, pady = 20)

def trans2func2():
	x0 = scr023.winfo_x()
	y0 = scr023.winfo_y()
	scr023.destroy()
	scr02.deiconify()
	scr02.geometry("1200x700+%d+%d" %(x0, y0))

## Buy
def buy2():
	global scr23
	global fr231
	global fr232
	global day_entry23
	global month_entry23
	global orderid_entry23
	global cusid_entry23
	global prodid_entry23
	global quantity_entry23
	global price_entry23
	global rs23
	global results23
	global results23_date
	global results23_orderid
	global results23_cusid
	global results23_prodid
	global results23_quantity
	global results23_price
	global icon_date23
	global icon_orderid23
	global icon_cusid23
	global icon_prodid23
	global icon_quantity23
	global icon_price23
	global icon_true23
	global icon_false23
	global icon_coincide23
	global icon_exist23
	global icon_notexist23
	global icon_bg23
	global back23

	scr023.withdraw()
	scr23 = Toplevel(scr023)
	x0 = scr023.winfo_x()
	y0 = scr023.winfo_y()
	scr23.geometry("1200x700+%d+%d" %(x0, y0))
	scr23.title("Buy")
	scr23.resizable(width = False, height = False)
	scr23.protocol("WM_DELETE_WINDOW", close)
	logo(scr23, 12)
	
	## Info
	fr = Frame(scr23)
	fr231 = Frame(fr)
	
	# Date
	Label(fr231, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 1)
	day = StringVar()
	day_entry23 = Entry(fr231, textvariable = day, width = 7, font = 30)
	day_entry23.grid(row = 0, column = 1, sticky = W)

	Label(fr231, text = "/", font = ("Tahoma", 20)).grid(row = 0, column = 2)
	
	month = StringVar()
	month_entry23 = Entry(fr231, textvariable = month, width = 7, font = 30)
	month_entry23.grid(row = 0, column = 3, sticky = E)

	# OrderID
	Label(fr231, text = "OrderID", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 3)
	orderid = StringVar()
	orderid_entry23 = Entry(fr231, textvariable = orderid, width = 20, font = 30)
	orderid_entry23.grid(row = 2, column = 1, columnspan = 3, sticky = W)
	
	# CusID
	Label(fr231, text = "CusID", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 5)
	cusid = StringVar()
	cusid_entry23 = Entry(fr231, textvariable = cusid, width = 20, font = 30)
	cusid_entry23.grid(row = 4, column = 1, columnspan = 3, sticky = W)

	# ProdID
	Label(fr231, text = "ProdID", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 7)
	proid = StringVar()
	prodid_entry23 = Entry(fr231, textvariable = proid, width = 20, font = 30)
	prodid_entry23.grid(row = 6, column = 1, columnspan = 3, sticky = W)

	# Quantity
	Label(fr231, text = "Quantity", font = ("Tahoma", 20)).grid(row = 8, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 9)
	quantity = StringVar()
	quantity_entry23 = Entry(fr231, textvariable = quantity, width = 20, font = 30)
	quantity_entry23.grid(row = 8, column = 1, columnspan = 3, sticky = W)

	# Price
	Label(fr231, text = "Price", font = ("Tahoma", 20)).grid(row = 10, column = 0, sticky = W, padx = 30)
	Label(fr231).grid(row = 11)
	price = StringVar()
	price_entry23 = Entry(fr231, textvariable = price, width = 20, font = 30)
	price_entry23.grid(row = 10, column = 1, columnspan = 3, sticky = W)

	# Reset
	rs23 = PhotoImage(file = "reset.png")
	Button(fr231, image = rs23, relief = FLAT, command = reset23).grid(row = 12, column = 1, sticky = W)
	
	# CREATE
	Button(fr231, text = "CREATE", font = ("Tahoma", 16), command = create23).grid(row = 12, column = 2, columnspan = 2, sticky = E)
	scr23.bind("<Return>", create23)

	# Back to login
	back23 = PhotoImage(file = "left.png")
	Button(fr231, image = back23, relief = FLAT, command = buy2trans23).grid(row = 12, column = 0)

	# Check icons
	icon_true23 = PhotoImage(file = "true.png")
	icon_false23 = PhotoImage(file = "false.png")
	icon_exist23 = PhotoImage(file = "exist.png")
	icon_notexist23 = PhotoImage(file = "notexist.png")
	icon_coincide23 = PhotoImage(file = "coincide.png")
	icon_bg23 =  PhotoImage(file = "bg.png")

	icon_date23 = Label(fr231, image = icon_bg23)
	icon_date23.grid(row = 0, column = 6, padx = 20)
	icon_orderid23 = Label(fr231, image = icon_bg23)
	icon_orderid23.grid(row = 2, column = 6, padx = 20)
	icon_cusid23 = Label(fr231, image = icon_bg23)
	icon_cusid23.grid(row = 4, column = 6, padx = 20)
	icon_prodid23 = Label(fr231, image = icon_bg23)
	icon_prodid23.grid(row = 6, column = 6, padx = 20)
	icon_quantity23 = Label(fr231, image = icon_bg23)
	icon_quantity23.grid(row = 8, column = 6, padx = 20)
	icon_price23 = Label(fr231, image = icon_bg23)
	icon_price23.grid(row = 10, column = 6, padx = 20)

	## Results
	fr232 = Frame(fr)
	Label(fr232, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 12)
	Label(fr232, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 12)
	Label(fr232, text = "OrderID", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 12)
	Label(fr232, text = "CusID", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 12)
	Label(fr232, text = "ProdID", font = ("Tahoma", 20)).grid(row = 0, column = 9, padx = 12)
	Label(fr232, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 12)
	Label(fr232, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 12)

	# No.
	results23 = Label(fr232, font = ("Tahoma", 20))
	results23.grid(row = 1, column = 5)

	# Date
	results23_date = Label(fr232, font = ("Arial", 15))
	results23_date.grid(row = 1, column = 6)

	# OrderID
	results23_orderid = Label(fr232, font = ("Arial", 15))
	results23_orderid.grid(row = 1, column = 7)

	# CusID
	results23_cusid = Label(fr232, font = ("Arial", 15))
	results23_cusid.grid(row = 1, column = 8)

	# ProdID
	results23_prodid = Label(fr232, font = ("Arial", 15))
	results23_prodid.grid(row = 1, column = 9)

	# Quantity
	results23_quantity = Label(fr232, font = ("Arial", 15))
	results23_quantity.grid(row = 1, column = 10)

	# Price
	results23_price = Label(fr232, font = ("Arial", 15))
	results23_price.grid(row = 1, column = 11)
	
	fr231.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr232.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def buy2trans23():
	x0 = scr23.winfo_x()
	y0 = scr23.winfo_y()
	scr23.destroy()
	scr023.deiconify()
	scr023.geometry("1200x700+%d+%d" %(x0, y0))

def reset23():
	day_entry23.delete(0, END)
	month_entry23.delete(0, END)
	orderid_entry23.delete(0, END)
	cusid_entry23.delete(0, END)
	prodid_entry23.delete(0, END)
	quantity_entry23.delete(0, END)
	price_entry23.delete(0, END)

	icon_date23.configure(image = icon_bg23)
	icon_orderid23.configure(image = icon_bg23)
	icon_cusid23.configure(image = icon_bg23)
	icon_prodid23.configure(image = icon_bg23)
	icon_quantity23.configure(image = icon_bg23)
	icon_price23.configure(image = icon_bg23)

	results23.configure(text = "")
	results23_date.configure(text = "")
	results23_orderid.configure(text = "")
	results23_cusid.configure(text = "")
	results23_prodid.configure(text = "")
	results23_quantity.configure(text = "")
	results23_price.configure(text = "")

def create23(*arg):
	day230 = day_entry23.get()
	month230 = month_entry23.get()
	orderid230 = orderid_entry23.get()
	cusid230 = cusid_entry23.get()
	prodid230 = prodid_entry23.get()
	quantity230 = quantity_entry23.get()
	price230 = price_entry23.get()

	# Check date
	check_date = True
	if day230 == "" or month230 == "":
		check_date = False
	else:
		if (day230.isdigit() == False or month230.isdigit() == False):
			check_date = False
		else:
			d230 = int(day230)
			m230 = int(month230)
			if m230 not in range(1, 13):
				check_date = False
			else:
				if m230 in [1, 3, 5, 7, 8, 10, 12] and d230 not in range(1, 32):
					check_date = False
				elif m230 in [4, 6, 9, 11] and d230 not in range(1, 31):
					check_date = False
				elif m230 == 2 and d230 not in range(1, 30):
					check_date = False
	
	if check_date:
		icon_date23.configure(image = icon_true23)
	else:
		icon_date23.configure(image = icon_false23)

	# Check OrderID
	check_orderid = True
	if orderid230 == "":
		check_orderid = False
	else:
		check_orderid = orderid230.isdigit()

	f_orderid = False
	if check_orderid:
		f_orderid = True
		file = open("hoadon_mua.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; orderid = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			orderid.append(sub[1])
		for i in range(0, len(orderid)):
			if int(orderid[i]) == int(orderid230):
				f_orderid = False
	
	if f_orderid:
		icon_orderid23.configure(image = icon_true23)
	else:
		icon_orderid23.configure(image = icon_coincide23)

	if check_orderid == False:
		icon_orderid23.configure(image = icon_false23)

	# Check CusID
	check_cusid = True
	if cusid230 == "":
		check_cusid = False
	else:
		check_cusid = cusid230.isdigit()
	
	if check_cusid:
		icon_cusid23.configure(image = icon_true23)
	else:
		icon_cusid23.configure(image = icon_false23)

	# Check ProdID
	check_prodid = True
	if prodid230 == "":
		check_prodid = False
	else:
		check_prodid = prodid230.isdigit()
	
	if check_prodid:
		icon_prodid23.configure(image = icon_true23)
	else:
		icon_prodid23.configure(image = icon_false23)

	# Check Quantity
	check_quantity = True
	if quantity230 == "":
		check_quantity = False
	else:
		check_quantity = quantity230.isdigit()

	if check_quantity:
		icon_quantity23.configure(image = icon_true23)
	else:
		icon_quantity23.configure(image = icon_false23)

	# Check Price
	check_price = True
	if price230 == "":
		check_price = False
	else:
		check_price = price230.isdigit()

	if check_price:
		icon_price23.configure(image = icon_true23)
	else:
		icon_price23.configure(image = icon_false23)

	# All check are true	
	if check_date and f_orderid and check_cusid and check_prodid and check_quantity and check_price:
		# Check if this customer has already existed
		file = open("customer.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; name231 = []; phone231 = []; age231 = []; gender231 = []; price231 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()
		for i in range(0, lines):
			sub = data[i].split()
			name231.append(sub[0])
			phone231.append(sub[1])
			age231.append(sub[2])
			gender231.append(sub[3])
			price231.append(sub[4])

		f_cusid = False
		for i in range(0, len(phone231)):
			if phone231[i] == cusid230:
				f_cusid = True
				price231[i] = str(int(price231[i]) + int(quantity230)*int(price230)) 
				data[i] = name231[i] + " " + phone231[i] + " " + age231[i] + " " + gender231[i] + " " + price231[i] + "\n"
				icon_cusid23.configure(image = icon_exist23)
		if f_cusid == False:
			new_cus = "x" + " " + cusid230 + " " + "0" + " " + "x" + " " + str(int(quantity230)*int(price230)) + "\n"
			data.append(new_cus)
			icon_cusid23.configure(image = icon_notexist23) 

		file = open("customer.txt", "r+")
		file.writelines(["%s" %item for item in data])
		file.close()

		# Check if this product has already existed
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id231 = []; type231 = []; size231 = []; brand231 = []; quantity231 = []; price231 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()
		for i in range(0, lines):
			sub = data[i].split()
			id231.append(sub[0])
			type231.append(sub[1])
			size231.append(sub[2])
			brand231.append(sub[3])
			quantity231.append(sub[4])
			price231.append(sub[5])

		f_prodid = False
		for i in range(0, len(id231)):
			if int(id231[i]) == int(prodid230):
				f_prodid = True
				quantity231[i] = str(int(quantity231[i]) + int(quantity230))
				if int(price231[i]) < 2*int(price230):
					price231[i] = str(2*int(price230))
				data[i] = id231[i] + " " + type231[i] + " " + size231[i] + " " + brand231[i] + " " + quantity231[i] + " " + price231[i] + "\n"
				icon_prodid23.configure(image = icon_exist23)
		if f_prodid == False:
			new_prod = prodid230 + " " + "x" + " " + "0" + " " + "x" + " " + quantity230 + " " + str(2*int(price230)) + "\n"
			data.append(new_prod)
			icon_prodid23.configure(image = icon_notexist23) 

		file = open("product.txt", "r+")
		file.writelines(["%s" %item for item in data])
		file.close()

		# Create Bill
		results23.configure(text = 1)
		results23_date.configure(text = day230 + "/" + month230)
		results23_orderid.configure(text = orderid230)
		results23_cusid.configure(text = cusid230)
		results23_prodid.configure(text = prodid230)
		results23_quantity.configure(text = quantity230)
		results23_price.configure(text = price230)
		file = open("hoadon_mua.txt", "a+")
		file.writelines(day230 + "." + month230 + " " + orderid230 + " " + cusid230 + " " + prodid230 + " " + quantity230 + " " + price230 + "\n")
		file.close()
	else:
		results23.configure(text = "")
		results23_date.configure(text = "")
		results23_orderid.configure(text = "")
		results23_cusid.configure(text = "")
		results23_prodid.configure(text = "")
		results23_quantity.configure(text = "")
		results23_price.configure(text = "")
# Sell
def sell2():
	global scr24
	global fr241
	global fr242
	global day_entry24
	global month_entry24
	global orderid_entry24
	global cusid_entry24
	global prodid_entry24
	global quantity_entry24
	global rs24
	global results24
	global results24_date
	global results24_orderid
	global results24_cusid
	global results24_prodid
	global results24_quantity
	global results24_price
	global state24
	global icon_date24
	global icon_orderid24
	global icon_cusid24
	global icon_prodid24
	global icon_quantity24
	global icon_price24
	global icon_true24
	global icon_false24
	global icon_exist24
	global icon_notexist24
	global icon_notexist242
	global icon_coincide24
	global icon_exclamation24
	global icon_bg24
	global back24

	scr023.withdraw()
	scr24 = Toplevel(scr023)
	x0 = scr023.winfo_x()
	y0 = scr023.winfo_y()
	scr24.geometry("1200x700+%d+%d" %(x0, y0))
	scr24.title("Sell")
	scr24.resizable(width = False, height = False)
	scr24.protocol("WM_DELETE_WINDOW", close)
	logo(scr24, 12)
	
	## Info
	fr = Frame(scr24)
	fr241 = Frame(fr)
	
	# Date
	Label(fr241, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30)
	Label(fr241).grid(row = 1)
	day = StringVar()
	day_entry24 = Entry(fr241, textvariable = day, width = 7, font = 30)
	day_entry24.grid(row = 0, column = 1, sticky = W)

	Label(fr241, text = "/", font = ("Tahoma", 20)).grid(row = 0, column = 2)
	
	month = StringVar()
	month_entry24 = Entry(fr241, textvariable = month, width = 7, font = 30)
	month_entry24.grid(row = 0, column = 3, sticky = E)

	# OrderID
	Label(fr241, text = "OrderID", font = ("Tahoma", 20)).grid(row = 2, column = 0, sticky = W, padx = 30)
	Label(fr241).grid(row = 3)
	orderid = StringVar()
	orderid_entry24 = Entry(fr241, textvariable = orderid, width = 20, font = 30)
	orderid_entry24.grid(row = 2, column = 1, columnspan = 3, sticky = W)
	
	# CusID
	Label(fr241, text = "CusID", font = ("Tahoma", 20)).grid(row = 4, column = 0, sticky = W, padx = 30)
	Label(fr241).grid(row = 5)
	cusid = StringVar()
	cusid_entry24 = Entry(fr241, textvariable = cusid, width = 20, font = 30)
	cusid_entry24.grid(row = 4, column = 1, columnspan = 3, sticky = W)

	# ProdID
	Label(fr241, text = "ProdID", font = ("Tahoma", 20)).grid(row = 6, column = 0, sticky = W, padx = 30)
	Label(fr241).grid(row = 7)
	proid = StringVar()
	prodid_entry24 = Entry(fr241, textvariable = proid, width = 20, font = 30)
	prodid_entry24.grid(row = 6, column = 1, columnspan = 3, sticky = W)

	# Quantity
	Label(fr241, text = "Quantity", font = ("Tahoma", 20)).grid(row = 8, column = 0, sticky = W, padx = 30)
	Label(fr241).grid(row = 9)
	quantity = StringVar()
	quantity_entry24 = Entry(fr241, textvariable = quantity, width = 20, font = 30)
	quantity_entry24.grid(row = 8, column = 1, columnspan = 3, sticky = W)

	# Reset
	rs24 = PhotoImage(file = "reset.png")
	Button(fr241, image = rs24, relief = FLAT, command = reset24).grid(row = 10, column = 1, sticky = W)
	
	# CREATE
	Button(fr241, text = "CREATE", font = ("Tahoma", 16), command = create24).grid(row = 10, column = 2, columnspan = 2, sticky = E)
	scr24.bind("<Return>", create24)

	# State
	state24 = Label(fr241, font = ("Arial", 15))
	state24.grid(row = 11, column = 1, columnspan = 3)

	# Back to login
	back24 = PhotoImage(file = "left.png")
	Button(fr241, image = back24, relief = FLAT, command = sell2trans24).grid(row = 12, column = 0)

	# Check icons
	icon_true24 = PhotoImage(file = "true.png")
	icon_false24 = PhotoImage(file = "false.png")
	icon_exist24 = PhotoImage(file = "exist.png")
	icon_notexist24 = PhotoImage(file = "notexist.png")
	icon_notexist242 = PhotoImage(file = "notexist2.png")
	icon_coincide24 = PhotoImage(file = "coincide.png")
	icon_exclamation24 = PhotoImage(file = "!.png")
	icon_bg24 =  PhotoImage(file = "bg.png")

	icon_date24 = Label(fr241, image = icon_bg24)
	icon_date24.grid(row = 0, column = 6, padx = 20)
	icon_orderid24 = Label(fr241, image = icon_bg24)
	icon_orderid24.grid(row = 2, column = 6, padx = 20)
	icon_cusid24 = Label(fr241, image = icon_bg24)
	icon_cusid24.grid(row = 4, column = 6, padx = 20)
	icon_prodid24 = Label(fr241, image = icon_bg24)
	icon_prodid24.grid(row = 6, column = 6, padx = 20)
	icon_quantity24 = Label(fr241, image = icon_bg24)
	icon_quantity24.grid(row = 8, column = 6, padx = 20)

	## Results
	fr242 = Frame(fr)
	Label(fr242, text = "No.", font = ("Tahoma", 20)).grid(row = 0, column = 5, padx = 12)
	Label(fr242, text = "Date", font = ("Tahoma", 20)).grid(row = 0, column = 6, padx = 12)
	Label(fr242, text = "OrderID", font = ("Tahoma", 20)).grid(row = 0, column = 7, padx = 12)
	Label(fr242, text = "CusID", font = ("Tahoma", 20)).grid(row = 0, column = 8, padx = 12)
	Label(fr242, text = "ProdID", font = ("Tahoma", 20)).grid(row = 0, column = 9, padx = 12)
	Label(fr242, text = "Quan.", font = ("Tahoma", 20)).grid(row = 0, column = 10, padx = 12)
	Label(fr242, text = "Price", font = ("Tahoma", 20)).grid(row = 0, column = 11, padx = 12)

	# No.
	results24 = Label(fr242, font = ("Tahoma", 20))
	results24.grid(row = 1, column = 5)

	# Date
	results24_date = Label(fr242, font = ("Arial", 15))
	results24_date.grid(row = 1, column = 6)

	# OrderID
	results24_orderid = Label(fr242, font = ("Arial", 15))
	results24_orderid.grid(row = 1, column = 7)

	# CusID
	results24_cusid = Label(fr242, font = ("Arial", 15))
	results24_cusid.grid(row = 1, column = 8)

	# ProdID
	results24_prodid = Label(fr242, font = ("Arial", 15))
	results24_prodid.grid(row = 1, column = 9)

	# Quantity
	results24_quantity = Label(fr242, font = ("Arial", 15))
	results24_quantity.grid(row = 1, column = 10)

	# Price
	results24_price = Label(fr242, font = ("Arial", 15))
	results24_price.grid(row = 1, column = 11)
	
	fr241.grid(row = 0, rowspan = 100, column = 0, columnspan = 5)
	fr242.grid(row = 0, rowspan = 100, column = 5, columnspan = 5, sticky = "nw")
	fr.grid(row = 1)

def sell2trans24():
	x0 = scr24.winfo_x()
	y0 = scr24.winfo_y()
	scr24.destroy()
	scr023.deiconify()
	scr023.geometry("1200x700+%d+%d" %(x0, y0))

def reset24():
	day_entry24.delete(0, END)
	month_entry24.delete(0, END)
	orderid_entry24.delete(0, END)
	cusid_entry24.delete(0, END)
	prodid_entry24.delete(0, END)
	quantity_entry24.delete(0, END)

	icon_date24.configure(image = icon_bg24)
	icon_orderid24.configure(image = icon_bg24)
	icon_cusid24.configure(image = icon_bg24)
	icon_prodid24.configure(image = icon_bg24)
	icon_quantity24.configure(image = icon_bg24)
	state24.configure(text = "")

	results24.configure(text = "")
	results24_date.configure(text = "")
	results24_orderid.configure(text = "")
	results24_cusid.configure(text = "")
	results24_prodid.configure(text = "")
	results24_quantity.configure(text = "")
	results24_price.configure(text = "")
	

def create24(*arg):
	day240 = day_entry24.get()
	month240 = month_entry24.get()
	orderid240 = orderid_entry24.get()
	cusid240 = cusid_entry24.get()
	prodid240 = prodid_entry24.get()
	quantity240 = quantity_entry24.get()

	# Check date
	check_date = True
	if day240 == "" or month240 == "":
		check_date = False
	else:
		if (day240.isdigit() == False or month240.isdigit() == False):
			check_date = False
		else:
			d240 = int(day240)
			m240 = int(month240)
			if m240 not in range(1, 13):
				check_date = False
			else:
				if m240 in [1, 3, 5, 7, 8, 10, 12] and d240 not in range(1, 32):
					check_date = False
				elif m240 in [4, 6, 9, 11] and d240 not in range(1, 31):
					check_date = False
				elif m240 == 2 and d240 not in range(1, 30):
					check_date = False
	
	if check_date:
		icon_date24.configure(image = icon_true24)
	else:
		icon_date24.configure(image = icon_false24)

	# Check OrderID
	check_orderid = True
	if orderid240 == "":
		check_orderid = False
	else:
		check_orderid = orderid240.isdigit()

	f_orderid = False
	if check_orderid:
		f_orderid = True
		file = open("hoadon_ban.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; orderid = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			orderid.append(sub[1])
		for i in range(0, len(orderid)):
			if int(orderid[i]) == int(orderid240):
				f_orderid = False
	
	if f_orderid:
		icon_orderid24.configure(image = icon_true24)
	else:
		icon_orderid24.configure(image = icon_coincide24)

	if check_orderid == False:
		icon_orderid24.configure(image = icon_false24)

	# Check CusID
	check_cusid = True
	if cusid240 == "":
		check_cusid = False
	else:
		check_cusid = cusid240.isdigit()
	
	if check_cusid:
		icon_cusid24.configure(image = icon_true24)
	else:
		icon_cusid24.configure(image = icon_false24)

	# Check ProdID
	check_prodid = True
	if prodid240 == "":
		check_prodid = False
	else:
		check_prodid = prodid240.isdigit()

	f_prodid = False
	if check_prodid:
		f_prodid = True
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; prodid = []; price = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			prodid.append(sub[0])
			price.append(sub[5])
		for i in range(0, len(prodid)):
			if int(prodid[i]) == int(prodid240):
				f_prodid = False
				price240 = price[i]
	
	if f_prodid:
		icon_prodid24.configure(image = icon_notexist242)
	else:
		icon_prodid24.configure(image = icon_true24)

	if check_prodid == False:
		icon_prodid24.configure(image = icon_false24)

	# Check Quantity
	check_quantity = True
	if quantity240 == "":
		check_quantity = False
	else:
		check_quantity = quantity240.isdigit()

	if check_quantity:
		icon_quantity24.configure(image = icon_true24)
	else:
		icon_quantity24.configure(image = icon_false24)

	# All check are true	
	if check_date and f_orderid and check_cusid and not f_prodid and check_quantity:
		# Check if this product is enough
		file = open("product.txt")
		lines = sum(1 for line in file)
		file.seek(0)
		data = []; id241 = []; type241 = []; size241 = []; brand241 = []; quantity241 = []; price241 = []
		for i in range(0, lines):
			data.append(file.readline()) 
		file.close()

		for i in range(0, lines):
			sub = data[i].split()
			id241.append(sub[0])
			type241.append(sub[1])
			size241.append(sub[2])
			brand241.append(sub[3])
			quantity241.append(sub[4])
			price241.append(sub[5])

		for i in range(0, len(id241)):
			if int(id241[i]) == int(prodid240):
				if int(quantity241[i]) < int(quantity240):
					icon_quantity24.configure(image = icon_exclamation24)
					state24.configure(text = "Not enough")
				else:
					icon_quantity24.configure(image = icon_true24)
					state24.configure(text = "")
					quantity241[i] = str(int(quantity241[i]) - int(quantity240))
					data[i] = id241[i] + " " + type241[i] + " " + size241[i] + " " + brand241[i] + " " + quantity241[i] + " " + price241[i] + "\n"
					file = open("product.txt", "r+")
					file.writelines(["%s" %item for item in data])
					file.close()

					# Check if this customer has alreadry existed
					file = open("customer.txt")
					lines = sum(1 for line in file)
					file.seek(0)
					data = []; name241 = []; phone241 = []; age241 = []; gender241 = []; price241 = []
					for i in range(0, lines):
						data.append(file.readline()) 
					file.close()
					for i in range(0, lines):
						sub = data[i].split()
						name241.append(sub[0])
						phone241.append(sub[1])
						age241.append(sub[2])
						gender241.append(sub[3])
						price241.append(sub[4])

					f_cusid = False
					for i in range(0, len(phone241)):
						if phone241[i] == cusid240:
							f_cusid = True
							price241[i] = str(int(price241[i]) + int(quantity240)*int(price240)) 
							data[i] = name241[i] + " " + phone241[i] + " " + age241[i] + " " + gender241[i] + " " + price241[i] + "\n"
							icon_cusid24.configure(image = icon_exist24)
					if f_cusid == False:
						new_cus = "x" + " " + cusid240 + " " + "0" + " " + "x" + " " + str(int(quantity240)*int(price240)) + "\n"
						data.append(new_cus)
						icon_cusid24.configure(image = icon_notexist24) 

					file = open("customer.txt", "r+")
					file.writelines(["%s" %item for item in data])
					file.close()

					# Create bill
					results24.configure(text = 1)
					results24_date.configure(text = day240 + "/" + month240)
					results24_orderid.configure(text = orderid240)
					results24_cusid.configure(text = cusid240)
					results24_prodid.configure(text = prodid240)
					results24_quantity.configure(text = quantity240)
					results24_price.configure(text = price240)
					file = open("hoadon_ban.txt", "a+")
					file.writelines(day240 + "." + month240 + " " + orderid240 + " " + cusid240 + " " + prodid240 + " " + quantity240 + " " + price240 + "\n")
					file.close()
					break
	else:
		results24.configure(text = "")
		results24_date.configure(text = "")
		results24_orderid.configure(text = "")
		results24_cusid.configure(text = "")
		results24_prodid.configure(text = "")
		results24_quantity.configure(text = "")
		results24_price.configure(text = "")
###---------------------###
## Login
def boss(*arg):
	global scr01
	global back01
	root.withdraw()
	scr01 = Toplevel(root)
	x0 = root.winfo_x()
	y0 = root.winfo_y()
	scr01.geometry("1200x700+%d+%d" %(x0, y0))
	scr01.title("Function")
	scr01.resizable(width = False, height = False)
	logo(scr01, 1)
	scr01.protocol("WM_DELETE_WINDOW", close) 

	fr = Frame(scr01)
	Label(fr, text = "Hi Boss", font = 30, fg = "red").grid(row = 0, pady = 10)
	Button(fr, text = "1. Customer", width = 20, font = ("Tahoma", 20), command = customer1).grid(row = 1, pady = 30)
	scr01.bind("1", customer1)
	
	Button(fr, text = "2. Product", width = 20, font = ("Tahoma", 20), command = product1).grid(row = 2, pady = 30)
	scr01.bind("2", product1)

	Button(fr, text = "3. Transaction", width = 20, font = ("Tahoma", 20), command = transaction1).grid(row = 3, pady = 30)
	scr01.bind("3", transaction1)
	
	back01 = PhotoImage(file = "logout.png")
	Button(fr, image = back01, relief = FLAT, command = boss2home).grid(row = 4, pady = 10)
	fr.grid(row = 1, pady = 20)

def boss2home():
	if messagebox.askquestion("Shop BK", "Do you really want to log out?") == 'yes':
		x0 = scr01.winfo_x()
		y0 = scr01.winfo_y()
		scr01.destroy()
		root.deiconify()
		root.geometry("1200x700+%d+%d" %(x0, y0))

def employee():
	global scr02
	global back02
	root.withdraw()
	scr02 = Toplevel(root)
	x0 = root.winfo_x()
	y0 = root.winfo_y()
	scr02.geometry("1200x700+%d+%d" %(x0, y0))
	scr02.title("Function")
	scr02.resizable(width = False, height = False)
	logo(scr02, 1)
	scr02.protocol("WM_DELETE_WINDOW", close) 

	fr = Frame(scr02)
	Label(fr, text = "Hi " + user.title(), font = 30, fg = "red").grid(row = 0, pady = 10)
	Button(fr, text = "1. Customer", width = 20, font = ("Tahoma", 20), command = customer2).grid(row = 1, pady = 30)
	scr02.bind("1", customer2)
	
	Button(fr, text = "2. Product", width = 20, font = ("Tahoma", 20), command = product2).grid(row = 2, pady = 30)
	scr02.bind("2", product2)

	Button(fr, text = "3. Transaction", width = 20, font = ("Tahoma", 20), command = transaction2).grid(row = 3, pady = 30)
	scr02.bind("3", transaction2)
	
	back02 = PhotoImage(file = "logout.png")
	Button(fr, image = back02, relief = FLAT, command = emp2home).grid(row = 4, pady = 10)
	fr.grid(row = 1, pady = 20)

def emp2home():
	if messagebox.askquestion("Shop BK", "Do you really want to log out?") == 'yes':
		x0 = scr02.winfo_x()
		y0 = scr02.winfo_y()
		scr02.destroy()
		root.deiconify()
		root.geometry("1200x700+%d+%d" %(x0, y0))

def login(*arg):
	global user
	m = mode.get()
	user = username_entry.get()
	passwd = password_entry.get()

	if m == 1:
		if user == "boss" and passwd == "123":
			boss()
		else:
			messagebox.showinfo("Oops", "The username or password is incorrect!")

	if m == 2:
		if user in ["duy", "dat", "dang", "duc", "giang", "hoang"] and passwd == "123":
			employee()
		else:
			messagebox.showinfo("Oops", "The username or password is incorrect!")

###----------------------###
## Main
def main_screen():
	global root
	global lg
	global username_entry
	global password_entry
	global mode

	root = Tk()
	root.geometry("1200x700+200+50")
	root.title("SHOP BK")
	root.resizable(width = False, height = False) 
	root.title("Shop BK")
	lg = PhotoImage(file = "bk.png")
	logo(root, 1)
		
	fr = Frame(root)
	Label(fr, text = "Username", font = ("Tahoma", 20)).grid(row = 0, column = 0, sticky = W, padx = 30, pady = 20)
	username = StringVar()
	username_entry = Entry(fr, textvariable = username, width = 20, font = 30)
	# username_entry.bind("<Return>", login)
	username_entry.grid(row = 0, column = 1, sticky = W, padx = 30, pady = 20)
	
	Label(fr, text = "Password", font = ("Tahoma", 20)).grid(row = 1, column = 0, sticky = W, padx = 30, pady = 20)
	password = StringVar()
	password_entry = Entry(fr, textvariable = password, width = 20, font = 30)
	# password_entry.bind("<Return>", login)
	password_entry.grid(row = 1, column = 1, sticky = W, padx = 30, pady = 20)

	mode = IntVar()
	Radiobutton(fr, text = "Boss", font = 20, variable = mode, value = 1).grid(row = 2, column = 1, sticky = W, padx = 30, pady = 10)
	Radiobutton(fr, text = "Employee", font = 20, variable = mode, value = 2).grid(row = 3, column = 1, sticky = W, padx = 30, pady = 10)
	mode.set(1)
	
	btn = Button(fr, text = "Log in", font = ("Tahoma", 20), command = login)
	btn.bind("<Return>", login)
	btn.grid(row = 4, column = 1, sticky = W, padx = 30, pady = 30)
	
	root.bind("<Return>", login)  # bind for button login  
	
	fr.grid(row = 1, pady = 20)
	root.protocol("WM_DELETE_WINDOW", close)
	root.mainloop()
	
main_screen()