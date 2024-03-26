if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from retail_sales_etl.utils.utils import project_id, dataset_name, dataset_1, dataset_2, dataset_3, dataset_4, retail_dataset_merged
from retail_sales_etl.utils.pyspark_utils import read_bigquery_data, union_and_drop_duplicates, clean_data, write_to_bigquery

@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    """
    This function is the entry point for the pyspark script. It reads BigQuery data, merges, cleans, and writes it back.
    """

    # from pyspark.sql import SparkSession
    # Configure SparkSession with BigQuery connector
    # spark = SparkSession.builder.appName("BigQuery Data Merge").config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest.jar').getOrCreate()
    # spark.read.format("bigquery").option("credentialsFile", "</path/to/key/file>").option("table", "<table>").load()

    spark = kwargs.get('spark')

    table_names = [
        f"{project_id}.{dataset_name}.{dataset_1}",
        f"{project_id}.{dataset_name}.{dataset_2}",
        f"{project_id}.{dataset_name}.{dataset_3}",
        f"{project_id}.{dataset_name}.{dataset_4}",
    ]
    output_table = f"{project_id}.{dataset_name}.{retail_dataset_merged}"

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
