import socket
import os

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# 接続を待つUNIXソケットのパスを設定
server_address = './socket/tcp_socket_file'

try:
    # ソケットファイルが存在している場合は削除
    os.unlink(server_address)
except FileNotFoundError:
    # ソケットファイルが存在しない場合は何もしない
    pass

# サーバアドレスにソケットをバインド
print('starting up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

# クライアントからの接続待機
while True:
    # クライアントからの接続を受け入れ
    connection, client_address = sock.accept()
    try:
        print('\nconnection from', client_address)

        # データを受信
        while True:
            # 最大16バイトのデータを読み込む
            data = connection.recv(16)

            # 受け取ったデータをバイナリ形式から文字列に変換
            data_str = data.decode('utf-8')

            # 受け取ったデータを表示
            print('received: {}'.format(data_str))

            if data:
                response = 'processing ' + data_str
                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break

    # 接続を閉じる
    finally:
        print('closing current connection')
        connection.close()
