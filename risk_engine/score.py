def _clamp(x):
    return max(0.0, min(100.0, float(x)))

def calculate_global_risk(d):
    supply = _clamp(d["supply_disruption"]*.40 + d["inventory_stress"]*.25 + d["spare_capacity_stress"]*.35)
    chokepoint = _clamp(d["hormuz_risk"]*.35 + d["bab_risk"]*.30 + d["suez_risk"]*.15 + d["malacca_risk"]*.15 + d["turkish_risk"]*.05)
    shipping = _clamp(d["hormuz_traffic_stress"]*.35 + d["red_sea_traffic_stress"]*.30 + d["suez_traffic_stress"]*.15 + d["tanker_freight_stress"]*.20)
    price = _clamp(d["brent_price_stress"]*.35 + d["brent_momentum"]*.25 + d["oil_volatility"]*.20 + d["physical_premium"]*.20)
    geopolitical = _clamp(d["geopolitical_stress"])
    macro = _clamp(d["oil_to_cpi"]*.35 + d["inflation_surprise"]*.25 + d["yield_stress"]*.20 + d["credit_stress"]*.20)
    total = supply*.25 + chokepoint*.25 + shipping*.15 + price*.15 + geopolitical*.10 + macro*.10

    if total < 30: regime = "🟢 NORMAL"
    elif total < 50: regime = "🟡 ELEVATED"
    elif total < 70: regime = "🟠 HIGH"
    elif total < 85: regime = "🔴 SEVERE"
    else: regime = "🟥 CRISIS"

    return {"total": total, "regime": regime, "pillars": {
        "Supply": supply, "Chokepoints": chokepoint, "Shipping": shipping,
        "Price": price, "Geopolitical": geopolitical, "Macro": macro}}
