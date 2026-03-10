"""
This is a boilerplate pipeline 'crime_pipeline'
generated using Kedro 1.2.0
"""



from kedro.pipeline import Pipeline, node
from .nodes import (
    fetch_data,
    validate_data,
    clean_transform,
    feature_or_aggregate,
    generate_report,
)


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=fetch_data,
                inputs="params:dataset_url",
                outputs="raw_data",
                name="fetch_data_node",
            ),
            node(
                func=validate_data,
                inputs=dict(
                    df="raw_data",
                    min_rows="params:min_rows",
                    required_columns="params:required_columns",
                ),
                outputs="validated_data",
                name="validate_data_node",
            ),
            node(
                func=clean_transform,
                inputs="validated_data",
                outputs="processed_data",
                name="clean_transform_node",
            ),
            node(
                func=feature_or_aggregate,
                inputs=dict(
                    df="processed_data",
                    top_k="params:top_k",
                ),
                outputs="metrics_table",
                name="feature_node",
            ),
            node(
                func=generate_report,
                inputs="metrics_table",
                outputs="report",
                name="report_node",
            ),
        ]
    )