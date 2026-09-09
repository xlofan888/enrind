def get_demo_market_data():
    # Clearly labeled demo values. Replace with validated API data for live use.
    return {
        "brent": 101.0, "brent_1d": 2.1,
        "supply_disruption": 62, "inventory_stress": 55, "spare_capacity_stress": 60,
        "hormuz_risk": 92, "bab_risk": 84, "suez_risk": 63, "malacca_risk": 48, "turkish_risk": 35,
        "hormuz_traffic_stress": 80, "red_sea_traffic_stress": 68,
        "suez_traffic_stress": 55, "tanker_freight_stress": 72,
        "brent_price_stress": 78, "brent_momentum": 70, "oil_volatility": 65, "physical_premium": 60,
        "geopolitical_stress": 78,
        "oil_to_cpi": 55, "inflation_surprise": 48, "yield_stress": 45, "credit_stress": 30,
    }
