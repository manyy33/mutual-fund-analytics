# Mutual Fund Analytics - Data Dictionary


## 1. dim_fund (Dimension Table)

Purpose:
Stores master information about mutual fund schemes.

| Column | Description |
|---|---|
| amfi_code | Unique identifier of mutual fund |
| scheme_name | Name of the mutual fund scheme |
| fund_house | Asset management company name |
| category | Fund category (Equity/Debt/etc.) |
| plan | Direct or Regular plan |


---

## 2. dim_date (Dimension Table)

Purpose:
Stores date-related information for time-based analysis.

| Column | Description |
|---|---|
| date | Actual date |
| year | Year extracted from date |
| month | Month extracted from date |
| quarter | Quarter of the year |


---

## 3. fact_nav (Fact Table)

Purpose:
Stores historical Net Asset Value information.

| Column | Description |
|---|---|
| amfi_code | Mutual fund identifier |
| date | NAV date |
| nav | Net Asset Value of fund |


---

## 4. fact_transactions (Fact Table)

Purpose:
Stores investor transaction records.

| Column | Description |
|---|---|
| investor_id | Unique investor identifier |
| amfi_code | Mutual fund identifier |
| transaction_date | Date of transaction |
| transaction_type | Purchase or Redemption |
| amount | Transaction amount |


---

## 5. fact_performance (Fact Table)

Purpose:
Stores mutual fund performance metrics.

| Column | Description |
|---|---|
| scheme_name | Fund scheme name |
| return_1yr_pct | One year return percentage |
| return_3yr_pct | Three year return percentage |
| return_5yr_pct | Five year return percentage |
| benchmark_3yr_pct | Benchmark return |
| alpha | Excess return compared to benchmark |
| beta | Market sensitivity |
| sharpe_ratio | Risk adjusted return |
| sortino_ratio | Downside risk adjusted return |

