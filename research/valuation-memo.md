# Valuation memo

**GXO Logistics financial modeling case study**  
Prepared September 28, 2026. Retrospective FY2025 basis. USD millions unless stated otherwise.

## Conclusion

The illustrative Base DCF produces **$5,413m enterprise value** and **$2,970m equity value**, or **$25.94 per year-end basic share**. The defensible conclusion is that terminal economics require substantial diligence. It is not a buy/sell recommendation or a claim about today's stock price.

The operating scenarios range from $6.57 to $32.42 per basic share under a common 8.8125% WACC. These are conditional outcomes, not statistical probability bounds. Debt makes equity value more sensitive than enterprise value to operating deterioration.

## Why cash conversion matters

The historical input reconciles reported free cash flow to operating cash flow, gross capital expenditure, and asset-sale proceeds. For 2025, operating cash flow less gross capex is $110m; adding $149m of proceeds gives company-defined FCF of $259m. This motivates excluding future disposals from the recurring forecast. [Source: GXO FY2025 release, Cash Flows and Other Reconciliations](https://investors.gxo.com/news-releases/news-release-details/gxo-reports-fourth-quarter-and-full-year-2025-results).

## What drives the Base case

Revenue grows at an assumed 5% per year. Margin improvement totals 50 basis points over five years, partially offset by a recurring-cost allowance. Forecast unlevered free cash flow rises from $377m to $509m. The terminal reinvestment rule then reduces cash available for distribution to $357m in the first terminal year.

This transition explains why blindly growing Year-5 cash flow forever would overstate value relative to the model's sustainable reinvestment assumption. The terminal ROIC assumption is central and needs support from a detailed invested-capital analysis.

## Terminal-method disagreement

The perpetual-growth terminal value implies **4.68x Year-5 adjusted EBITDA**. An assumed **8.5x** exit multiple instead produces **$8,436m enterprise value** and **$52.33 per basic share**. The two methods embed materially different expectations for cash conversion, growth, reinvestment, or required returns.

Do not present the higher exit-multiple result as corroboration of the DCF. No comparable-company evidence supports the 8.5x assumption in this version. The next valuation improvement would be a matched-date peer study and a reconciliation of accounting and lease treatment.

## Questions before relying on the valuation

1. Which excluded costs recur, and what reserve best approximates them?
2. How much capital expenditure is maintenance versus growth, and who funds warehouse automation?
3. Do contract pricing and renewal terms allow productivity improvements to reach operating profit?
4. What working-capital investment is required for new contracts and seasonal peaks?
5. How much cash is accessible, and what claims or dilution belong in the equity bridge?
6. Can independently estimated WACC and terminal ROIC support the assumed economics?

## Verification

Excel formulas were reconciled to a separate Python implementation for Base, Downside, and Upside. Six unit tests cover historical cash-flow reconciliation, sensitivity direction, the debt/equity bridge, the excess-cash floor, terminal constraints, and reinvestment. This validates the modeled mechanics; it does not validate the assumed future outcomes. Native Excel recalculation was not independently tested.
