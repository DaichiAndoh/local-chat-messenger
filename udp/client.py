import socket
import os

while True:
    # データグラムソケットを作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    # UNIXドメインソケットのパスを指定  
    server_address = './socket/udp_server_socket_file'
    client_address = './socket/udp_client_socket_file'

    try:
        # ソケットファイルが存在している場合は削除
        os.unlink(client_address)
    except FileNotFoundError:
        # ソケットファイルが存在しない場合は何もしない
        pass

    # このクライアントのアドレスにソケットをバインド
    sock.bind(client_address)

    try:
        # 送信するメッセージを標準入力から取得
        input_str = input('please input string value sent to server:')
        message = input_str.encode()

        # サーバにメッセージを送信
        print('sending message: {}'.format(input_str))
        sent = sock.sendto(message, server_address)

        # サーバからの応答を待機
        print('waiting to receive')

        # 最大4096バイトのデータを受信
        data, server = sock.recvfrom(4096)

        # サーバから受け取ったメッセージを表示
        print('server response: {}'.format(data.decode('utf-8')))

    finally:
        # ソケットを閉じる
        print('closing socket\n')
        sock.close()
