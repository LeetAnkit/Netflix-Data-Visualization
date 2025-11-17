import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y= [10, 20, 25, 30, 40]

#savfig is used to save the figure in your desired format
# syntax of savefig is plt.savefig("filename.format")
plt.plot(x, y, marker='o', linestyle='--', color='green')
plt.title("Sales Data")
plt.xlabel("Days")
plt.ylabel("Sales in USD")
plt.savefig("sales_data_chart.png", dpi =300, bbox_inches='tight')  # Saves the figure as a PNG file
plt.savefig("sales_data_chart.pdf")  # Saves the figure as a PDF file
plt.show()