import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [50, 55, 65, 70, 75, 80, 85, 90, 95, 100] 

hours_played = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
game_scores = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

#this is mainly used to show the relationship between two variables
plt.scatter(hours_studied, test_scores, color='green', marker='x')
plt.scatter(hours_played, game_scores, color='red', marker='o')
plt.legend(['Test Scores', 'Game Scores'])
plt.title("Hours Studied vs Test Scores")   
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")   
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()  
