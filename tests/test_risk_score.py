from risk_engine.score import calculate_global_risk

def test_score_is_bounded():
    d = {k: 50 for k in [
        "supply_disruption","inventory_stress","spare_capacity_stress",
        "hormuz_risk","bab_risk","suez_risk","malacca_risk","turkish_risk",
        "hormuz_traffic_stress","red_sea_traffic_stress","suez_traffic_stress",
        "tanker_freight_stress","brent_price_stress","brent_momentum",
        "oil_volatility","physical_premium","geopolitical_stress",
        "oil_to_cpi","inflation_surprise","yield_stress","credit_stress"
    ]}
    result = calculate_global_risk(d)
    assert 0 <= result["total"] <= 100
