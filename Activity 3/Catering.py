cheesecake = int(input("How many cheesecakes will you be making today?"))
cakes = int(input("How many chocolate cakes will you be making today?"))
cupcakes = int(input("How many cupcake sets are will you be making today?"))

eggs = cheesecake * 2 + cakes * 2 + cupcakes
flour = cheesecake + cakes + 0.5 * cupcakes
milk = cheesecake*250 + cakes * 250 + cupcakes * 150
chocolate = cakes*200 + cupcakes*100
butter = cakes*100 + cupcakes*50
sugar = cheesecake * 100 + cakes * 150 + cupcakes * 100
cheese = cheesecake*200 + cupcakes * 100

print("Eggs:", eggs)
print("Flour:", flour)
print("Milk:", milk)
print("Chocolate :", chocolate)
print("Butter:", butter)
print("Sugar:", sugar)
print("Cream Cheese:", cheese)
