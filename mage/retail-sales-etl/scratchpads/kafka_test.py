"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable

from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
import json

BOOTSTRAP_SERVERS = ['broker:29092']
KAFKA_TOPIC = 'test-topic'
config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'key_serializer': lambda key: str(key).encode(),
        'value_serializer': lambda x: json.dumps(x.__dict__, default=str).encode('utf-8')
}

df = get_variable('retail_sales_analytics', 'ingest_dataset_2', 'output_0')
#producer = KafkaProducer(**config)
for index, row in df.iterrows():
    try:
        #record = producer.send(topic=KAFKA_TOPIC, key=index, value=row)
        # print('Record {} successfully produced at offset {}'.format(index, record.get().offset))
    except KafkaTimeoutError(e):
        print('timeout')
    if index == 3:
        print('breaking...')
        break

