# inventory.py
# -------------------------------
# Simple Inventory Management App
# Author: Rafael
# Description:
#   This CLI app lets you add, remove, update, search, and save products with categories.
#   Categories: drink, cleaning, food
#   Data is saved to 'inventory.txt' and can be read back.
# -------------------------------
product = {}
category = ["drink", "cleaning", "food"]
while True:
    print("1) Add product")
    print("2) Remove product")
    print("3) Show inventory")
    print("4) Update product price")
    print("5) Find product")
    print("6) Save product")
    print("7) Read product")
    print("0) Quit")

    print("_" * 20)

    option = input("Enter option: ")

    print("_" * 20)

    match option:
        case "1":
            name = input("Enter product name: ")
            try:
                price = int(input("Enter product price: "))
                count = int(input("Enter product count: "))
                if price < 0 or count < 0:
                    print("Error: Invalid number")
                    print("_" * 20)
                    continue
            except ValueError:
                print("Error: Invalid number")
                print("_" * 20)
                continue
            print("Available categories: ")
            for cat in category:
                print("_", cat)

            chosen_category = input("Enter product category: ").lower()
            if chosen_category not in category:
                print("Error: Invalid category")
                print("_" * 20)
                continue
            product[name] = {
                "name" : name,
                "price" : price,
                "count" : count,
                "category" : chosen_category
            }
            print(f"{name} has added in inventory")
        case "2":
            remove = input("Enter product name to remove: ")
            if remove in product:
                del product[remove]
                print(f"{remove} removed as inventory")
            else:
                print("Error: Invalid name")
        case "3":
            print("1) All item")
            print("2) See category")
            chose = input("chose option: ")
            match chose:
                case "1":
                    if not product:
                        print("inventory is empty")
                    else:
                        for name in product:
                            info = product[name]
                            print(f"{name} category: {info['category']} | price: {info['price']} | count: {info['count']}")
                case "2":
                    print("Available categories: ")
                    for i, cat in enumerate(category, start=1):
                        print(f"{i} {cat}")
                    cat_index = int(input("Enter category (1-3): ")) - 1

                    if 0 <= cat_index < len(category):
                        selected_cat = category[cat_index]
                        found = False
                        for name, info in product.items():
                            if info.get("category") == selected_cat:
                                print(f"{name} price: {info['price']} | count: {info['count']}")
                                found = True
                        if not found:
                            print("No items found in category:", selected_cat)
                    else:
                        print("Error: Invalid category")
                case _:
                    print("Error: Invalid option")
                    continue
        case "4":
            update = input("Enter product name to update: ")
            if update in product:
                try:
                    price_update = int(input("Enter product price for update: "))
                    count_update = int(input("Enter product count for update: "))
                except ValueError:
                    print("Error: Invalid number")
                    continue
                if price_update < 0 or count_update < 0:
                    print("Error: Invalid number")
                    print("_" * 20)
                    continue
                product[update] = {
                "name" : update,
                "price" : price_update,
                "count" : count_update,
                "category" : product[update]["category"]
                }
                print(f"{update} updated in inventory")
            else:
                print("Error: Invalid name")
        case "5":
            find = input("Enter product name to find: ").lower()
            found = False
            for name, info in product.items():
                if find in name.lower():
                    print(f"{name} category: {info['category']} | price: {info['price']} | count: {info['count']}")
                    found = True
            if not found:
                print("Error: Invalid name")
        case "6":
            with open("../inventory.txt", "w") as file:
                for i, (name, info) in enumerate(product.items(), start=1):
                    file.write(f"{i}. {name}: category: {info['category']} | price: {info['price']} | count: {info['count']}\n")
            print("file saved in inventory.txt")
        case "7":
            try:
                with open("../inventory.txt", "r") as file:
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("Error: Inventory file not found")
        case "0":
            left = input("Do you want to quit(y/n)").lower()
            if left == "y":
                print("Goodbye")
                break
            elif left == "n":
                print("you back in the app")
            else:
                print("Error: Invalid option")
        case _:
            print("Invalid option")
    print("_" * 20)