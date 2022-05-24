# 定义学生列表，使用全局变量
student_list=[]

# 显示菜单功能
def Show_menu():
    print("--------学生管理系统--------")
    print("1.添加学生")
    print("2.删除学生")
    print("3.查找学生")
    print("4.修改学生")
    print("5.显示所有学生")
    print("6.退出")

# 1.添加学生
def Add_student():
    name=input("Please input student's name:")
    gender=input("Please input student's gender:")
    # 定义学生字典类型变量
    student_dict={}
    student_dict['name']=name
    student_dict['gender']=gender
    # 添加到学生列表后
    student_list.append(student_dict)

# 2.删除学生
def Del_student():
    name=input("Please input the name you want to delete:")
    i=0
    # 遍历学生列表进行查找，若找到则find标记为位置
    for n in student_list:
        # 若找到则删除3
        if name==n['name']:
            del student_list[i]
            print("Delete ok!")
        else:
            print("Not find it!")

# 3.查找学生
def Find_student():
    name=input("Please input the name you want to find:")
    for n in student_list:
        if name == n['name']:
            print("Find it!")
            print(n)
        else:
            print("Don't find it!")

# 4.修改学生
def Modify_student():
    name=input("Please input the name you want to modify:")
    for n in student_list:
        if name == n['name']:
            print("Find it!")
            n['name']=input("Please input the new name:")
            n['age']=input("Please input the new age:")
        else:
            print("Don't find it!")

# 5.显示所有学生
def Show_students():
    for n in student_list:
        print(n)

# 6.主函数
def run():
    while True:
        Show_menu()
        menu_option=input("Please input the number of the function:")
        if menu_option=='1':
            print("1.添加学生")
            Add_student()
        elif menu_option == '2':
            print("2.删除学生")
            Del_student()
        elif menu_option == '3':
            print("3.查找学生")
            Find_student()
        elif menu_option == '4':
            print("4.修改学生")
            Modify_student()
        elif menu_option == '5':
            print("5.显示所有学生")
            Show_students()
        elif menu_option == '6':
            print("Welcome to come again!")
            break
run()