import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [5000, 5500, 7000, 6000]


plt.pie(revenue, labels=regions, autopct='%1.1f%%',)
plt.title("Revenue Distribution by Region")
plt.show()