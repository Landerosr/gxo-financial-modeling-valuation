# Methodology and assumptions

## Source map

All historical inputs come from [GXO's February 10, 2026 FY2025 release](https://investors.gxo.com/news-releases/news-release-details/gxo-reports-fourth-quarter-and-full-year-2025-results), accessed September 28, 2026. The release labels its tables unaudited.

| Fields | Source table | Transformation |
|---|---|---|
| Revenue, operating income, D&A | Consolidated Statements of Operations | Annual columns, USD millions |
| Adjusted EBITDA | Reconciliation of Net Income to Adjusted EBITDA | Reported non-GAAP measure |
| OCF, capex, property sale proceeds, FCF | Cash Flows and Other Reconciliations | Capex stored as positive expenditure |
| Cash, debt, NCI | Consolidated Balance Sheets | Current plus long-term debt |
| Period-end basic shares | Common-stock balance-sheet description | Thousands divided by 1,000 |

Do not replace period-end shares with weighted-average EPS shares. The per-share calculation is still a basic-share approximation; outstanding awards and future dilution are not modeled.

## Operating forecast

Revenue grows from the reported base. Adjusted EBITDA uses the historical margin plus scenario-specific changes. A recurring-cost allowance reduces forecast adjusted EBITDA by 0.50% of revenue in Base/Upside and 0.75% in Downside. This is an assumed reserve for potentially recurring excluded costs, not an audited adjustment. Stock compensation is not separately added back.

The Base case assumes 5% annual revenue growth, 10 basis points of annual margin improvement, D&A of 3% of revenue, capex of 2.5%, and operating NWC of 5%. Those are modeling judgments; reported revenue growth includes effects that should not be extrapolated mechanically. Downside stresses revenue, margins, reinvestment, and cash tied up in working capital. Upside requires faster growth and greater margin improvement, with more capex.

Opening operating NWC is an assumed 5% of revenue, not a reconstructed balance-sheet figure. A change in the forecast ratio therefore affects the first forecast year's cash requirement. D&A and capex are simplified revenue ratios. D&A includes amortization, so capex below total D&A need not imply declining productive capacity, but separating depreciation and amortization is a future refinement.

```
Normalized EBITDA proxy = adjusted EBITDA - recurring-cost allowance
EBIT proxy = normalized EBITDA proxy - D&A
NOPAT = EBIT proxy - max(EBIT proxy, 0) x normalized tax rate
FCFF = NOPAT + D&A - capex - change in operating NWC
```

FCFF excludes interest and debt repayment because it is available to all capital providers. It differs from reported company-defined FCF, which starts from operating cash flow and includes property-sale proceeds. No future property-sale proceeds are projected.

## WACC

Risk-free rate 4.25%, levered beta 1.20, equity risk premium 5.00%, pre-tax debt cost 6.00%, target debt weight 25%, and tax rate 25% are **illustrative inputs**, not observed market estimates.

Cost of equity = 4.25% + 1.20 x 5.00% = 10.25%.

WACC = 75% x 10.25% + 25% x 6.00% x (1 - 25%) = 8.8125%.

Using target weights avoids mistaking book equity for market capitalization. Beta consistency with the assumed capital structure still requires a peer unlevering/relevering exercise before practical use.

## Terminal value and timing

End-year discounting is applied to the five forecast years. Terminal NOPAT grows at 2.5%; 10% terminal ROIC implies reinvestment of 25% of NOPAT.

```
Terminal FCFF = Year-5 NOPAT x (1 + g) x (1 - g / ROIC)
Terminal value = terminal FCFF / (WACC - g)
Enterprise value = PV(explicit FCFF) + PV(terminal value)
```

The terminal cash flow resets reinvestment to a sustainable level instead of perpetuating forecast capex/D&A ratios. This creates a deliberate downward step from Year-5 FCFF. A smoother transition is a future refinement. WACC must exceed g, and g must be below ROIC.

The alternative terminal method applies an **assumed 8.5x multiple to Year-5 reported-basis adjusted EBITDA**. It is an assumption test, not trading comparables evidence. Do not average the two answers without reconciling their economic assumptions.

## Equity bridge

Excess cash is reported cash less a $200m required-cash assumption, floored at zero. Equity value = enterprise value + excess cash - reported debt - NCI proxy. All unrestricted cash is assumed accessible. Debt and NCI carrying values proxy for market values. Finance leases remain in debt; operating lease costs stay in earnings and operating lease liabilities are not separately deducted. Changes to that treatment require consistent cash-flow and WACC changes.

No pension deficit, off-balance-sheet claim, restricted cash, tax-loss carryforward, interest-deductibility limitation, future dilution, or mid-year timing adjustment is included. These limitations prevent treating the output as a transaction-ready price.
