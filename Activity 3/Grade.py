score1 = float(input("What is your score on assignment 1?\n"))
weight1 = float(input("What is the weightage of this assignment?\n"))
                      
score2 = float(input("What is your score on assignment 2?\n"))
weight2 = float(input("What is the weightage of this assignment?\n"))

score3 = float(input("What is your score on assignment 3?\n"))
weight3 = float(input("What is the weightage of this assignment?\n"))

score4 = float(input("What is your score on assignment 4?\n"))
weight4 = float(input("What is the weightage of this assignment?\n"))

final = score1*weight1 + score2*weight2 + score3*weight3 + score4*weight4
print("Your final grade calculated is:", final)
