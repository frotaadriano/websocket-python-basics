# websocket-python-basics
# WebSocket com Python — Exemplo Básico

Este repositório mostra como usar WebSockets de forma simples com Python. Inclui:

- Exemplo com **FastAPI** e **HTML/JS**
- Exemplo com **rtclient** como cliente ou servidor
- Ideal para entender o básico de comunicação em tempo real

## 🔧 Pré-requisitos

```bash
pip install -r requirements.txt

websocket-python-basics/
│
├── README.md
├── requirements.txt
├── app/
│   ├── main.py               # FastAPI com endpoint websocket
│   └── client.html           # Página web simples para testar
│
├── rtclient_example/
│   ├── server.py             # Exemplo usando rtclient como WebSocket server
│   └── client.py             # Cliente básico com rtclient
│
└── assets/
    └── diagram.png           # (Opcional) Diagrama simples da comunicação WebSocket
