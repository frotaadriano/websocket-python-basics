import websocket

def on_message(ws, message):
    print("Resposta do servidor:", message)

def on_open(ws):
    ws.send("Hello from websocket-client!")

def on_error(ws, error):
    print("❌ Erro:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔒 Conexão encerrada:", close_status_code, close_msg)


if __name__ == "__main__":
    print("Conectando ao WebSocket...")
    # ws = websocket.WebSocketApp("ws://localhost:8001/ws",
    #                             on_open=on_open,
    #                             on_message=on_message)

    ws = websocket.WebSocketApp("ws://localhost:8001/ws",
                             on_open=on_open,
                             on_message=on_message,
                             on_error=on_error,
                             on_close=on_close)
    
    ws.run_forever()