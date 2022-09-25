# 建议使用type

class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is B)
print(isinstance(b, A))
