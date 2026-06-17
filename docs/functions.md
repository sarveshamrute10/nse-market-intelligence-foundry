# Ontology Functions

## Top Gainers

Input:
- trade_date

Output:
- Top 10 stocks ranked by daily_return

---

## Top Losers

Input:
- trade_date

Output:
- Bottom 10 stocks ranked by daily_return

---

## Volume Spike Detector

Logic:

volume >
2 * rolling_30_day_avg_volume

Returns:
- TRUE
- FALSE