favorite_foods = {"John" : "Wings", "Steven" : "Burgers", "Mitch" : "Fries"}
favorite_foods["Mike"] = "Carrots"

print(favorite_foods)

for key,value in favorite_foods.items():
    print(key + "'s favorite food is " + value)

if "Mary" in favorite_foods:
    print("Mary in dictionary")
else:
    favorite_foods["Mary"] = "Cake"

foods = ["pizza" , "tikka masala", "pizza", "bagels", "bagels", "ice cream", "pizza"]
food_counts = {}

for x in foods:
    if x not in food_counts.keys():
        food_counts[x] = foods.count(x)


keys = ["one", "two", "three"]
nums = {keys[i]: i + 1 for i in range(len(keys))}

print(nums)

test = {1:11 , 2: 22}

for x in test:
    print(x)

