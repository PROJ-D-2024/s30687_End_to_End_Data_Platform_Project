## Dataset
```
https://data.cityofchicago.org/resource/ijzp-q8t2.csv?$limit=50000
```
In this project the size of downloaded data was limited to **50000** records due to file being to big

## Dataset description

The dataset contains reported crime incidents in the city of Chicago. Each record represents a single crime event and includes information such as the type of crime, date and time of occurrence, location details, and case identifiers.

## How to run Kedro pipeline

You can run Kedro project with:

```
kedro run
```

## Outputs

| Dataset | Path |
|--------|------|
| raw_data | `data/01_raw/raw_data.csv` |
| validated_data | `data/02_intermediate/validated_data.csv` |
| processed_data | `data/03_primary/processed_data.csv` |
| metrics_table | `data/04_feature/metrics_table.csv` |
| report | `data/08_reporting/report.json` |

## Example Report Output

``` json
{
  "rows": 10,
  "columns": 2,
  "generated_at": "2026-03-07T13:12:44.955478"
}
```



