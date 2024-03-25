if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
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

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    columns = {
        'InvoiceNo': 'invoice_no',
        'StockCode': 'stock_code',
        'Description': 'description',
        'Quantity': 'quantity',
        'InvoiceDate': 'invoice_date',
        'UnitPrice': 'unit_price',
        'CustomerID': 'customer_id',
        'Country': 'customer_country',
    }
    transform = data.rename(columns=columns)

    new_cols = {'gender': 'Unknown', 'age': 999999, 'category': 'Unknown', 'payment_method': 'Unknown', 'shopping_mall': 'Unknown', 'source': 'online_retail_dataset'} 
    transform = transform.assign(**new_cols)  # Unpack dictionary as arguments

    transform = transform.reindex(columns=schema.keys()).astype(schema)
    
    transform['invoice_date'] = pd.to_datetime(transform['invoice_date'], format='%m/%d/%y %H:%M') 
    transform['invoice_date'] = transform['invoice_date'].dt.strftime('%Y-%m-%d %H:%M')
    
    return transform


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
