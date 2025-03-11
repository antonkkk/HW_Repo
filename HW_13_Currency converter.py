class CurrencyConverter:
    def __init__(self, rates):
        self.exchange_rates = rates

    def exchange_currency(self, from_currency, amount, to_currency='BYN'):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Unsupported currency")
        byn_amount = amount * self.exchange_rates[from_currency]
        final_amount = round(byn_amount / self.exchange_rates[to_currency], 2)
        return final_amount, to_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


exchange_rates = {'USD': 3.269, 'EUR': 3.52, 'BYN': 1.0}
converter = CurrencyConverter(exchange_rates)

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Проверяем конвертацию в BYN:
print(converter.exchange_currency(vasya.currency, vasya.amount))  # (32.69, "BYN")
print(converter.exchange_currency(petya.currency, petya.amount))  # (17.60, "BYN")

# Конвертация в заданную валюту:
print(converter.exchange_currency(vasya.currency, vasya.amount, 'EUR'))  # (9.29, "EUR")
print(converter.exchange_currency(petya.currency, petya.amount, 'USD'))  # (5.38, "USD")
