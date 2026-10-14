number_of_items=int(input("enter the product count:"))
product_count_perbox=int(input("enter the box size:"))
total_boxes_needed=number_of_items//product_count_perbox
remaining_items=number_of_items%product_count_perbox
print("total boxes:",total_boxes_needed)
print("remaining items:",remaining_items)