first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True],
                 ["Depak", "Medium", False]]
customer_data[2][-1] = False
customer_data[1].remove(False)
new_customer_data = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final = customer_data + new_customer_data
print(customer_data_final)
