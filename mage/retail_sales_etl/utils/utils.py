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
project_id = "zoomcamp-de-411412"
dataset_name = "retail_sales"
dataset_1 = "dataset_1"
dataset_2 = "dataset_2"
dataset_3 = "dataset_3"
dataset_4 = "dataset_4"
retail_dataset_merged = "retail_dataset_merged"
