from Inheritence.chef import Chef
class ChineseChef(Chef):   # Instead of pasting the while content of chef.py we can inherits its Cheff Object
                           # Where the Chinese can have all the qualities of normal chef as well

    def make_special_dish(self):  # This function will overwrites the Inherited function
        print("The Chef makes Orange Chicken")

    def make_fried_rice(self):
        print("The Chef makes fried rice")