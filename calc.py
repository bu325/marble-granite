def area_m2(length_m, width_m, pieces=1):
    """Calculates the area in square meters."""
    return float(length_m) * float(width_m) * float(pieces)

def purchase_cost(items):
    """Calculates the total purchase cost from a list of invoice items."""
    total_cost = 0
    for item in items:
        total_cost += item.area_m2 * item.buy_price_m2
    return total_cost

def sell_price(items):
    """Calculates the total selling price from a list of invoice items."""
    total_sell_price = 0
    for item in items:
        total_sell_price += item.area_m2 * item.sell_price_m2
    return total_sell_price

def pre_discount_total(sell_price_materials, delivery_fee_billed, install_fee_billed):
    """Calculates the total before discount, including material sell price and billed fees."""
    return sell_price_materials + delivery_fee_billed + install_fee_billed

def discount_amount(total_before_discount, discount_rate):
    """Calculates the discount amount."""
    return total_before_discount * (discount_rate / 100)

def taxable_base(total_before_discount, discount_amount):
    """Calculates the base amount subject to tax."""
    return total_before_discount - discount_amount

def tax_amount(taxable_base_amount, tax_rate):
    """Calculates the tax amount."""
    return taxable_base_amount * (tax_rate / 100)

def final_total(taxable_base_amount, tax_amount_val):
    """Calculates the final total after tax."""
    return taxable_base_amount + tax_amount_val

def profit_margin(sell_price_materials, fees_billed, purchase_cost_materials, direct_extra_costs=0):
    """Calculates the profit margin for an invoice."""
    return (sell_price_materials + fees_billed) - purchase_cost_materials - direct_extra_costs

def net_profit(profit_margin_val, workers_wages, extra_expenses):
    """Calculates the net profit."""
    return profit_margin_val - workers_wages - extra_expenses


