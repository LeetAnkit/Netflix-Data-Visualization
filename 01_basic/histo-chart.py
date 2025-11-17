import matplotlib.pyplot as plt

scores = [55, 70, 75, 80, 85, 90, 95, 100, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
#bins define the range of scores for each bar we want to create
plt.xlabel("Score Ranges")
plt.ylabel("Number of Students")    
plt.hist(scores, bins=12, color='purple', edgecolor='black')
plt.show()