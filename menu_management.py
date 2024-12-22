def update_menu(menu, add_item=None, remove_item=None):
    if add_item:
        menu.append(add_item)
    if remove_item:
        if remove_item in menu:
            menu.remove(remove_item)
        else:
            return f"{remove_item} does not exist in the menu."
    return menu


def check_availability(menu, check_item):
    return f"Availability: {check_item} is available" if check_item in menu else f"{check_item} is not available"


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

menu = update_menu(initial_menu, add_item, remove_item)
print(f"Updated menu: {menu}")
print(check_availability(menu, check_item))