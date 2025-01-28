import xml.etree.ElementTree as xml
import os
import time
import datetime

time.sleep(2)
print('Hello, welcome to the inventory system')

# import xml.etree.ElementTree as xml
# import os
# # from colorama import Fore, init, Back, Style
# # init()

# '''
# These are variable that can be modified according to the user's likings.
# '''
# user_os = 'Unix' # Change manually here your OS
# file_name = 'inventory.xml' # Change the value of this variable in order to change the default name


# '''
# Please, do not change the following code
# '''

# root = xml.Element('inventory')
# PROPERTIES = ['author', 'released_date', 'genre', 'age_clasification', 'language', 'isbn', 'price']

# def clear(user_os):
# 	if 'Windows' == user_os:
# 		os.system('cls')
# 	else:
# 		os.system('clear')

# def delete(file_name):
# 	tree = xml.parse(file_name)

# 	temp_file = xml.Element('inventory')
# 	in_user = input('Insert the book title you want to delete >')

# 	for book in tree.getroot():
# 		if book.tag != in_user:
# 			temp_file.append(book)
# 		else:
# 			pass
	
# 	tree = xml.ElementTree(temp_file)
# 	tree.write(file_name)
			
# def update(file_name):
# 	def change_values(element):
# 		print('Change:'+
# 			"\n\t1 - Book's title"+
# 			'\n\t2 - Author'+
# 			'\n\t3 - Date of release'+
# 			'\n\t4 - Genre'+
# 			'\n\t5 - Age clasification'+
# 			'\n\t6 - Language'+
# 			'\n\t7 - ISBN'+
# 			'\n\t8 - Price'+
# 			'\n[Enter] to cancel the operation')
		
# 		in_user = input('>')
		
# 		if '1' == in_user:
# 			element.tag = input('Insert new title >')
# 			return element
# 		elif '2' == in_user:
# 			element[0].text = input('Insert new author >')
# 			return element
# 		elif '3' == in_user:
# 			for date in element[1]:
# 				date.text = input(f'Insert new {date.tag} >')
# 			return element
# 		elif '4' == in_user:
# 			element[2].text = input('Insert new genre >')
# 			return element
# 		elif '5' == in_user:
# 			element[3].text = input('Insert new age classification >')
# 			return element
# 		elif '6' == in_user:
# 			element[4].text = input('Insert new language >')
# 			return element
# 		elif '7' == in_user:
# 			element[5].text = input('Insert new ISBN >')
# 			return element
# 		elif '8' == in_user:
# 			element[6].text = input('Insert new price >')
# 		else:
# 			return element

# 	tree = xml.parse(file_name)


# 	temp_file = xml.Element('inventory')
# 	in_user = input('Insert the book title you want to update >')

# 	for book in tree.getroot():
# 		if book.tag == in_user:
# 			temp_file.append(change_values(book))
# 		else:
# 			temp_file.append(book)
	
# 	tree = xml.ElementTree(temp_file)
# 	tree.write(file_name)
		
# def show(file_name):
	
# 	def show_all():

# 		tree = xml.parse(file_name)
		
		
# 		print('All books:')
# 		for book in tree.getroot():
# 			print(f'\t- {book.tag}')
		
# 	def show_all_properties():
# 		tree = xml.parse(file_name)
# 		in_user = input('Insert the book that you want to see its properties>')
	
# 		for book in tree.getroot():
# 			if book.tag == in_user:
# 				for property in book:
# 					# Only for the released date
# 					if book[1] == property:
# 						for date in property:
# 							print(f'\t{date.tag}: {date.text}')
# 					else:
# 						print(f'\t{property.tag}: {property.text}')
# 			else:
# 				pass

# 	def show_one_property():
# 		tree = xml.parse(file_name)
# 		in_user = input('Insert the book that you want to see its property >')

# 		for book in tree.getroot():
# 			if book.tag == in_user:
# 				# Menu
# 				print('All properties:')
# 				for property in PROPERTIES:
# 					print(f'\t-{property}')
# 				in_user = input('Insert which option you want to see >')
				
# 				for property in book:
# 					if property.tag == in_user:
# 						# Only for the released date
# 						if book[1] == property:
# 							for date in property:
# 								print(f'\t{date.tag}: {date.text}')
# 						else:
# 							print(f'\t{property.tag}: {property.text}')
# 			else:
# 				pass
	

# 	clear(user_os)
# 	print('Options:'+
# 			'\n\t1 - All books'+
# 			'\n\t2 - Show all the information of a book'+
# 			'\n\t3 - Show a property of a book '+
# 			'\n[Enter] to cancel the operation')
# 	in_user = input('>')

# 	if '1' == in_user:
# 		show_all()
# 	elif '2' == in_user:
# 		show_all_properties()
# 	elif '3' == in_user:
# 		show_one_property()
# 	else:
# 		pass

# def calculate(file_name):
# 	def all_revenue():
# 		tree = xml.parse(file_name)
# 		all_revenue = 0
		
# 		for book in tree.getroot():
# 			try:
# 				all_revenue += float(book[6].text)
# 			except:
# 				pass

# 		print(f"The total inventory's revenue is: {all_revenue}")
	
# 	def years_passed():
# 		tree = xml.parse(file_name)
# 		actual_year = 2024
		
# 		in_user = input('Insert which book you want to calculate its years >')

# 		for book in tree.getroot():
# 			if book.tag == in_user:
# 				for property in book:
# 					if book[1] == property:
# 						for date in property:
# 							if 'released_year' == date.tag:
# 								print(f'The book {book.tag} is {actual_year - int(date.text)} years old')
# 							else:
# 								pass
# 					else:
# 						pass

# 	def price_amount_books():
# 		tree = xml.parse(file_name)
# 		total_price = 0
# 		amount_books = []
		
# 		in_user = ''

# 		while in_user.lower() != 'q':
# 			in_user = input('Insert which books you want to sum its price [q for exit]>')
# 			amount_books.append(in_user)
		
# 		for book in tree.findall('inventory'):
# 			print(book.tag)
# 			if book.tag in amount_books:
# 				total_price += float(book[6].text)
# 			else:
# 				pass
		
# 		print(f'Total price: {total_price}')
	
# 	tree = xml.parse(file_name)
# 	clear(user_os)
	
# 	print('Options:'+
# 			'\n\t1 - Calculates how many years has passed since released'+
# 			'\n[Enter] to cancel the operation')
# 	in_user = input('>')
	
# 	if '1' == in_user:
# 		years_passed()
# 	else:
# 		pass

# def add(file_name):
# 	temp_element = {
# 		'author': '',
# 		'released_date': [],
# 		'genre': '',
# 		'age_clasification': 0,
# 		'language': '',
# 		'isbn': 0,
# 		'price': 0.0
# 	}
	
# 	child = xml.SubElement(root, input('Insert the book title >'))
		
# 	for k in temp_element:
# 			if list == type(temp_element[k]):
# 				temp_element[k] = input(f'Insert {k} [day month year]>').split(' ')
# 			else:
# 				temp_element[k] = input(f'Insert {k} >')  
	
# 	for k, v in temp_element.items():
# 		if isinstance(v, list):
# 			index = ['released_day', 'released_month', 'released_year']
			
# 			data = xml.SubElement(child, k)
			
# 			i = 0
# 			for item in v:
# 				xml.SubElement(data, index[i]).text = item
# 				i += 1
# 		else:
# 			xml.SubElement(child, k).text = v
	
# 	with open(file_name, 'a', encoding='utf-8'):
# 					tree = xml.ElementTree(root)
# 					tree.write(file_name)


# def main():
# 	print("""
# .___                           __                       
# |   | _______  __ ____   _____/  |_  ___________ ___.__.
# |   |/    \  \/ // __ \ /    \   __\/  _ \_  __ <   |  |
# |   |   |  \   /\  ___/|   |  \  | (  <_> )  | \/\___  |
# |___|___|  /\_/  \___  >___|  /__|  \____/|__|   / ____|
# 		 \/          \/     \/                   \/     
# """)
	
# 	input('Press enter to continue >')
	
# 	while True:
# 		clear(user_os)
# 		print('Menu:'+
# 			'\n\t1 - Add'+
# 			'\n\t2 - Update'+
# 			'\n\t3 - Delete'+
# 			'\n\t4 - Consult'+
# 			'\n\t5 - Calculate'+
# 			'\n[q] for exit the program')
# 		in_user = input('>')
		
# 		if 'q' == in_user.lower():
# 			print('Exiting program...')
# 			break
		
# 		elif '1' == in_user:
# 			add(file_name)
# 			input('Press enter to continue >')
		
# 		elif '2' == in_user:
# 			update(file_name)
# 			input('Press enter to continue >')

		
# 		elif '3' == in_user:
# 			delete(file_name)
# 			input('Press enter to continue >')

		
# 		elif '4' == in_user:
# 			show(file_name)
# 			input('Press enter to continue >')
		
# 		elif '5' == in_user:
# 			calculate(file_name)
# 			input('Press enter to continue >')
# 		else:
# 			pass


# if __name__ == '__main__':
# 	main()
