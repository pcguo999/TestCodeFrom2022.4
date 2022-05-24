import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用, 程序退出端口立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 8080))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 等待接受客户端的连接请求
        server_client_socket, client_addr = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        client_request_data = server_client_socket.recv(4096)

        # 对二进制数据进行解码
        server_client_socket = client_request_data.decode()
        print(server_client_socket)
        # 根据指定字符串进行分割
        request_list = server_client_socket.split(" ")

        # 获取请求资源路径
        request_path = request_list[1]
        print(request_path)

        # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
        if request_path == "/":
            request_path = "/index.html"

        try:
            # 动态打开指定文件
            with open("./Web"+request_path, "rb") as file:
                # 读取文件数据
                file_data = file.read()
        except Exception as e:
            # 请求资源不存在，返回404数据
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PythonWeb\r\n"
            with open("./Web/error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            response_body = file_data
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            # 发送数据
            server_client_socket.send(response_data)
        else: #正常返回数据
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PythonWeb\r\n"
            # 响应体
            response_body = file_data
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            # 发送数据
            server_client_socket.send(response_data)
        finally:
            # 关闭服务与客户端的套接字
            server_client_socket.close()
