results = [1, 1, 2, 3, 3, 3, 4, 5]
x = sum(results) / len(results)
Jimmy_var_number = sum((xi - x) ** 2 for xi in results) / len(results)
print("The variance number is", Jimmy_var_number)
