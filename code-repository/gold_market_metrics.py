from transforms.api import transform, Input, Output
from pyspark.sql.window import Window
from pyspark.sql.functions import (
lag,
avg,
col,
when
)

@transform(
output=Output("/NSE/gold/nse_market_metrics_gold"),
trades=Input("/NSE/silver/nse_trades_silver")
)
def compute(ctx, trades, output):

```
df = trades.dataframe()

stock_window = Window.partitionBy("symbol").orderBy("trade_date")

df = (
    df
    .withColumn(
        "daily_return",
        (
            col("close_price") -
            lag("close_price").over(stock_window)
        ) /
        lag("close_price").over(stock_window)
    )
    .withColumn(
        "turnover",
        col("close_price") * col("volume")
    )
)

rolling_window = (
    Window
    .partitionBy("symbol")
    .orderBy("trade_date")
    .rowsBetween(-30, -1)
)

df = (
    df
    .withColumn(
        "avg_30_day_volume",
        avg("volume").over(rolling_window)
    )
    .withColumn(
        "volume_spike_flag",
        when(
            col("volume") >
            2 * col("avg_30_day_volume"),
            True
        ).otherwise(False)
    )
)

output.write_dataframe(df)
```
