from tkinter import *
import psycopg2

root = Tk()
root.title('Výpočet BMI')
root.geometry('250x250')
root.resizable(False, False)

# Function
def calculate_bmi(weight, height):
	text_result = ''
	bmi = round(float(weight)/float(height)**2, 2)
	if bmi < 18.5:
		text_result = 'podváha'
	elif bmi < 24.9:
		text_result = 'normal'
	elif bmi < 29.9:
		text_result = 'nadváha'
	elif bmi < 34.9:
		text_result = 'obezita'
	elif bmi >= 34.9:
		text_result = 'extrémní obezita'

	# výsledky do labelu
	label_user_result_1['text'] = bmi
	label_user_result_2['text'] = text_result

	insert_data(bmi, text_result)

def check_dot(number):
	number_string = str(number)
	if ',' in number_string:
		return number_string.replace(',', '.')
	return number

def insert_data(bmi_n, bmi_t):
	connection = psycopg2.connect(
		dbname='health',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)
	cur = connection.cursor()

	query = '''INSERT INTO bmi(bmi_number, bmi_text) values (%s, %s)'''

	cur.execute(query, (bmi_n, bmi_t))
	connection.commit()
	connection.close()

def count_all_data():
	connection = psycopg2.connect(
		dbname='health',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)
	cur = connection.cursor()
	query = '''SELECT COUNT(bmi_id) FROM bmi'''
	cur.execute(query)
	count = cur.fetchone()
	connection.close()
	return count[0]

# general Label
label_general = Label(root, text='Výpočet BMI')
label_general.grid(row=0, column=1)

# weight section
label_weight = Label(root, text='Zadejte váhu (kg):')
label_weight.grid(row=1, column=0)

entry_weight = Entry(root)
entry_weight.grid(row=1, column=1)

# height section
label_height = Label(root, text='Zadejte výšku (m):')
label_height.grid(row=2, column=0)

entry_height = Entry(root)
entry_height.grid(row=2, column=1)

# button
button = Button(root, text='Vypočítat', command=lambda:calculate_bmi(
	check_dot(entry_weight.get()), check_dot(entry_height.get())))
button.grid(row=3, column=1)

# result seciton
label_result_1 = Label(root, text='Číselný výsledek:')
label_result_1.grid(row=4, column=0)

label_user_result_1 = Label(root)
label_user_result_1.grid(row=4, column=1)

label_result_2 = Label(root, text='Textový výsledek:')
label_result_2.grid(row=5, column=0)

label_user_result_2 = Label(root,)
label_user_result_2.grid(row=5, column=1)

label_count_text = Label(root, text='Počet uživatelů:')
label_count_text.grid(row=6, column=0)

label_count_number = Label(root, text=count_all_data())
label_count_number.grid(row=6, column=1)

root.mainloop()