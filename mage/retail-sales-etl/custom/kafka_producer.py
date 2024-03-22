if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError

BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'sample_data'
config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'key_serializer': lambda key: str(key).encode(),
        'value_serializer': lambda x: json.dumps(x.__dict__, default=str).encode('utf-8')
    }
producer = KafkaProducer(**config)


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    header = args[0]
    print(header)
    for item in args[1:10]:
        try:
            record = producer.send(topic=KAFKA_TOPIC, key=item[0], value=item)
            print('Record {} successfully produced at offset {}'.format(item[0], record.get().offset))
        except KafkaTimeoutError as e:
            print(e.__str__())

    return args


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
