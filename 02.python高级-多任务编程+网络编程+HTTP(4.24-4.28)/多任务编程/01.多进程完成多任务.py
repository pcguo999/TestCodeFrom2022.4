# import multiprocessing
# import os
# import time
#
#
# # 跳舞任务
# def dance():
#     for i in range(5):
#         print("跳舞中")
#         time.sleep(0.2)  # 每循环一次停留0.2秒，让结果更加清晰
#
#
# # 唱歌任务
# def sing(x1, x2):
#     for i in range(5):
#         print("%s和%s唱歌中" % (x1, x2))
#         print("当前进程编号：%d,当前父进程的编号：%d" % (os.getpid(), os.getppid()))
#         time.sleep(0.2)
#
# # 思考
# def think(name,age):
#     for i in range(5):
#         print("%s思考小明%d岁了" % (name, age))
#         print("当前进程编号：%d,当前父进程的编号：%d" % (os.getpid(), os.getppid()))
#         time.sleep(0.2)
#
# if __name__ == "__main__":  # 若是在当前文件下运行
#     # 创建子进程 dance方法不需要加括号
#     dance_process = multiprocessing.Process(target=dance)
#     # 创建子进程,若需要传参则使用args=(参数)以元组的方式传参
#     sing_process = multiprocessing.Process(target=sing, args=('Tom', 'Jack'))
#     # 创建子进程,若需要传参则使用kwargs={参数}以字典的方式传参
#     think_process = multiprocessing.Process(target=think, kwargs={'name':'Tom', 'age':20})
#
#     # 启动进程
#     dance_process.start()
#     sing_process.start()
#     think_process.start()