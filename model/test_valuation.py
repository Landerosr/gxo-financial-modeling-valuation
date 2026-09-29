import copy
import json
import unittest
from pathlib import Path
from valuation import value

class ValuationTests(unittest.TestCase):
    def setUp(self): self.d=json.loads((Path(__file__).parent/'inputs.json').read_text())
    def test_reported_cash_flow(self):
        for h in self.d['historical'].values(): self.assertEqual(h['ocf']-h['capex']+h['asset_sales'],h['company_fcf'])
    def test_directional_sensitivity(self):
        self.assertGreater(value(self.d,wacc=.08)['enterprise_value'],value(self.d,wacc=.10)['enterprise_value'])
        self.assertGreater(value(self.d,'Upside')['enterprise_value'],value(self.d)['enterprise_value'])
        self.assertLess(value(self.d,'Downside')['enterprise_value'],value(self.d)['enterprise_value'])
    def test_equity_bridge(self):
        before=value(self.d); d=copy.deepcopy(self.d);d['historical']['2025']['debt']+=100
        self.assertAlmostEqual(before['equity_value']-value(d)['equity_value'],100)
        self.assertEqual(before['enterprise_value'],value(d)['enterprise_value'])
    def test_cash_floor(self):
        d=copy.deepcopy(self.d); d['assumptions']['required_cash']=1000
        r=value(d);self.assertAlmostEqual(r['equity_value'],r['enterprise_value']-3065-32)
    def test_invalid_terminal_assumptions(self):
        with self.assertRaises(ValueError): value(self.d,wacc=.025,growth=.025)
    def test_terminal_reinvestment(self):
        d=copy.deepcopy(self.d);d['assumptions']['terminal_roic']=.08
        self.assertLess(value(d)['enterprise_value'],value(self.d)['enterprise_value'])

if __name__=='__main__': unittest.main()
