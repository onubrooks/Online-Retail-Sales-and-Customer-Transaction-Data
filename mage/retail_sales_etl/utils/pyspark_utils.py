from pyspark.sql import SparkSession


def read_bigquery_data(spark, project_id, dataset_name, table_names):
  """
  This function reads data from multiple BigQuery tables into separate DataFrames.

  Args:
      spark (SparkSession): SparkSession object.
      project_id (str): Your Google Cloud project ID.
      dataset_name (str): Name of the dataset containing your BigQuery tables.
      table_names (list): List of BigQuery table names to read from.

  Returns:
      list: List of Spark DataFrames, one for each table.
  """
  dfs = [spark.read.format("bigquery").load(f"{project_id}.{dataset_name}.{table_name}") for table_name in table_names]
  return dfs


def union_and_drop_duplicates(dfs):
  """
  This function performs a union of all DataFrames and drops duplicate rows.

  Args:
      dfs (list): List of Spark DataFrames.

  Returns:
      pyspark.sql.DataFrame: The unioned DataFrame with duplicates removed.
  """
  merged_df = dfs[0].unionByName(*dfs[1:])  # Union all DataFrames
  return merged_df.dropDuplicates()  # Remove duplicate rows


def clean_data(df):
  """
  This function performs basic data cleaning operations (can be extended for specific needs).

  Args:
      df (pyspark.sql.DataFrame): The DataFrame to clean.

  Returns:
      pyspark.sql.DataFrame: The cleaned DataFrame.
  """
  # Replace None or empty strings with appropriate values (e.g., null)
  df = df.fillna(value="")  # Adjust based on data types and cleaning requirements

  # Handle casting data types if necessary (e.g., converting strings to numerics)
  # df = df.withColumn("cast_column", df["string_column"].cast("int"))

  # Apply additional cleaning logic as needed (e.g., handling outliers, formatting strings)

  return df


def write_to_bigquery(df, project_id, dataset_name, output_table):
  """
  This function writes a DataFrame back to BigQuery.

  Args:
      df (pyspark.sql.DataFrame): The DataFrame to write.
      project_id (str): Your Google Cloud project ID.
      dataset_name (str): Name of the dataset to write the data to.
      output_table (str): Name of the BigQuery table to store the results.
  """
  df.write.format("bigquery").option("writeMode", "overwrite").save(f"{project_id}.{dataset_name}.{output_table}")


def main():
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


if __name__ == "__main__":
  main()
