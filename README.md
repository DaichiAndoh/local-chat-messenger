# local-chat-messenger &middot; ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

UNIXドメインソケットを用いてプロセス間通信を行うプログラムです。
client（`client.py`）とserver（`server.py`）の2つのプログラムが通信します。

## Usage

### TCP通信

```:python
# サーバ起動
$ cd tcp
$ python server.py
starting up on ./socket/tcp_socket_file
```

```:python
# クライアント起動, リクエスト送信, レスポンス受信
$ cd tcp
$ python client.py
connecting to ./socket/tcp_socket_file
please input string value sent to server:hello!
server response: processing hello!
socket timeout, ending listening for server messages
closing socket

connecting to ./socket/tcp_socket_file
please input string value sent to server:
```

```:python
# サーバログ
connection from
received: hello!
received:
no data from
closing current connection
```

### UDP通信

```:python
# サーバ起動
$ cd udp
$ python server.py
starting up on ./socket/udp_server_socket_file

waiting to receive message
```

```:python
# クライアント起動, リクエスト送信, レスポンス受信
$ cd udp
$ python client.py
please input string value sent to server:hello!
sending message: hello!
waiting to receive
server response: hello!
closing socket

please input string value sent to server:
```

```:python
# サーバログ
waiting to receive message
received 6 bytes from ./socket/udp_client_socket_file
received: hello!
sent 6 bytes back to ./socket/udp_client_socket_file

waiting to receive message
```
