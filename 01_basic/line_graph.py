import matplotlib.pyplot as plt

x = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
y = [1, 20, 33, 40, 5, 61, 73]

z = [34, 2, 5,7, 73,2, 3]
plt.title("Bakery Data")
plt.xlabel("Days of the Week")  
plt.ylabel("Number of Breads Sold")
plt.grid(True)
plt.plot(x, y , marker ='o', linestyle ='--', color ='blue', label= '2025 sales')
plt.plot(x, z,marker ='*', linestyle ='--',  color ='orange' , label= '2024 sales')
plt.legend()
plt.xticks(rotation=45)

plt.yticks(range(0, 81, 10))
plt.show()