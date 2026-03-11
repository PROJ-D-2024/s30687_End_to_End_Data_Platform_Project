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


### evidence of successful execution
```log
(.venv) PS C:\Users\kostu\OneDrive\Pulpit\NYC PROJECT\crime-analytics-data-platform\new-kedro-project> kedro run
[03/11/26 07:20:49] INFO     Using 'conf\logging.yml' as logging configuration. You can change this by   __init__.py:269
                             setting the KEDRO_LOGGING_CONFIG environment variable accordingly.
[03/11/26 07:20:49] WARNING  C:\Users\kostu\OneDrive\Pulpit\NYC                                          warnings.py:110
                             PROJECT\crime-analytics-data-platform\new-kedro-project\.venv\Lib\site-pack
                             ages\requests\__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3)
                             or chardet (7.0.1)/charset_normalizer (3.4.5) doesn't match a supported
                             version!
                               warnings.warn(

                    WARNING  No 'settings.py' found, defaults will be used.                              __init__.py:345
[03/11/26 07:20:50] INFO     Kedro project new_kedro_project                                              session.py:335
                    INFO     Kedro is sending anonymous usage data with the sole purpose of improving the  plugin.py:242
                             product. No personal data or IP addresses are stored on our side. To opt out,
                             set the `KEDRO_DISABLE_TELEMETRY` or `DO_NOT_TRACK` environment variables, or
                             create a `.telemetry` file in the current working directory with the contents
                             `consent: false`. To hide this message, explicitly grant or deny consent.
                             Read more at https://docs.kedro.org/en/stable/about/telemetry/
[03/11/26 07:20:51] INFO     Using synchronous mode for loading and saving data. Use the --async sequential_runner.py:59
                             flag for potential performance gains.
                             https://docs.kedro.org/en/stable/build/run_a_pipeline/#load-and-sav
                             e-asynchronously
                    INFO     Loading data from params:dataset_url (MemoryDataset)...                data_catalog.py:1048
                    INFO     Running node: fetch_data_node: fetch_data() ->                                  node.py:531
[03/11/26 07:21:10] INFO     Saving data to raw_data (CSVDataset)...                                data_catalog.py:1008
                    INFO     Completed node: fetch_data_node                                               runner.py:245
                    INFO     Completed 1 out of 5 tasks                                                    runner.py:246
                    INFO     Loading data from raw_data (CSVDataset)...                             data_catalog.py:1048
[03/11/26 07:21:11] INFO     Loading data from params:min_rows (MemoryDataset)...                   data_catalog.py:1048
                    INFO     Loading data from params:required_columns (MemoryDataset)...           data_catalog.py:1048
                    INFO     Running node: validate_data_node: validate_data() ->                            node.py:531
                    INFO     Saving data to validated_data (CSVDataset)...                          data_catalog.py:1008
                    INFO     Completed node: validate_data_node                                            runner.py:245
                    INFO     Completed 2 out of 5 tasks                                                    runner.py:246
                    INFO     Loading data from validated_data (CSVDataset)...                       data_catalog.py:1048
                    INFO     Running node: clean_transform_node: clean_transform() ->                        node.py:531
                    INFO     Saving data to processed_data (CSVDataset)...                          data_catalog.py:1008
                    INFO     Completed node: clean_transform_node                                          runner.py:245
                    INFO     Completed 3 out of 5 tasks                                                    runner.py:246
                    INFO     Loading data from processed_data (CSVDataset)...                       data_catalog.py:1048
[03/11/26 07:21:12] INFO     Loading data from params:top_k (MemoryDataset)...                      data_catalog.py:1048
                    INFO     Running node: feature_node: feature_or_aggregate() ->                           node.py:531
                    INFO     Saving data to metrics_table (CSVDataset)...                           data_catalog.py:1008
                    INFO     Completed node: feature_node                                                  runner.py:245
                    INFO     Completed 4 out of 5 tasks                                                    runner.py:246
                    INFO     Loading data from metrics_table (CSVDataset)...                        data_catalog.py:1048
                    INFO     Running node: report_node: generate_report() ->                                 node.py:531
                    INFO     Saving data to report (JSONDataset)...                                 data_catalog.py:1008
                    INFO     Completed node: report_node                                                   runner.py:245
                    INFO     Completed 5 out of 5 tasks                                                    runner.py:246
                    INFO     Pipeline execution completed successfully in 20.9 sec.                        runner.py:119
```


