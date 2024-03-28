if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from retail_sales_etl.utils.pyspark_utils import write_to_bigquery
from retail_sales_etl.utils.variables import credentials_path, bq_reports_table_names

@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    spark = kwargs.get('spark')
    spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')
    spark._jsc.hadoopConfiguration().set('fs.AbstractFileSystem.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS')
    spark._jsc.hadoopConfiguration().set('fs.gs.auth.service.account.enable', 'true')
    spark._jsc.hadoopConfiguration().set('google.cloud.auth.service.account.json.keyfile', credentials_path)

    cleaned_df = args[0]
    cleaned_df.createOrReplaceTempView('retail_data')

    report1 = spark.sql("""
        SELECT
            customer_country,
            category,
            gender,
            payment_method,
            SUM(quantity) AS total_quantity,
            SUM(unit_price * quantity) AS total_sales
        FROM retail_data
        WHERE category != 'Unknown'
        GROUP BY customer_country, category, gender, payment_method
        ORDER BY total_sales DESC
    """)

    report2 = spark.sql("""
        SELECT
            stock_code,
            description,
            shopping_mall,
            SUM(quantity) AS total_quantity,
            SUM(unit_price * quantity) AS total_sales
        FROM retail_data
        WHERE stock_code IS NOT NULL AND description IS NOT NULL
        GROUP BY stock_code, description, shopping_mall
        ORDER BY total_sales DESC
    """)

    report3 = spark.sql("""
        SELECT
            customer_id,
            COUNT(DISTINCT invoice_date) AS purchase_frequency,
            SUM(quantity) AS total_quantity_purchased,
            SUM(unit_price * quantity) AS total_amount_spent
        FROM retail_data
        WHERE customer_id IS NOT NULL
        GROUP BY customer_id
        ORDER BY total_amount_spent DESC;
    """)

    report4 = spark.sql("""
        SELECT
                category,
                SUM(quantity) AS total_quantity_sold,
                SUM(quantity * unit_price) AS total_revenue,
                COUNT(DISTINCT invoice_no) AS number_of_orders,
                AVG(unit_price) AS average_unit_price,
                SUM(quantity * unit_price) / SUM(quantity) AS average_order_value
            FROM retail_data
            GROUP BY category
            ORDER BY total_revenue DESC; 
    """)

    report_dfs = [report1, report2, report3, report4]
    reports = dict(zip(bq_reports_table_names, report_dfs))

    for report_table_name, report_df in reports.items():
        write_to_bigquery(report_df, report_table_name)

    return cleaned_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
