import pymysql

# 创建表SQL语句
# CREATE TABLE `student`.`student_table` (
#   `idstudent_table` INT NOT NULL AUTO_INCREMENT,
#   `name` VARCHAR(45) NOT NULL,
#   `gender` VARCHAR(4) NOT NULL,
#   `class` INT NOT NULL,
#   PRIMARY KEY (`idstudent_table`));

class Student(object):
    # 初始化连接数据库
    def __init__(self, target_db, username, password):
        self.connect = pymysql.Connect(host='localhost', port=3306, database=target_db, user=username,passwd=password, charset='utf8')
    # 对象销毁时执行关闭数据库
    def __del__(self):
        self.connect.close()
    # 打印目录
    def print_menu(self):
        print('1. 查看所有学生信息')
        print("2. 查看某个学生信息")
        print("3. 增加学生信息")
        print("4. 给每个班都分配老师")
        print("5. 修改班级老师信息")
        print("6. 修改学生信息")
        print("7. 删除学生信息")
        print("8. 退出系统")
    # 查看所有学生信息
    def __print_all_student(self):
        # 获取游标对象
        cursor=self.connect.cursor()
        count=cursor.execute("select * from student_table;")
        if count==0:
            print("表为空")
            return
        # 获取结果集
        result=cursor.fetchall()
        # 输出结果
        for x in result:
            print(x)
        # 关闭游标
        cursor.close()
    # 查看某个学生信息
    def __print_only_student(self):
        # 获取游标对象
        cursor=self.connect.cursor()
        flag=input("按学号查询请输入1，按姓名查询请输入2：")
        if flag=='1':
            id = input("要查询的学生学号")
            cursor.execute("select * from student_table where idstudent_table=%d;"%int(id))
        elif flag=='2':
            name=input("要查询的学生姓名")
            cursor.execute("select * from student_table where name='%s';"%name)
        else:
            print("输入非法")
            return
        # 获取结果集
        result=cursor.fetchall()
        # 输出结果
        print(result)
        # 关闭游标
        cursor.close()
    # 添加学生
    def __add_student(self):
        # 获取游标对象
        cursor = self.connect.cursor()
        name = input("要添加的学生姓名")
        gender = input("要添加的学生性别")
        No_class = input("要添加学生的班级")
        # 查看是否有老师选项
        cursor.execute("desc student_table;")
        result = cursor.fetchall()
        teacher=0
        for i in result:
            if i[0]==teacher:
                teacher=1
        # 若老师存在
        if teacher == 1:
            teacher_name = input("要添加学生的老师")
            # 执行SQL结果
            sql="insert into student_table (name,gender,class,teacher) values ('%s','%s','%s','%s');"%(name,gender,int(No_class),teacher_name)
        else:
            # 执行SQL结果
            sql = "insert into student_table (name,gender,class) values ('%s','%s','%s');"%(name, gender, int(No_class))
        cursor.execute(sql)
        # 将修改数据提交到数据库
        self.connect.commit()
        # 关闭游标
        cursor.close()
    # 给每个班级分配老师
    def __add_teacher(self):
        # 获取游标对象
        cursor = self.connect.cursor()
        # 查看是否有老师选项
        cursor.execute("desc student_table;")
        result = cursor.fetchall()
        teacher = 0
        for i in result:
            if i[0] == 'teacher':
                teacher = 1
        # 因为result结果为元组，并且第一个元素为字段名，所以使用i[0]
        # ('idstudent_table', 'int', 'NO', 'PRI', None, 'auto_increment')
        # ('name', 'varchar(45)', 'NO', '', None, '')
        # ('gender', 'varchar(4)', 'NO', '', None, '')
        # ('class', 'int', 'NO', '', None, '')
        # 若老师不存在则添加字段
        if teacher == 0:
            sql = "alter table student_table add teacher varchar(45);"
            cursor.execute(sql)
            # 将修改数据提交到数据库
            self.connect.commit()
        # 添加老师信息
        # 查找班级信息
        cursor.execute("select distinct class from student_table")
        class_num = cursor.fetchall()
        # print(class_num) #((1,), (2,), (4,))
        # 给每个班分配老师
        for i in class_num:
            # print(type(i)) # 单个数据元组的第一个数据为其值
            teacher=input("请输入%d班老师姓名："%i[0])
            # 分配老师
            cursor.execute("update student_table set teacher='%s' where class=%d"%(teacher,i[0]))
        # 将修改数据提交到数据库
        self.connect.commit()
        # 关闭游标
        cursor.close()
    # 更换老师
    def __alter_teacher(self):
        # 获取游标对象
        cursor = self.connect.cursor()
        # 查看是否有老师选项
        cursor.execute("desc student_table;")
        result = cursor.fetchall()
        teacher = 0
        for i in result:
            if i[0] == 'teacher':
                teacher = 1
        # 若老师不存在输出错误并退出函数
        if teacher == 0:
            print("并未分配老师")
            return
        class_num = input("要更改的班级")
        teacher = input("重新分配的老师姓名")
        cursor.execute("update student_table set teacher='%s' where class='%d'"% (teacher, int(class_num)))
        # 将修改数据提交到数据库
        self.connect.commit()
        # 关闭游标
        cursor.close()
    # 修改学生信息
    def __alter_student(self):
        # 获取游标对象
        cursor = self.connect.cursor()
        # 查看学生原信息
        id=input("请输入要查询的学生学号")
        cursor.execute("select * from student_table where idstudent_table='%d';"%int(id))
        result = cursor.fetchall()
        print(result)
        name = input("修改后的学生姓名")
        gender = input("修改后的学生性别")
        No_class = input("修改后学生的班级")
        # 查看是否有老师
        teacher = 0
        for i in result:
            if i[0] == 'teacher':
                teacher = 1
        # 若老师存在
        if teacher == 1:
            teacher_name = input("修改后的老师姓名")
            cursor.execute("update student_table set name='%s',gender='%s',class='%d', teacher='%s' where idstudent_table='%d';"% (name, gender, int(No_class), teacher_name, int(id)))
        else:
            cursor.execute("update student_table set name='%s',gender='%s',class='%d' where idstudent_table='%d';"%(name, gender, int(No_class), int(id)))
        # 将修改数据提交到数据库
        self.connect.commit()
        # 关闭游标
        cursor.close()
    # 删除学生
    def __del_student(self):
        # 获取游标对象
        cursor = self.connect.cursor()
        id = input("请输入要删除的学生学号")
        cursor.execute("delete from student_table where idstudent_table='%d';"% int(id))
        # 将修改数据提交到数据库
        self.connect.commit()
        # 关闭游标
        cursor.close()
    # 运行主函数
    def main(self):
        while True:
            self.print_menu()
            index=input("请输入要执行的操作：")
            if index=='1':
                self.__print_all_student()
            elif index=='2':
                self.__print_only_student()
            elif index=='3':
                self.__add_student()
            elif index=='4':
                self.__add_teacher()
            elif index=='5':
                self.__alter_teacher()
            elif index=='6':
                self.__alter_student()
            elif index=='7':
                self.__del_student()
            elif index == '8':
                return

handle_student = Student("student","root","root")
handle_student.main()