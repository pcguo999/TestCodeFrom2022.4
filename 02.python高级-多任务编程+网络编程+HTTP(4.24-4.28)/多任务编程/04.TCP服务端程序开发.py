# # 导入socket模块
# import socket
#
# if __name__=='__main__':
#     # 1.创建服务端套接字对象
#     tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 设置端口号复用，让程序退出端口号立即释放
#     tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     # 2.和服务端套接字建立连接
#     tcp_server_socket.bind(("", 8888))
#         # 如果bind中的参数第一个IP地址设置为""，默认为本机IP地址
#         # 端口号只要不是特殊的端口号就可以
#     # 3.设置监听
#     tcp_server_socket.listen(128)
#         # 可以等待排队连接的最大数量
#         # listen后的这个套接字只负责接收客户端连接请求，不能收发消息，收发消息使用返回的这个新套接字来完成
#     # 4.等待客户端连接请求  accept阻塞等待，直到有客户端连接，
#     # 返回1.一个专门用以和客户端通信的socket套接字；2.客户端的ip地址和端口号
#     conn_socket, ip_port=tcp_server_socket.accept()
#     print("客户端的ip地址和端口号:", ip_port)
#     # 代码执行到此说明连接建立成功
#     # 5.接收客户端发送的数据, 这次接收数据的最大字节数是1024 recv阻塞等待数据的到来
#     recv_data = conn_socket.recv(1024)
#     # 获取数据的长度
#     recv_data_length = len(recv_data)
#     print("接收数据的长度为:", recv_data_length)
#     # 对二进制数据进行解码
#     recv_content = recv_data.decode()
#     print("接收客户端的数据为:", recv_content)
#
#     # 6.发送数据
#     # 准备发送的数据
#     send_data = "ok, 问题正在处理中...".encode()
#         # 要发送的二进制数据， 注意: 字符串需要使用encode()方法进行编码
#     # 发送数据
#     tcp_server_socket.send(send_data)
#     # 5.关闭套接字
#     # 关闭服务与客户端的套接字， 终止和客户端通信的服务
#     conn_socket.close()
#     # 关闭服务端的套接字, 终止和客户端提供建立连接请求的服务
#     tcp_server_socket.close()
