class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Client already exists")
        self.clients[client_id] = {'name': name}

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError("Client not found")
        if client_id in self.deposits:
            raise ValueError("Deposit already exists")
        self.deposits[client_id] = {
            'balance': start_balance,
            'years': years
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("Deposit not found")

        deposit = self.deposits[client_id]
        balance = deposit['balance']
        years = deposit['years']
        amount = balance * (1 + 0.05 / 12) ** (12 * years)
        return round(amount, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("Deposit not found")

        amount = self.calc_deposit_interest_rate(client_id)
        del self.deposits[client_id]
        return amount
