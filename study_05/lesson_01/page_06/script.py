from drink import Drink
from food import Food

food1 = Food('Sandwich', 5)
food1.calorie_count = 330
print(food1.info())
drink1 = Drink('Coffee', 3)
drink1.volume = 180
print(drink1.info())
