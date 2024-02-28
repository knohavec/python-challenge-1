import tkinter as tk

menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = []

def submit_order():
    menu_category = menu_category_var.get()
    menu_selection = menu_selection_var.get()
    quantity = quantity_var.get()

    if menu_category and menu_selection and quantity:
        if isinstance(menu[menu_category][menu_selection], dict):
            item_name = f"{menu_selection} - {list(menu[menu_category][menu_selection].keys())[0]}"
            price = list(menu[menu_category][menu_selection].values())[0]
        else:
            item_name = menu_selection
            price = menu[menu_category][menu_selection]
        
        order_list.append({
            "Item name": item_name,
            "Price": price,
            "Quantity": int(quantity)
        })
        update_order_list()
    else:
        status_label.config(text="Please select a menu category, item, and quantity.")


def update_order_list():
    order_list_text.delete(1.0, tk.END)
    for item in order_list:
        order_list_text.insert(tk.END, f"{item['Item name']} - ${item['Price']} - Quantity: {item['Quantity']}\n")
    total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
    total_cost_label.config(text=f"Total cost: ${total_cost:.2f}")

root = tk.Tk()
root.title("Resturant Order System")

menu_category_var = tk.StringVar()
menu_selection_var = tk.StringVar()
quantity_var = tk.StringVar()

menu_frame = tk.LabelFrame(root, text="Menu Selection")
menu_frame.pack(padx=10, pady=10)

menu_category_label = tk.Label(menu_frame, text="Menu Category:")
menu_category_label.grid(row=0, column=0, padx=5, pady=5)
menu_category_dropdown = tk.OptionMenu(menu_frame, menu_category_var, *menu.keys())
menu_category_dropdown.grid(row=0, column=1, padx=5, pady=5)

menu_selection_label = tk.Label(menu_frame, text="Menu Item:")
menu_selection_label.grid(row=1, column=0, padx=5, pady=5)
menu_selection_dropdown = tk.OptionMenu(menu_frame, menu_selection_var, "")
menu_selection_dropdown.grid(row=1, column=1, padx=5, pady=5)

quantity_label = tk.Label(menu_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(menu_frame, textvariable=quantity_var)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(menu_frame, text="Add To Cart", command=submit_order)
submit_button.grid(row=3, columnspan=2, padx=5, pady=5)

status_label = tk.Label(menu_frame, text="")
status_label.grid(row=4, columnspan=2, padx=5, pady=5)

order_list_text = tk.Text(root, height=10, width=50)
order_list_text.pack(padx=10, pady=10)

total_cost_label = tk.Label(root, text="")
total_cost_label.pack(padx=10, pady=5)

def update_menu_selection(*args):
    selected_category = menu_category_var.get()
    if selected_category:
        menu_selection_dropdown['menu'].delete(0, 'end')
        for item in menu[selected_category]:
            menu_selection_dropdown['menu'].add_command(label=item, command=tk._setit(menu_selection_var, item))
        menu_selection_var.set("")

menu_category_var.trace('w', update_menu_selection)

root.mainloop()
