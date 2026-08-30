# Part 1: Simple Currency Converter

expenses = {
    "Food": 500,
    "Travel": 1200,
    "Shopping": 2500,
    "Entertainment": 800
}

exchange_rate = 95.24  # 1 USD = 95.24 INR

print("Currency Conversion")
print("Exchange Rate: 1 USD =", exchange_rate, "INR")
print()

for category, amount_inr in expenses.items():
    amount_usd = amount_inr / exchange_rate
    print(f"{category}: ₹{amount_inr:.2f} → ${amount_usd:.2f}")