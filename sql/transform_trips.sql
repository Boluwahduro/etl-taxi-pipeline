CREATE TABLE IF NOT EXISTS trips_clean AS
SELECT
    *,
    datetime(tpep_pickup_datetime) AS pickup_dt,
    datetime(tpep_dropoff_datetime) AS dropoff_dt,
    (julianday(dropoff_dt) - julianday(pickup_dt)) * 1440 AS trip_duration_minutes
FROM trips_raw
WHERE
    passenger_count > 0
    AND trip_distance > 0
    AND fare_amount > 0;
