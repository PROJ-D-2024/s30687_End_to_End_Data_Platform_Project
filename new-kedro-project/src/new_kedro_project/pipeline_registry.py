from kedro.pipeline import Pipeline
from new_kedro_project.pipelines.crime_pipeline.pipeline import create_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    crime_pipeline = create_pipeline()

    return {
        "__default__": crime_pipeline,
        "crime_pipeline": crime_pipeline,
    }