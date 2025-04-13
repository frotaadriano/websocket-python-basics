from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Teste</title>
</head>
<body>
    <h1>Teste WebSocket</h1>
    <form onsubmit="sendMessage(event)">
        <input type="text" id="messageText" autocomplete="off"/>
        <button>Enviar</button>
    </form>
    <ul id="messages"></ul>
    <script>
        const ws = new WebSocket(`ws://${window.location.host}/ws`);
        ws.onopen = () => console.log("✅ Conectado!");
        ws.onmessage = function(event) {
            const messages = document.getElementById('messages');
            const message = document.createElement('li');
            message.textContent = event.data;
            messages.appendChild(message);
        };

        function sendMessage(event) {
            event.preventDefault();
            const input = document.getElementById("messageText");
            if (ws.readyState === WebSocket.OPEN) {
                ws.send(input.value);
                input.value = '';
            } else {
                alert("WebSocket não está conectado.");
            }
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket conectado")
    try:
        while True:
            texto_recebido = await websocket.receive_text()
            print("🔁 Texto Recebido no WS:", texto_recebido)
            
            retorno = "Retorno do servidor, uma ação foi realizada com o texto recebido"
            # Aqui você pode fazer o que quiser com o texto recebido
            await websocket.send_text(f"Fiz algo com seu texto e estou te dando um retorno aqui: {retorno}")
    except Exception as e:
        print("❌ WebSocket desconectado:", e)
