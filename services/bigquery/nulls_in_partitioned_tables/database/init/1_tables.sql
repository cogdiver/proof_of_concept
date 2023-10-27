-- Create a partitioned table
CREATE OR REPLACE TABLE `<PROJECT>.poc.my_partitioned_table` (
    id INT64,
    name STRING,
    entry_date DATE,
    value INTEGER
)
PARTITION BY entry_date;
