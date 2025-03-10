class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Client with such ID already registered")
        self.clients[client_id] = name
        self.deposits[client_id] = None

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError("Client not registered")
        if self.deposits[client_id] is not None:
            raise ValueError("Client already has opened deposit")
        self.deposits[client_id] = {
            'start_balance': start_balance,
            'years': years,
            'current_balance': start_balance
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.deposits or self.deposits[client_id] is None:
            raise ValueError("Deposit for current client not found")

        deposit = self.deposits[client_id]
        start_balance = deposit['start_balance']
        years = deposit['years']
        monthly_rate = 0.10 / 12
        months = years * 12

        final_balance = start_balance * (1 + monthly_rate) ** months
        return round(final_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits or self.deposits[client_id] is None:
            raise ValueError("Deposit for current client not found")

        final_balance = self.calc_deposit_interest_rate(client_id)
        self.deposits[client_id] = None
        return final_balance
