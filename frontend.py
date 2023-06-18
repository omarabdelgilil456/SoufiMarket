
import backend

import tkinter
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime


class Products:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Super Market")
        self.window.geometry("550x600")
        self.window.config(background="black", padx=10, pady=10)

        title = tkinter.Label(text="Market", font=('Times New Roman', 50, 'bold'), bg="black", fg="cyan")
        title.grid(row=0, column=0)

        switch = tkinter.Label(text="switch to employees : ", font=('Times New Roman', 16, 'bold'), bg="black", fg="cyan")
        switch.grid(row=1, column=0)
        self.employees_button = tkinter.Button(self.window, text="Switch to Employees", width=16,
                                               command=self.switch_to_employees)
        self.employees_button.grid(row=1, column=2)

        self.product_name = tkinter.Label(text="product name:", font=('Times New Roman', 16, 'normal'), bg="black",
                                          fg="white")
        self.product_name.grid(row=2, column=0, padx=20, pady=10)
        self.p_name_entry = tkinter.Entry(self.window)
        self.p_name_entry.grid(row=2, column=2)

        self.product_comp = tkinter.Label(text="product manufacturer:", font=('Times New Roman', 16, 'normal'), bg="black",
                                          fg="white")
        self.product_comp.grid(row=3, column=0, padx=20, pady=10)
        self.p_comp_entry = tkinter.Entry(self.window)
        self.p_comp_entry.grid(row=3, column=2)

        self.product_price = tkinter.Label(text="product price:", font=('Times New Roman', 16, 'normal'), bg="black",
                                           fg="white")
        self.product_price.grid(row=4, column=0, padx=20, pady=10)
        self.p_price_entry = tkinter.Entry(self.window)
        self.p_price_entry.grid(row=4, column=2)

        self.product_manDate = tkinter.Label(text="product manufacture date:", font=('Times New Roman', 16, 'normal'),
                                             bg="black", fg="white")
        self.product_manDate.grid(row=5, column=0, padx=20, pady=10)
        self.p_man_entry = DateEntry(self.window, width=16, date_pattern='yyyy-mm-dd')
        self.p_man_entry.grid(row=5, column=2)

        self.product_expDate = tkinter.Label(text="product expiration date:", font=('Times New Roman', 16, 'normal'),
                                             bg="black", fg="white")
        self.product_expDate.grid(row=6, column=0, padx=20, pady=10)
        self.p_exp_entry = DateEntry(self.window, width=16, date_pattern='yyyy-mm-dd')
        self.p_exp_entry.grid(row=6, column=2)

        self.view_b = tkinter.Button(self.window, text="View all", width=16, command=self.view_products)
        self.view_b.grid(row=7, column=0, padx=40)

        self.search_b = tkinter.Button(self.window, text="search product", width=16, command=self.search)
        self.search_b.grid(row=8, column=0, padx=40)

        self.add_b = tkinter.Button(self.window, text="add product", width=16, command=self.add_product)
        self.add_b.grid(row=9, column=0, padx=40)

        self.update_b = tkinter.Button(self.window, text="update product", width=16, command=self.update_product)
        self.update_b.grid(row=10, column=0, padx=40)

        self.delete_b = tkinter.Button(self.window, text="delete product", width=16, command=self.delete_product)
        self.delete_b.grid(row=11, column=0, padx=40)

        self.exit_b = tkinter.Button(self.window, text="Exit", width=16, command=self.exit_app)
        self.exit_b.grid(row=12, column=0, padx=40)

        self.list = tkinter.Listbox(self.window, height=12, width=40)
        self.list.grid(row=7, column=1, rowspan=7, columnspan=4)
        self.scroll = tkinter.Scrollbar(self.window)
        self.scroll.grid(row=7, column=6, rowspan=7, sticky=tkinter.NS)
        self.list.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list.yview)
        self.list.bind('<<ListboxSelect>>', self.get_selected_row)



        self.window.mainloop()

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list.curselection()[0]
            selected_tuple = self.list.get(index)
            man_date = datetime.datetime.strptime(selected_tuple[3], '%Y-%m-%d').date()
            exp_date = datetime.datetime.strptime(selected_tuple[4], '%Y-%m-%d').date()
            self.p_name_entry.delete(0, tkinter.END)
            self.p_name_entry.insert(tkinter.END, selected_tuple[1])
            self.p_price_entry.delete(0, tkinter.END)
            self.p_price_entry.insert(tkinter.END, selected_tuple[2])
            self.p_man_entry.delete(0, tkinter.END)
            self.p_man_entry.insert(tkinter.END, man_date)
            self.p_exp_entry.delete(0, tkinter.END)
            self.p_exp_entry.insert(tkinter.END, exp_date)
            self.p_comp_entry.delete(0, tkinter.END)
            self.p_comp_entry.insert(tkinter.END, selected_tuple[5])
        except IndexError:
            messagebox.showinfo("Alert!", "Nothing to select!")

    def view_products(self):
        self.list.delete(0, tkinter.END)
        for row in backend.view_product():
            self.list.insert(tkinter.END, row)

    def delete_product(self):
        try:
            backend.delete_product(selected_tuple[0])
            self.view_products()
        except NameError:
            messagebox.showinfo("Alert!", "Nothing to delete!")

    def search(self):
        flag = 0
        self.list.delete(0, tkinter.END)
        for row in backend.search_product(p_name=self.p_name_entry.get(), p_price=self.p_price_entry.get(),
                                          p_comp=self.p_comp_entry.get()):
            self.list.insert(tkinter.END, row)
            flag = 1
        if flag == 0:
            messagebox.showinfo("Sorry!", "Nothing found!")

    def add_product(self):
        if self.p_name_entry.get() != "" and self.p_comp_entry.get() != "":
            backend.insert_product(self.p_name_entry.get(), self.p_price_entry.get(), self.p_man_entry.get(),
                                   self.p_exp_entry.get(), self.p_comp_entry.get())
            messagebox.showinfo("Alert!", "Item added successfully!")
        else:
            messagebox.showinfo("Alert!", "Please fill all empty fields!")

    def update_product(self):
        try:
            backend.update_product(selected_tuple[0], self.p_name_entry.get(), self.p_price_entry.get(),
                                   self.p_man_entry.get(), self.p_exp_entry.get(), self.p_comp_entry.get())
            messagebox.showinfo("Alert!", "Item updated successfully!")
            self.view_products()
        except NameError:
            messagebox.showinfo("Alert!", "Something went wrong!")

    def exit_app(self):
        self.window.destroy()

    def switch_to_employees(self):
        self.window.destroy()
        Employees()


class Employees:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Super employees")
        self.window.geometry("500x500")
        self.window.config(background="black", padx=10, pady=10)

        title = tkinter.Label(text="Market", font=('Times New Roman', 50, 'bold'), bg="black", fg="cyan")
        title.grid(row=0, column=0)

        switch = tkinter.Label(text="switch to products : ", font=('Times New Roman', 16, 'bold'), bg="black",
                               fg="cyan")
        switch.grid(row=1, column=0)
        self.products_button = tkinter.Button(self.window, text="Switch to products", width=16,
                                              command=self.switch_to_products)
        self.products_button.grid(row=1, column=2, pady=10)

        self.employee_name = tkinter.Label(text="employee name:", font=('Times New Roman', 16, 'normal'), bg="black",
                                          fg="white")
        self.employee_name.grid(row=2, column=0, padx=20, pady=10)
        self.e_name_entry = tkinter.Entry(self.window)
        self.e_name_entry.grid(row=2, column=2)

        self.employee_age = tkinter.Label(text="employee age:", font=('Times New Roman', 16, 'normal'), bg="black",
                                          fg="white")
        self.employee_age.grid(row=3, column=0, padx=20, pady=10)
        self.e_age_entry = tkinter.Entry(self.window)
        self.e_age_entry.grid(row=3, column=2)

        self.employee_salary = tkinter.Label(text="employee salary:", font=('Times New Roman', 16, 'normal'), bg="black",
                                             fg="white")
        self.employee_salary.grid(row=4, column=0, padx=20, pady=10)
        self.e_salary_entry = tkinter.Entry(self.window)
        self.e_salary_entry.grid(row=4, column=2)


        self.view_b = tkinter.Button(self.window, text="View all", width=16, command=self.view_employees)
        self.view_b.grid(row=7, column=0, padx=40)

        self.search_b = tkinter.Button(self.window, text="search employee", width=16, command=self.search)
        self.search_b.grid(row=8, column=0, padx=40)

        self.add_b = tkinter.Button(self.window, text="add employee", width=16, command=self.add_employee)
        self.add_b.grid(row=9, column=0, padx=40)

        self.update_b = tkinter.Button(self.window, text="update employee", width=16, command=self.update_employee)
        self.update_b.grid(row=10, column=0, padx=40)

        self.delete_b = tkinter.Button(self.window, text="delete employee", width=16, command=self.delete_employee)
        self.delete_b.grid(row=11, column=0, padx=40)

        self.exit_b = tkinter.Button(self.window, text="Exit", width=16, command=self.exit_app)
        self.exit_b.grid(row=12, column=0, padx=40)

        self.list = tkinter.Listbox(self.window, height=12, width=40)
        self.list.grid(row=7, column=1, rowspan=7, columnspan=4)
        self.scroll = tkinter.Scrollbar(self.window)
        self.scroll.grid(row=7, column=6, rowspan=7, sticky=tkinter.NS)
        self.list.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list.yview)
        self.list.bind('<<ListboxSelect>>', self.get_selected_row)


        self.window.mainloop()

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list.curselection()[0]
            selected_tuple = self.list.get(index)
            self.e_name_entry.delete(0, tkinter.END)
            self.e_name_entry.insert(tkinter.END, selected_tuple[1])
            self.e_salary_entry.delete(0, tkinter.END)
            self.e_salary_entry.insert(tkinter.END, selected_tuple[2])
            self.e_age_entry.delete(0, tkinter.END)
            self.e_age_entry.insert(tkinter.END, selected_tuple[3])
        except IndexError:
            messagebox.showinfo("Alert!", "Nothing to select!")

    def view_employees(self):
        self.list.delete(0, tkinter.END)
        for row in backend.view_employee():
            self.list.insert(tkinter.END, row)

    def delete_employee(self):
        try:
            backend.delete_employee(selected_tuple[0])
            self.view_employees()
        except NameError:
            messagebox.showinfo("Alert!", "Nothing to delete!")

    def search(self):
        flag = 0
        self.list.delete(0, tkinter.END)
        for row in backend.search_employee(e_name=self.e_name_entry.get(), e_age=self.e_salary_entry.get(),
                                           e_salary=self.e_age_entry.get()):
            self.list.insert(tkinter.END, row)
            flag = 1
        if flag == 0:
            messagebox.showinfo("Sorry!", "Nothing found!")

    def add_employee(self):
        if self.e_name_entry.get() != "" and self.e_age_entry.get() != "":
            backend.insert_employee(self.e_name_entry.get(), self.e_salary_entry.get(), self.e_age_entry.get())
            messagebox.showinfo("Alert!", "Item added successfully!")
        else:
            messagebox.showinfo("Alert!", "Please fill all empty fields!")

    def update_employee(self):
        try:
            backend.update_employee(selected_tuple[0], self.e_name_entry.get(), self.e_salary_entry.get(),
                                    self.e_age_entry.get())
            messagebox.showinfo("Alert!", "Item updated successfully!")
            self.view_employees()
        except NameError:
            messagebox.showinfo("Alert!", "Something went wrong!")

    def switch_to_products(self):
        self.window.destroy()
        Products()

    def exit_app(self):
        self.window.destroy()


if __name__ == '__main__':
    Products()









