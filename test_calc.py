import unittest
from services.calc import area_m2, purchase_cost, sell_price, pre_discount_total, discount_amount, taxable_base, tax_amount, final_total, profit_margin, net_profit

class TestCalcFunctions(unittest.TestCase):

    def test_area_m2(self):
        self.assertAlmostEqual(area_m2(2, 3), 6.0)
        self.assertAlmostEqual(area_m2(2, 3, 2), 12.0)
        self.assertAlmostEqual(area_m2(1.5, 2.5), 3.75)

    def test_purchase_cost(self):
        items = [
            type("obj", (object,), {"area_m2": 10, "buy_price_m2": 50})(),
            type("obj", (object,), {"area_m2": 5, "buy_price_m2": 100})()
        ]
        self.assertAlmostEqual(purchase_cost(items), 10 * 50 + 5 * 100)

    def test_sell_price(self):
        items = [
            type("obj", (object,), {"area_m2": 10, "sell_price_m2": 70})(),
            type("obj", (object,), {"area_m2": 5, "sell_price_m2": 120})()
        ]
        self.assertAlmostEqual(sell_price(items), 10 * 70 + 5 * 120)

    def test_pre_discount_total(self):
        self.assertAlmostEqual(pre_discount_total(1000, 50, 100), 1150)

    def test_discount_amount(self):
        self.assertAlmostEqual(discount_amount(1000, 10), 100)
        self.assertAlmostEqual(discount_amount(500, 0), 0)

    def test_taxable_base(self):
        self.assertAlmostEqual(taxable_base(1000, 100), 900)

    def test_tax_amount(self):
        self.assertAlmostEqual(tax_amount(900, 15), 135)

    def test_final_total(self):
        self.assertAlmostEqual(final_total(900, 135), 1035)

    def test_profit_margin(self):
        self.assertAlmostEqual(profit_margin(1000, 150, 600, 50), 500)

    def test_net_profit(self):
        self.assertAlmostEqual(net_profit(500, 100, 50), 350)

if __name__ == '__main__':
    unittest.main()

