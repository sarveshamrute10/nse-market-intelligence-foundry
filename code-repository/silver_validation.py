from transforms.api import transform, Input, Output
from pyspark.sql.functions import col

@transform(
valid_output=Output("/NSE/silver/nse_trades_silver"),
rejected_output=Output("/NSE/silver/nse_trades_rejected"),
trades=Input("/NSE/bronze/nse_bhavcopy_bronze")
)
def compute(ctx, trades, valid_output, rejected_output):

```
df = trades.dataframe()

valid_df = df.filter(
    (col("volume") > 0) &
    (col("close_price") > 0) &
    (col("symbol").isNotNull()) &
    (col("trade_date").isNotNull())
)

rejected_df = df.subtract(valid_df)

valid_output.write_dataframe(valid_df)
rejected_output.write_dataframe(rejected_df)
```
