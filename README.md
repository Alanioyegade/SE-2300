# SE-2300
# Smart Currency Converter

## Project Description
The Smart Currency Converter is a command-line application that allows users to convert money from one currency to another using live exchange rates. Users can enter an amount, choose a source currency (or country), and select up to five target currencies. The program fetches real-time exchange rate data from an online API and displays accurate conversion results. It also keeps a session history of all conversions.

## How to Run the Program
1. Make sure you have **Python 3** installed on your computer.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the program files.
4. Install the required dependency:

5. Run the program:

6. Follow the prompts to enter the amount, source currency, and target currencies.

## Dependencies
- Python 3
- `requests` library (used to fetch live exchange rates from the API)

## Features and Notes
- Users can enter either a country name or a currency code.
- Supports multiple target currencies (up to 5 at a time).
- Validates user input to prevent negative numbers or invalid text entries.
- Handles unsupported currencies by displaying an error message for that specific conversion.
- Keeps a session history of all conversions, which the user can choose to view.
- Handles API errors gracefully by informing the user if live rates cannot be fetched.

