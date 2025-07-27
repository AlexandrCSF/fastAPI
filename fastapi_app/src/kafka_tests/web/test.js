const ws = new WebSocket("ws://localhost:8080/ws/test_topic");
ws.onmessage = (event) => console.log(JSON.parse(event.data));