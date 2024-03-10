import socket
import os

# データグラムソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバが接続を待ち受けるUNIXドメインソケットのパスを指定
server_address = './socket/udp_server_socket_file'

try:
    # ソケットファイルが存在している場合は削除
    os.unlink(server_address)
except FileNotFoundError:
    # ソケットファイルが存在しない場合は何もしない
    pass

# サーバアドレスにソケットをバインド
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# クライアントからの接続待機
while True:
    print('\nwaiting to receive message')

    # ソケットからのデータを受信
    # 最大4096バイトのデータを読み込む
    data, address = sock.recvfrom(4096)

    # 受信したデータのバイト数と送信元のアドレスを表示
    print('received {} bytes from {}'.format(len(data), address))
    print('received: {}'.format(data.decode('utf-8')))

    # 受信したデータをそのまま送信元に送信
    if data:
        sent = sock.sendto(data, address)
        # 送信したバイト数と送信先のアドレスを表示
        print('sent {} bytes back to {}'.format(sent, address))
