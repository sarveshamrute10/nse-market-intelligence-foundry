# Ontology Design

## Object: Stock

### Primary Key
symbol

### Properties
| Property | Type |
|-----------|---------|
| symbol | string |
| company_name | string |
| sector | string |
| industry | string |
| market_cap_category | string |

### Relationships
- Belongs to one Sector
- Has many Trading Sessions

---

## Object: Trading Session

### Primary Key
session_id

### Properties

| Property | Type |
|-----------|---------|
| trade_date | date |
| open_price | decimal |
| close_price | decimal |
| volume | bigint |
| turnover | decimal |
| daily_return | decimal |
| vwap | decimal |

### Relationships
- Belongs to one Stock

---

## Object: Sector

### Primary Key
sector_name

### Properties

| Property | Type |
|-----------|---------|
| sector_name | string |
| avg_return | decimal |
| avg_volume | bigint |
| stocks_count | integer |