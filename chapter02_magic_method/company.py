class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


"""
所谓魔法函数（Magic Methods），是Python的一种高级语法，允许你在类中自定义函数（函数名格式一般为__xx__），
并绑定到类的特殊方法中。比如在类A中自定义__str__()函数，则在调用str(A())时，会自动调用__str__()函数，并返回相应的结果。
在我们平时的使用中，可能经常使用__init__函数（构造函数）和__del__函数（析构函数），其实这也是魔法函数的一种。
"""
company = Company(["tom", "bob", "jane"])

# company1= company[:2]
#
print(len(company))

for em in company:
    print(em)
