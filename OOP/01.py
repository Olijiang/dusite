'''
定义一个学生类
'''
# 定义一个空的类
class Students():
    pass
# 定义一个对象
mingyue = Students()

# 定义一个类，用来形容学python的学生
class PythonStudent():
    # None 给不确定的值赋值
    name = None
    age = 18
    course = 'python'

    def doHomework(self):
        print('I am doing homework')
        return None

# 实例化一个叫yueyue 的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)


yueyue.doHomework()


