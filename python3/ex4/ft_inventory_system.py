import sys


def ft_inventory_system():
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        return

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = parts[0]
        quantity_str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory.update({item_name: quantity})
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")

    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item in items_list:
        qty = inventory[item]
        percentage = (qty / total_qty) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_abundant_item = items_list[0]
    least_abundant_item = items_list[0]

    for item in items_list:
        if inventory[item] > inventory[most_abundant_item]:
            most_abundant_item = item
        if inventory[item] < inventory[least_abundant_item]:
            least_abundant_item = item

    print(
        f"Item most abundant: {most_abundant_item} "
        f"with quantity {inventory[most_abundant_item]}"
    )
    print(
        f"Item least abundant: {least_abundant_item} "
        f"with quantity {inventory[least_abundant_item]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
