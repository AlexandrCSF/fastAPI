import json

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

async def produce_message(topic: str, message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        await producer.send_and_wait(
            topic,
            json.dumps(message).encode("utf-8")
        )
    finally:
        await producer.stop()

async def consume_messages(topic: str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="fastapi-group",
        auto_offset_reset="earliest"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            yield json.loads(msg.value.decode("utf-8"))
    finally:
        await consumer.stop()