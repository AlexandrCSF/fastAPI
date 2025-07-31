from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from pydantic import BaseModel

from src.kafka_service import produce_message, consume_messages

router = APIRouter()
class Message(BaseModel):
    topic: str
    data: dict

@router.post("/send/")
async def send_message(message: Message):
    await produce_message(message.topic, message.data)
    return {"status": "Сообщение отправлено в Kafka!"}

# Чтение сообщений через WebSocket (реальный времени)
@router.websocket("/ws/{topic}")
async def websocket_kafka(websocket: WebSocket, topic: str):
    await websocket.accept()
    try:
        async for message in consume_messages(topic):
            await websocket.send_json(message)
    except WebSocketDisconnect:
        print("Клиент отключился")