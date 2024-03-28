if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from retail_sales_etl.utils.variables import credentials_path, bq_jar_file, bq_table_names, bq_output_table
from retail_sales_etl.utils.pyspark_utils import read_bigquery_data, union_and_drop_duplicates, clean_data, write_to_bigquery
from pyspark.sql import SparkSession

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

    spark = kwargs.get('spark')
    spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')
    spark._jsc.hadoopConfiguration().set('fs.AbstractFileSystem.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS')
    spark._jsc.hadoopConfiguration().set('fs.gs.auth.service.account.enable', 'true')
    spark._jsc.hadoopConfiguration().set('google.cloud.auth.service.account.json.keyfile', credentials_path)

    # Read data from BigQuery tables
    dfs = read_bigquery_data(spark, bq_table_names)

    # Union DataFrames and drop duplicates
    merged_df = union_and_drop_duplicates(dfs)

    # Perform data cleaning
    cleaned_df = clean_data(merged_df)

    # Write cleaned data back to BigQuery
    write_to_bigquery(cleaned_df, bq_output_table)

    return cleaned_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
