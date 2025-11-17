import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"] 
# y = [1, 20, 33, 40, 5, 61, 73]

# plt.subplot(1, 2, 1)
# plt.plot(x, y, marker='o', linestyle='--', color='blue')
# plt.title("Sales Data line Chart")     

# plt.subplot(1, 2, 2)
# plt.bar(x, y, color='orange')
# plt.title("Sales Data Bar Chart")
# #plt.tight_layout
# plt.show()


#professional Way to draw the subplots

fig, ax= plt.subplots(1, 2, figsize=(10, 4))

x=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"] 
y=[1, 20, 33, 40, 5, 61, 73]    
ax[0].plot(x, y, marker='o', linestyle='--', color='blue')
ax[0].set_title("Sales Data line Chart")    

ax[1].bar(x, y, color='orange')
ax[1].set_title("Sales Data Bar Chart")

fig.suptitle("Weekly Sales Overview", fontsize=16)
plt.tight_layout()
plt.show()



