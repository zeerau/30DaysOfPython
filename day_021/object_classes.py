import statistics
from collections import Counter

class Statistics:
    
    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return statistics.mean(self.data)
    
    def median(self):
        return statistics.median(self.data)
    
    def mode(self):
        return statistics.mode(self.data)
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def variance(self):
        return statistics.variance(self.data)
    
    def stdev(self):
        return statistics.stdev(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def percentile(self, p):
        return statistics.quantiles(self.data, n=100)[p]
    
    def freq_dist(self):
        freq = Counter(self.data)
        return dict(freq)

sample = [2, 4, 5, 6, 7, 8, 8, 9, 10, 12, 14, 15, 15, 17, 18, 19, 20, 20, 20, 22]

stats = Statistics(sample)

print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Range:", stats.range())
print("Variance:", stats.variance())
print("Standard deviation:", stats.stdev())
print("Minimum:", stats.min())
print("Maximum:", stats.max())
print("Count:", stats.count())
print("50th percentile:", stats.percentile(50))
print("Frequency distribution:", stats.freq_dist())




class PersonAccount:
    
    def __init__(self, firstname, lastname, incomes=None, expenses=None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes or {}
        self.expenses = expenses or {}
        
    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())
    
    def account_info(self):
        return f"Account for {self.firstname} {self.lastname} - Balance: {self.account_balance():.2f}"
    
    def add_income(self, description, amount):
        self.incomes[description] = amount
        
    def add_expense(self, description, amount):
        self.expenses[description] = amount
        
    def account_balance(self):
        return self.total_income() - self.total_expense()


# Create a new person account with some initial incomes and expenses
person = PersonAccount("John", "Doe", {"Salary": 5000, "Freelance": 2000}, {"Rent": 1000, "Food": 500})

# Add a new income and expense item
person.add_income("Bonus", 1000)
person.add_expense("Entertainment", 200)

# Print the account information and balance
print(person.account_info())
print("Total Income:", person.total_income())
print("Total Expense:", person.total_expense())
print("Account Balance:", person.account_balance())


