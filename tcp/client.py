import socket
import sys

while True:
    # UNIXソケットをストリームモードで作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # サーバに接続
    try:
        server_address = './socket/tcp_socket_file'
        print('connecting to {}'.format(server_address))
        sock.connect(server_address)
    except socket.error as err:
        print(err)
        sys.exit(1)

    # サーバに接続できれば、サーバにメッセージを送信
    try:
        # 送信するメッセージを標準入力から取得
        input_str = input('please input string value sent to server:')
        message = input_str.encode()

        # サーバへ送信
        sock.sendall(message)

        # サーバからの応答待機時間を2秒間に設定
        sock.settimeout(2)

        # サーバからの応答待機
        try:
            while True:
                # サーバからデータを受信
                # 最大32バイトのデータを読み込む
                data = sock.recv(32).decode('utf-8')

                if data:
                    print('server response: ' + data)
                else:
                    break

        # タイムアウトエラー時の処理
        except socket.timeout:
            print('socket timeout, ending listening for server messages')

    # 接続を閉じる
    finally:
        print('closing socket\n')
        sock.close()
