# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    # Task 2: Implement Getters and Setters
    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name
    
    def set_allocated_budget(self, new_allocated_budget):
        self.__allocated_budget = new_allocated_budget
    
    # Task 3: Add Budget Functionality
    def add_expense(self, amount):
        if 0 < amount <= self.get_allocated_budget():
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            print(f"Expense of {amount} added.")
        else:
            print("Invalid expense amount.")

    # Task 4: Display Budget Details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}, Allocated Budget: {self.__allocated_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()