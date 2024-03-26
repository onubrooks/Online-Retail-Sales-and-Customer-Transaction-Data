if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from pyspark.sql import SparkSession
from utils.pyspark_utils import read_bigquery_data, union_and_drop_duplicates, clean_data, write_to_bigquery

@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
     """
    This function is the entry point for the script. It reads BigQuery data, merges, cleans, and writes it back.
    """

    # Configure SparkSession with BigQuery connector
    spark = SparkSession.builder.appName("BigQuery Data Merge").getOrCreate()

    # Replace with your actual values
    project_id = "your-project-id"
    dataset_name = "your_dataset"
    table_names = [
        f"{project_id}.{dataset_name}.table1",
        f"{project_id}.{dataset_name}.table2",
        f"{project_id}.{dataset_name}.table3",
        f"{project_id}.{dataset_name}.table4",
    ]
    output_table = f"{project_id}.{dataset_name}.merged_table"

    # Read data from BigQuery tables
    dfs = read_bigquery_data(spark, project_id, dataset_name, table_names)

    # Union DataFrames and drop duplicates
    merged_df = union_and_drop_duplicates(dfs)

    # Perform data cleaning (optional, extend `clean_data` function for specific needs)
    cleaned_df = clean_data(merged_df)

    # Write cleaned data back to BigQuery
    write_to_bigquery(cleaned_df, project_id, dataset_name, output_table)

    spark.stop()

    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
