import dlt

@dlt.table
def factstream_stg():
    df=spark.readStream.table("spotify_cata.silver.factstream ")
    return df
 

# Create streaming target table (Gold layer)
dlt.create_streaming_table("factstream")

# Automatically apply CDC (Slowly Changing Dimension Type-2)
dlt.create_auto_cdc_flow(
    target = "factstream",                 # Gold table name
    source = "factstream_stg",             # Staging view
    keys = ["stream_id"],                 # Business key
    sequence_by = "stream_timestamp",         # Change timestamp column
    stored_as_scd_type = 1,             # SCD Type-1 
    track_history_except_column_list = None,
    name = None,
    once = False
)