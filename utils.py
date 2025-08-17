# app/core/utils.py

import locale

def format_currency(amount):
    # Set locale for Moroccan Dirham (MAD) formatting
    # This might need adjustment based on the specific system locale availability
    try:
        locale.setlocale(locale.LC_ALL, 'ar_MA.UTF-8') # Or 'fr_MA.UTF-8' or similar
    except locale.Error:
        # Fallback if locale not available
        pass

    # Format with Western Arabic Digits and two decimal places
    # Example: 1,500.00 د.م
    return f"{amount:,.2f} د.م".replace(",", " ") # Replace comma with space for thousands separator

def format_number(number):
    return f"{number}"


