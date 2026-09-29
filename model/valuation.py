"""Reproducible illustrative GXO DCF. Standard library only. USD millions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def value(data, case='Base', wacc=None, growth=None):
    a, h = data['assumptions'], data['historical']['2025']
    c = data['cases'][case]
    discount = wacc if wacc is not None else ((a['risk_free']+a['beta']*a['equity_risk_premium'])*(1-a['debt_weight'])+a['cost_of_debt']*(1-a['tax_rate'])*a['debt_weight'])
    g = a['terminal_growth'] if growth is None else growth
    if not (0 <= g < discount and g < a['terminal_roic']):
        raise ValueError('Require 0 <= terminal growth < WACC and terminal ROIC')
    rev, nwc = h['revenue'], h['revenue']*a['opening_nwc_ratio']
    years=[]
    for t in range(1,6):
        rev *= 1+c['growth'][t-1]
        ebitda=rev*(h['adjusted_ebitda']/h['revenue']+c['margin_uplift'][t-1])
        haircut=rev*c['cost_haircut']; da=rev*a['da_ratio']
        ebit=ebitda-haircut-da; tax=max(ebit,0)*a['tax_rate']
        nopat=ebit-tax; capex=rev*c['capex_ratio']
        end_nwc=rev*c['nwc_ratio']; delta=end_nwc-nwc
        fcff=nopat+da-capex-delta; pv=fcff/(1+discount)**t
        years.append(dict(year=t,revenue=rev,ebitda=ebitda,haircut=haircut,da=da,ebit=ebit,nopat=nopat,capex=capex,delta_nwc=delta,fcff=fcff,pv=pv))
        nwc=end_nwc
    terminal_nopat=years[-1]['nopat']*(1+g)
    terminal_fcff=terminal_nopat*(1-g/a['terminal_roic'])
    terminal_value=terminal_fcff/(discount-g)
    pv_terminal=terminal_value/(1+discount)**5
    ev=sum(y['pv'] for y in years)+pv_terminal
    excess_cash=max(0,h['cash']-a['required_cash'])
    equity=ev+excess_cash-h['debt']-h['nci']
    exit_ev=sum(y['pv'] for y in years)+years[-1]['ebitda']*a['exit_multiple']/(1+discount)**5
    return dict(case=case,wacc=discount,terminal_growth=g,years=years,terminal_fcff=terminal_fcff,terminal_value=terminal_value,pv_terminal=pv_terminal,enterprise_value=ev,equity_value=equity,per_share=equity/h['shares'],terminal_share=pv_terminal/ev,implied_terminal_multiple=terminal_value/years[-1]['ebitda'],exit_multiple_ev=exit_ev)

if __name__=='__main__':
    data=json.loads((ROOT/'model/inputs.json').read_text())
    results={c:value(data,c) for c in data['cases']}
    (ROOT/'research/results.json').write_text(json.dumps(results,indent=2)+'\n')
    for c,r in results.items(): print(f"{c}: WACC {r['wacc']:.2%}; EV ${r['enterprise_value']:,.1f}m; equity/share ${r['per_share']:.2f}")
