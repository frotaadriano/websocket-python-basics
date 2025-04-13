# WebSocket com Python — Exemplo Básico

Este repositório mostra como usar WebSockets de forma simples com Python. Inclui:

- ✅ Exemplo com **FastAPI** e **HTML/JS**
- ✅ Exemplo com **WebSocket em Python puro** com `websocket-client`
- Ideal para entender o básico de comunicação em tempo real com WebSockets

---

## 🔧 Pré-requisitos

Instale o Python 3.8 ou superior, depois instale as dependências com:

```bash
pip install -r requirements.txt
```

> 💡 Se você preferir, pode instalar o FastAPI com suporte total a WebSocket e outros protocolos com:

```bash
pip install "uvicorn[standard]" fastapi
```

---

## ✅ Exemplo 1: WebSocket com FastAPI + HTML

### 📁 Arquivos

- `app/main.py`: Backend FastAPI
- `app/client.html`: Frontend HTML com JavaScript nativo

### ▶️ Como rodar:

1. No terminal, vá até o diretório do projeto:
   ```bash
   cd websocket-python-basics
   ```

2. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Acesse no navegador:
   ```
   http://127.0.0.1:8000
   ```

4. Envie mensagens no campo e veja a resposta via WebSocket!

---

## ✅ Exemplo 2: Comunicação com WebSocket puro (sem navegador)

### 📁 Arquivos

- `rtclient_example/server.py`: Servidor FastAPI (WebSocket)
- `rtclient_example/client.py`: Cliente em Python que se conecta via WebSocket

### ▶️ Como rodar:

1. Em um terminal, inicie o servidor:

```bash 
uvicorn rtclient_example.server:app --reload --port 8001

```
2. Em outro terminal teste: 
```bash 
netstat -ano | findstr :8001   
```
O retorno deve ser algo como:  
```
TCP    127.0.0.1:8001         0.0.0.0:0              LISTENING       29644
```
3. Em outro terminal, execute o cliente:

```bash
python rtclient_example/client.py

```

Você verá no terminal algo como:

```
Conectando ao WebSocket...
Resposta do servidor: Echo: Hello from websocket-client!
🔒 Conexão encerrada: 1012 
```

---

## 🧠 Dica bônus

Você pode testar o WebSocket direto do console do navegador:

```js
let ws = new WebSocket("ws://127.0.0.1:8000/ws");
ws.onmessage = (e) => console.log("Mensagem:", e.data);
ws.onopen = () => ws.send("Olá backend!");
```

---

## 📚 Referências

- [FastAPI WebSocket Docs](https://fastapi.tiangolo.com/advanced/websockets/)
- [WebSocket RFC6455](https://datatracker.ietf.org/doc/html/rfc6455)