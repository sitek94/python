class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def get_expenses(self):
        total = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                total += entry['amount']
        return total

    def __str__(self):
        # Title
        stars = '*' * int((30 - len(self.name)) / 2)
        output = stars + self.name + stars + '\n'

        # Ledger entries
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)
            amount = "{:7.2f}".format(entry['amount'])
            output += description + amount + '\n'

        # Total
        output += 'Total: ' + str(self.get_balance())

        return output


def create_spend_chart(categories):
    output = 'Percentage spent by category\n'

    # Calculate percentage for each category
    total = sum(c.get_expenses() for c in categories)
    percentages = []
    for c in categories:
        percentages.append(round(c.get_expenses() / total * 100))

    # Draw chart
    for n in range(11):
        line = str(100 - n * 10).rjust(3) + '| '

        for i, c in enumerate(categories):
            line += 'o' if percentages[i] >= 100 - n * 10 else ' '
            line += '  '
        output += line + '\n'

    # Print separator
    output += '    -' + '---' * len(categories) + '\n'

    # Print labels
    longest_name_length = max(len(c.name) for c in categories)
    for n in range(longest_name_length):
        line = '     '
        for c in categories:
            line += c.name[n] if n < len(c.name) else ' '
            line += '  '
        output += line + '\n'

    return output


food = Category("Food")
food.deposit(900, "deposit")
food.withdraw(105.55)

entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40)

business = Category("Business")
business.deposit(900, "deposit")
business.withdraw(10.99)

print(repr(create_spend_chart([business, food, entertainment])))
