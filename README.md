# 🌍 Global Energy War Dashboard V1

Streamlit framework for monitoring global energy supply, chokepoints, oil/LNG,
shipping stress, macro transmission and Canada.

## Important
V1 uses a clearly labeled demo/fallback dataset. It is not a live market-data
terminal. Replace demo fields with validated official/API data before using it
for investment or operational decisions.

## Risk model
Supply 25% | Chokepoints 25% | Shipping 15% | Price 15% |
Geopolitical 10% | Macro 10%

## Run locally

    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    pip install -r requirements.txt
    streamlit run app.py

## Data roadmap
Official/free first: EIA, FRED, Bank of Canada Valet, Statistics Canada,
OPEC public releases and IEA public releases.

Later: AIS/shipping provider, tanker freight, GDELT/news events and commercial
energy/shipping feeds.

## Disclaimer
Risk scores are model outputs, not forecasts or investment advice.
