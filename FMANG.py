total_Income = 0
total_Expenses = 0
yestotal_Savings = 0

mainTable = []
table_raw = 1

class Event:
    def __init__(self, name, description, state, amount):
        self.name = name
        self.description = description
        self.state = state
        self.amount = amount

    
    def create_data_row(name, description, state, amount):
        mainTable.append({'ID': str(table_raw), 'name': name, 'description': description, 'state': state, 'amount': amount})


    def sum_totals(state, amount):
        global total_Income, total_Expenses, total_Savings
        if state == 'income':
            total_Income += int(amount)
        elif state == 'expense':
            total_Expenses += int(amount)
        elif state == 'saving':
            total_Savings += int(amount)



for raw in mainTable:
    print(f"|{raw['name']}|{raw['description']}|{raw['state']}|{raw['amount']}|")


