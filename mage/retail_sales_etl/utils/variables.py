schema = {
    'invoice_no': 'str',
    'stock_code': 'str',
    'description': 'str',
    'invoice_date': 'str',
    'unit_price': 'float64',
    'quantity': 'float64',
    'customer_country': 'str',
    'customer_id': 'str',
    'source': 'str',
    'gender': 'str',
    'age': 'int64',
    'category': 'str',
    'payment_method': 'str',
    'shopping_mall': 'str'
}

credentials_path = "/home/src/retail_sales_etl/secrets/google.json"
bq_jar_file = "/home/src/retail_sales_etl/spark-lib/spark-3.5-bigquery-0.37.0.jar"
gcp_bucket = "mage-zoomcamp-onubrooks"
gcs_path = "pyspark"
project_id = "zoomcamp-de-411412"
dataset_name = "retail_sales"
dataset_1 = "dataset_1"
dataset_2 = "dataset_2"
dataset_3 = "dataset_3"
dataset_4 = "dataset_4"

report_1 = "report_shopping_trends_by_demographics"
report_2 = "report_product_performance_by_malls"
report_3 = "report_customer_purchase_behaviour"
report_4 = "report_product_category_performance"

retail_dataset_merged = "retail_dataset_merged"

bq_table_names = [
    f"{project_id}.{dataset_name}.{dataset_1}",
    f"{project_id}.{dataset_name}.{dataset_2}",
    f"{project_id}.{dataset_name}.{dataset_3}",
    f"{project_id}.{dataset_name}.{dataset_4}",
]
bq_output_table = f"{project_id}.{dataset_name}.{retail_dataset_merged}"

bq_reports_table_names = [
    f"{project_id}.{dataset_name}.{report_1}",
    f"{project_id}.{dataset_name}.{report_2}",
    f"{project_id}.{dataset_name}.{report_3}",
    f"{project_id}.{dataset_name}.{report_4}",
]
