import matplotlib.pyplot as plt

products = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
sales_A = [150, 280, 200, 150, 400]
#++++++++++++++++++++++++ Bar Chart ++++++++++++++++++++++++++++++++++++++
plt.bar(products, sales_A, color='skyblue', label='Store A Sales')
plt.title("Fruit Sales Comparison") 
plt.xlabel("Fruits")
plt.ylabel("Number of Fruits Sold")
plt.legend()
plt.xticks(rotation=45)
plt.show()
