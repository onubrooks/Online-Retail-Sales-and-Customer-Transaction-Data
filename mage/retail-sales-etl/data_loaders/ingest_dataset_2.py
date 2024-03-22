import io
import pandas as pd
import requests
import zipfile
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://storage.googleapis.com/public-project-dataset/2_Market%20Basket%20Analysis%20in%20Istanbul%20Retail%20Data.zip'
    response = requests.get(url)

    # Read the zip file content
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        # Get information about all files in the zip (choose the first CSV)
        file_info = zip_ref.infolist()
        csv_filename = [info.filename for info in file_info if info.filename.endswith('.csv')][0]
    
        # Extract the first CSV file
        with zip_ref.open(csv_filename) as csv_file:
            df = pd.read_csv(csv_file)  # Read the CSV data into a DataFrame

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
