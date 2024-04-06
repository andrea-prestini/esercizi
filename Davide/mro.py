class A:
    f = "sono f di A"


class B(A):
    f = "sono f di B"


class C(A):
    f = "sono f di C"


class D(B, C):
    f = "sono f di D"


d = D()
print(d.f)
print()

print("Analizziamo il Method Resolution Order (MRO) di D")
for val in D.mro():
    print(val)
