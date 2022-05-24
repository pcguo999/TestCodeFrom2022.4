import socket

if __name__=='__main__':
    # 1.编写一个TCP服务端程序
    # 创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 保证端口复用，程序退出端口立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定地址和端口号
    tcp_server_socket.bind(("",8080))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 2.获取浏览器发送的HTTP请求报文数据
        # 建立连接，等待接收客户端连接请求
        server_client_socket,client_addr = tcp_server_socket.accept()
        # 获取浏览器的请求信息
        client_request_data=server_client_socket.recv(1024).decode()
        print(client_request_data)
        # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
        with open("./Web/index.html", "rb") as f: # 以二进制可读的方式进行读取
            file_data=f.read()
        # 应答行
        response_line="HTTP/1.1 200 OK\r\n"
        # 应答头，自己设置名称
        response_header="Server:PythonWeb\r\n"
        # 应答体，如html代码数据
        response_body=file_data

        # 整理整体的应答数据，记住空行的”\r\n“以及因为response_body已经是二进制文件，前面的应答行和应答头以及空行的"\r\n"也需要转化成二进制
        response_data=(response_line+response_header+"\r\n").encode()+response_body
        # 传输数据
        server_client_socket.send(response_data)

        # 4.HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字
        server_client_socket.close()