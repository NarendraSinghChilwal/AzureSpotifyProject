import dlt

@dlt.table(name="dimdate")
def dimdate():
    return spark.readStream.table("spotify_cata.silver.dimdate")
