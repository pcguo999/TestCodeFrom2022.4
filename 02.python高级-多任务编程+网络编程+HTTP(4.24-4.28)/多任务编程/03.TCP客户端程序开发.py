# # 导入socket模块
# import socket
#
# if __name__=='__main__':
#     # 1.创建客户端套接字对象
#     tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         # socket.socket(AddressFamily, Type)
#         # AddressFamily 表示IP地址类型, 分为IPv4和IPv6 AF_INET表示IPv4
#         # Type 表示传输协议类型 SOCK_STREAM表示TCP类型
#     # 2.和服务端套接字建立连接
#     tcp_client_socket.connect(("192.168.206.129", 8080))
#     # 代码执行到此，说明连接建立成功
#     # 3.发送数据
#     # 准备发送的数据
#     send_data = "你好服务端，我是客户端PCGuo!".encode("utf-8")
#         # 要发送的二进制数据， 注意: 字符串需要使用encode()方法进行编码，encode不写参数表示默认utf-8
#     # 发送数据
#     tcp_client_socket.send(send_data)
#     # 4.接收数据 recv阻塞等待数据的到来
#     recv_data = tcp_client_socket.recv(1024)
#         # recv参数表示每次接收数据的大小，单位是字节
#     # 查看是否接收到
#     # 返回的直接是服务端程序发送的二进制数据
#     print(recv_data)
#     # 对数据进行解码
#     recv_content = recv_data.decode("utf-8")
#     print("接收服务端的数据为:", recv_content)
#     # 5.关闭客户端套接字
#     tcp_client_socket.close()
