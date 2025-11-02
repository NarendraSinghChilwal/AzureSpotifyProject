import dlt

@dlt.table
def dimtrack_stg():
    df=spark.readStream.table("spotify_cata.silver.dimtrack")
    return df
 

# Create streaming target table (Gold layer)
dlt.create_streaming_table("dimtrack")

# Automatically apply CDC (Slowly Changing Dimension Type-2)
dlt.create_auto_cdc_flow(
    target = "dimtrack",                 # Gold table name
    source = "dimtrack_stg",             # Staging view
    keys = ["track_id"],                 # Business key
    sequence_by = "updated_at",         # Change timestamp column
    stored_as_scd_type = 2,             # SCD Type-2
    track_history_except_column_list = None,
    name = None,
    once = False
)