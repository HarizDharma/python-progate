from menu_item import MenuItem


class Food(MenuItem):
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
