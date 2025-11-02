import dlt

@dlt.table
def dimuser_stg():
    df=spark.readStream.table("spotify_cata.silver.dimuser")
    return df


# Create streaming target table (Gold layer)
dlt.create_streaming_table("dimuser")

# Automatically apply CDC (Slowly Changing Dimension Type-2)
dlt.create_auto_cdc_flow(
    target = "dimuser",                 # Gold table name
    source = "dimuser_stg",             # Staging view
    keys = ["user_id"],                 # Business key
    sequence_by = "updated_at",         # Change timestamp column
    stored_as_scd_type = 2,             # SCD Type-2
    track_history_except_column_list = None,
    name = None,
    once = False
)