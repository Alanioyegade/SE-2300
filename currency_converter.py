import requests

# ----------------------------------------
# Country to Currency Mapping (Global Dictionary)
# ----------------------------------------
COUNTRY_TO_CURRENCY = {
    "Nigeria": "NGN",
    "South Africa": "ZAR",
    "Egypt": "EGP",
    "Kenya": "KES",
    "Ghana": "GHS",
    "Tanzania": "TZS",
    "Uganda": "UGX",
    "Morocco": "MAD",
    "Algeria": "DZD",
    "Angola": "AOA",
    "Ethiopia": "ETB",
    "Senegal": "XOF",
    "Botswana": "BWP",
    "Namibia": "NAD",
    "Zambia": "ZMW",
    "Zimbabwe": "ZWL",
    "Togo": "XOF",
    "Cameroon": "XAF",
    "United States": "USD",
    "Canada": "CAD",
    "Mexico": "MXN",
    "United Kingdom": "GBP",
    "Germany": "EUR",
    "France": "EUR",
    "Italy": "EUR",
    "Spain": "EUR",
    "Switzerland": "CHF",
    "China": "CNY",
    "Japan": "JPY",
    "India": "INR",
    "South Korea": "KRW",
    "Singapore": "SGD",
    "Saudi Arabia": "SAR",
    "Australia": "AUD",
    "New Zealand": "NZD",
    "Brazil": "BRL",
    "Argentina": "ARS",
    "Chile": "CLP"
}

# ----------------------------------------
# Custom CurrencyConverter Class 
# ----------------------------------------
class CurrencyConverter:

    def __init__(self):
        self.conversion_history = []

# This method checks if the user entered a country name.

    def get_currency_code(self, user_input):
        formatted_input = user_input.strip().title()
        if formatted_input in COUNTRY_TO_CURRENCY:
            return COUNTRY_TO_CURRENCY[formatted_input]
        return formatted_input.upper()

# This method connects to the Exchange Rate API

    def fetch_live_rates(self, base_currency="USD"):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            return data["rates"]
        except requests.RequestException:
            return None

# This method performs the currency conversion.

    def convert_currency(self, amount, from_code, to_code, rates):
        if from_code != "USD":
            if from_code not in rates:
                return None
            amount_in_usd = amount / rates[from_code]
        else:
            amount_in_usd = amount

        if to_code not in rates:
            return None

        converted_amount = amount_in_usd * rates[to_code]
        return round(converted_amount, 2)

# Add to history

    def add_to_history(self, record):
        self.conversion_history.append(record)

# Displays all previous conversions. If no history exists, it informs the user.

    def show_history(self):
        if not self.conversion_history:
            print("No conversions recorded.")
        else:
            print("\n--- Conversion History ---")
            for record in self.conversion_history:
                print(record)


# ----------------------------------------
# Main Program
# It handles user input, validation, and calls class methods.
# ----------------------------------------
def main():
    converter = CurrencyConverter()

    print("=== Welcome to the Smart Currency Converter ===\n")

    while True:
        try:
            amount_to_convert = float(input("Enter amount to convert: "))
            if amount_to_convert <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

# Get source currency or country

    source_input = input("Enter source country or currency code: ")
    source_currency_code = converter.get_currency_code(source_input)

# Get up to 5 target currencies

    targets_input = input("Enter target countries/currency codes (up to 5, separated by commas): ")
    target_currency_codes = [item.strip() for item in targets_input.split(",")][:5]

# Fetch exchange rates from API

    exchange_rates = converter.fetch_live_rates()

# Check if API call failed

    if not exchange_rates:
        print("Error retrieving exchange rates. Please try again later.")
        return

    print("\n--- Conversion Results ---")

# Loop through each target currency

    for target in target_currency_codes:
        target_code = converter.get_currency_code(target)
        converted_amount = converter.convert_currency(
            amount_to_convert,
            source_currency_code,
            target_code,
            exchange_rates
        )

# Handle unsupported currency
        
        if converted_amount is None:
            print(f"Conversion failed for {target_code}. Unsupported currency.")
        else:
            result_string = f"{amount_to_convert} {source_currency_code} = {converted_amount} {target_code}"
            print(result_string)
            # Save successful conversion to history
            converter.add_to_history(result_string)

# Ask user if they want to see history
    
    show_history_choice = input("\nDo you want to see your conversion history? (yes/no): ").lower()

    if show_history_choice.startswith("y"):
        converter.show_history()


if __name__ == "__main__":
    main()

