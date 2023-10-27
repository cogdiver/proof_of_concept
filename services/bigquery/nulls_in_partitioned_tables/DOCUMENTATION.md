# Null Values in Partitioned Table PoC

## Project Overview
This Proof of Concept (PoC) explores how Google BigQuery handles null values in a partitioned table. We specifically investigate the behavior of queries against a partitioned table when the partitioning column contains null values. The focus is on understanding how these null values influence the retrieval of data, particularly in relation to the partitioning column `entry_date`.

## Table Structure
The table `my_partitioned_table` in the dataset `poc` has the following schema:
- `id`: INT64
- `name`: STRING
- `entry_date`: DATE (used for partitioning the table)
- `value`: INTEGER

## Key Findings

### 1. Retrieving All Records

```sql
SELECT *
FROM poc.my_partitioned_table
```
Outcome:
- This query fetches all records in the table, including those with `NULL` values in the `entry_date` column.

| id  | name    | entry_date | value |
|-----|---------|------------|-------|
| 1   | Alice   | 2023-10-01 | 10    |
| 2   | Bob     | 2023-10-01 | 20    |
| 3   | Charlie | 2023-10-02 | 30    |
| 4   | David   | 2023-10-03 | 40    |
| 5   | Eva     | NULL       | 50    |
| 6   | Sam     | NULL       | 60    |

### 2. Filtering on Partitioned Column (`>=`, `<=`, `!=`)

```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date >= "2023-10-02"
```
Similar outcomes were observed for `<=` and `!=`.

Outcome:
- Queries with these conditions do not return rows where the `entry_date` is `NULL`.
- This behavior highlights that `NULL` values are not considered in range comparisons.

| id  | name    | entry_date | value |
|-----|---------|------------|-------|
| 3   | Charlie | 2023-10-02 | 30    |
| 4   | David   | 2023-10-03 | 40    |

### 3. Combined Filters on Partitioned and Non-partitioned Columns

```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date >= "2023-10-02"
  AND value >= 40
```
Similar outcomes were observed for conditions using `<=` and `!=`.

Outcome:
- Similar to the previous finding, any query applying a filter on the partitioned column (`entry_date`) alongside other columns does not return rows with `NULL` in `entry_date`.

| id  | name    | entry_date | value |
|-----|---------|------------|-------|
| 4   | David   | 2023-10-03 | 40    |

### 4. Explicit Filtering for `NULL` Values
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date IS NULL;

SELECT *
FROM poc.my_partitioned_table
WHERE value > 40;
```
Similar outcomes were observed for conditions using `value >= n`.

Outcome:
- Null values are only returned when there is either no filter applied on the `entry_date` or the condition `entry_date IS NULL` is explicitly used.


| id  | name    | entry_date | value |
|-----|---------|------------|-------|
| 5   | Eva     | NULL       | 50    |
| 6   | Sam     | NULL       | 60    |



## Query Analysis and Data Processed

Based on these additional findings, where different dates result in different amounts of data being processed, you can see how BigQuery efficiently processes only the relevant partitions. Here's how these results can be incorporated into the markdown table:

## Expanded Query Analysis and Data Processed

### 1. Full Table Scan
```sql
SELECT *
FROM poc.my_partitioned_table
```
**Data Processed:** 166 B

### 2. Filtering with Date (Non-null values)
- Date >= 2023-10-01
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date >= "2023-10-01"
```
**Data Processed:** 166 B  
**Note:** This query processes 166 B but does not return rows with `NULL` in `entry_date`.

- Date = 2023-10-01
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date = "2023-10-01"
```
**Data Processed:** 60 B

- Date = 2023-10-02
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date = "2023-10-02"
```
**Data Processed:** 33 B

- Date = 2023-10-03
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date = "2023-10-03"
```
**Data Processed:** 31 B

### 3. Range Filter between Two Dates
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date >= "2023-10-01"
  AND entry_date <= "2023-10-02"
```
**Data Processed:** 93 B

### 4. Filtering for Null Values
```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date IS NULL
```
**Data Processed:** 42 B

```sql
SELECT *
FROM poc.my_partitioned_table
WHERE entry_date IS NOT NULL
```
**Data Processed:** 124 B


>**Outcome:** These findings further demonstrate BigQuery's ability to optimize query performance based on partitioning. The data processed varies significantly based on the specific partition being queried. When the query is **filtered for a specific date or range**, only the data corresponding to that day's partition is processed, making the query more **efficient and cost-effective**. This is a key benefit of using partitioned tables, especially in big data environments, as it leads to both faster queries and reduced costs.

| Query Description                     | Data Processed |
|------------------------------------   |----------------|
| Full Table Scan                       | 166 B          |
| Filter (>= "2023-10-01")              | 166 B          |
| Filter (entry_date = "2023-10-01")    | 60 B           |
| Filter (entry_date = "2023-10-02")    | 33 B           |
| Filter (entry_date = "2023-10-03")    | 31 B           |
| Filter ("2023-10-01" to "2023-10-02") | 93 B           |
| Filter (entry_date IS NULL)           | 42 B           |
| Filter (entry_date IS NOT NULL)       | 124 B          |


## Conclusions

From our series of queries on the partitioned table `my_partitioned_table` in BigQuery, we can draw several important conclusions regarding how data is processed and managed in partitioned tables:

1. **Partition Effectiveness:** The data processed in a query is directly linked to the number of partitions it accesses. Queries filtered to specific dates (or date ranges) only process data from the corresponding partitions, not the entire table. This demonstrates the efficiency of partitioning in managing large datasets.

2. **Handling of Null Values:** When querying a partitioned column, null values are treated distinctly. Queries that do not explicitly include or exclude null values (using `IS NULL` or `IS NOT NULL`) won't process rows with null values in the partitioned column. Explicitly querying for null values in the partition column (`entry_date IS NULL`) results in processing only the data pertinent to those null values.

3. **Data Scanning and Costs:** The amount of data scanned during queries affects the cost. Our observations illustrate that:
   - A full table scan processes all the data (166 B in our case).
   - Filtering for specific dates like `2023-10-01`, `2023-10-02`, or `2023-10-03` processes 60 B, 33 B, and 31 B respectively, showing that only relevant partitions are scanned.
   - A range filter (`>= "2023-10-01" AND <= "2023-10-02"`) processed a combined size (93 B), reflecting the sum of individual partitions within the range.
   - A filter for null values in the partitioned column processed significantly less data (42 B), indicating that partitions with null values are smaller or treated differently.

These insights underline the importance of strategic querying and schema design in BigQuery, especially when handling large, partitioned datasets. Efficient querying not only reduces costs but also enhances performance, particularly vital in big data and cloud environments. This proof of concept underscores the utility and nuances of partitioning in BigQuery and the significant impact of partition design and query strategies on performance and cost.
