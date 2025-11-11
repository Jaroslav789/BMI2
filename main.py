from tkinter import *
import psycopg2

root = Tk()
root.title('Výpočet BMI')
root.geometry('250x250')
root.resizable(False, False)

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
button = Button(root, text='Vypočítat')
button.grid(row=3, column=1)

# result seciton
label_result_1 = Label(root, text='Číselný výsledek:')
label_result_1.grid(row=4, column=0)

label_user_result_1 = Label(root, text='DOPLNIT')
label_user_result_1.grid(row=4, column=1)

label_result_2 = Label(root, text='Textový výsledek:')
label_result_2.grid(row=5, column=0)

label_user_result_2 = Label(root, text='DOPLNIT')
label_user_result_2.grid(row=5, column=1)

label_count_text = Label(root, text='Počet uživatelů:')
label_count_text.grid(row=6, column=0)

label_count_number = Label(root, text='DOPLNIT')
label_count_number.grid(row=6, column=1)

root.mainloop()