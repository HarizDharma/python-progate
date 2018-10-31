class MenuItem:
    def info(self):
        return self.name + ': $' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5
print(menu_item1.info())
menu_item2 = MenuItem()
menu_item2.name = 'Chocolate Cake'
menu_item2.price = 4
print(menu_item2.info())
