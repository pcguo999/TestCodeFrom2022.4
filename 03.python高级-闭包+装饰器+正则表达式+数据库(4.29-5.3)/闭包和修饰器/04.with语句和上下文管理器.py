class File(object):
    # 初始化文件名和打开模式
    def __init__(self,name,model):
        self.name=name
        self.model=model
    # 上文方法
    def __enter__(self):
        print("上文方法")
        self.file=open(self.name,self.model)
        return self.file
    # 下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("下文方法")
        self.file.close()

if __name__=="__main__":
    with File("1.txt","w") as f:
        print("写入数据")
        f.write("Hello World")
