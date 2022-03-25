print("*" * 20 + " SHOPPING LIST " + "*" * 20)
print("""ADD ITEMS TO SHOPPING LIST!!
PLEASE TYPE \"DONE\" IF YOU FINISHED LISTING ALL ITEMS""")
print("")
print("")

count = 1
limit = 100
item_list = []
item_length = 0
total_price = 0
total_items = 0


while count <= limit:
    item = input(f"{count}. ")
    count += 1

    item_list.append(item)
    if item.upper() != "DONE":
        price = int(input("ESTIMATED PRICE: "))
        quantity = int(input("QUANTITY: "))

        total_per_item = price * quantity
        total_price += total_per_item
        total_items += quantity
        print("TOTAL PRICE PER ITEM: " + str(total_per_item))
        print("")

    else:
        break


item_list.pop()
item_length = len(item_list)
print("")
print("TOTAL NUMBER OF ITEMS: " + str(total_items))
print("TOTAL ESTIMATED PRICE: " + str(total_price))
