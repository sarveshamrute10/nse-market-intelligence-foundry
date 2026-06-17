from transforms.api import transform, Input, Output
from pyspark.sql.functions import current_timestamp, input_file_name

@transform(
output=Output("/NSE/bronze/nse_bhavcopy_bronze"),
trades=Input("/NSE/raw/nse_bhavcopy_raw")
)
def compute(ctx, trades, output):

```
df = trades.dataframe()

df = (
    df
    .withColumn("ingestion_ts", current_timestamp())
    .withColumn("source_file", input_file_name())
)

output.write_dataframe(df)
```
