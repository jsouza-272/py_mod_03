import sys


def inventory_system_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ==")
    s = 0
    for p in inventory.values():
        s += p
    print("Total items in inventory:", s)
    print("Unique item types:", len(inventory))


def current_inventory(invetory: dict) -> None:
    print("=== Current Inventory ===")
    total = 0
    for p in inventory.values():
        total += p
    for key, value in inventory.items():
        print(f"{key}: {value} units {((value * 100) / total):.1f}%")


def inventory_statistics(invetory: dict) -> None:
    print("=== Inventory Statistics ===")
    vmx, vmn, kmx, kmn = -1, 1000, 0, 0
    for k, v in inventory.items():
        if v > vmx:
            kmx = k
            vmx = v
        if v < vmn:
            kmn = k
            vmn = v
    print(f"Most abundant: {kmx} ({vmx} units)")
    if vmn == 1:
        print(f"Least abundant: {kmn} ({vmn} unit)")
    else:
        print(f"Least abundant: {kmn} ({vmn} units)")


def management_suggestions(invetory: dict) -> None:
    print("=== Management Suggestions ===")
    restock = []
    for k, v in inventory.items():
        if v == 1:
            restock.append(k)
    print(f"Restock needed: {restock}")


def dictionary_properties_demo(invetory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    keys = []
    for k in inventory.keys():
        keys.append(k)
    values = []
    for v in inventory.values():
        values.append(v)
    k = inventory.get("sword")
    if k:
        exist = True
    else:
        exist = False
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - 'sword' in inventory: {exist}")


if __name__ == "__main__":
    inventory = dict()
    try:
        for av in sys.argv[1:]:
            a = av.split(':')
            b = {a[0]: int(a[1])}
            inventory.update(b)
        inventory_system_analysis(inventory)
        print()
        current_inventory(inventory)
        print()
        inventory_statistics(inventory)
        print()
        management_suggestions(inventory)
        print()
        dictionary_properties_demo(inventory)
    except Exception:
        print(f"Usage: python3 {sys.argv[0]} <item_name>:<item_qnt> ...")
