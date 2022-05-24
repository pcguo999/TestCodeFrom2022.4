import socket
import threading
import sys

# 定义web服务器类
class HttpWebServer(object):
    def __init__(self,port): #添加一个端口参数
        # 创建tcp服务端套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用, 程序退出端口立即释放
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        self.tcp_server_socket.bind(("", port))
        # 设置监听
        self.tcp_server_socket.listen(128)

    # 处理客户端的请求,放start函数前
    @staticmethod
    def handle_client_request(self,server_client_socket):
        # 获取浏览器的请求信息
        client_request_data = server_client_socket.recv(4096)
        # 对二进制数据进行解码
        client_request_data = client_request_data.decode()
        print(client_request_data)
        # 根据指定字符串进行分割
        request_list = client_request_data.split(" ")
        # 判断客户端是否关闭：
        # 若返回的数据只包含一个，则表示返回的是浏览器返回的空字符串信息告知，则表示浏览器关闭，这时直接关闭套接字就可，并直接结束函数
        if len(request_list) == 1:
            server_client_socket.close()
            return
        # 获取请求资源路径
        request_path = request_list[1]
        print(request_path)
        # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
        if request_path == "/":
            request_path = "/index.html"
        try:
            # 动态打开指定文件
            with open("./Web" + request_path, "rb") as file:
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
        else:  # 正常返回数据
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

    # 启动Web服务器进行工作
    def start(self):
        while True:
            # 等待接受客户端的连接请求
            server_client_socket, client_addr = self.tcp_server_socket.accept()
            # 代码执行到此，说明连接建立成功
            # 创建子线程，传递参数是为了和客户端进行通信的，即传递server_client_socket，同时设置守护主线程
            sub_thread=threading.Thread(target=self.handle_client_request,args=(server_client_socket,),daemon=True)
            # 启动子线程
            sub_thread.start()

# 运行主函数
def main():
    # 获取执行python程序的终端命令行参数
    print(sys.argv) #输出为[文件名.py,端口号]
    #取出输入的端口号，并转换为int型
    port=sys.argv[1]
    # 判断格式是否错误
    if len(sys.argv)!=2:
        print("格式错误，格式为：python3 文件名.py 端口号")
        return
    # 判断是否是整型
    if not sys.argv[1].isdigit():
        print("格式错误，端口号为整型")
        return
    # 给服务器类的初始化添加一个端口号参数，用于绑定端口号
    # 创建web服务器对象
    web_server=HttpWebServer(port)
    # 启动Web服务器进行工作
    web_server.start()

if __name__=='__main__':
    main()