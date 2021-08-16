
from multipledispatch import dispatch


class A:
    @dispatch()
    def f(self):
        print("nothing.")

    @dispatch(float)
    def f(self, x):
        print(f"float: {x}")

    @dispatch(str)
    def f(self, x):
        print(f"str: {x}")

    @dispatch(int)
    def f(self, x):
        print("dispatching to float:", end="  ")
        self.f(float(x))


class B(A):
    @dispatch()
    def f(self):
        super().f()

    @dispatch(object)
    def f(self, x):
        super().f(x)

    @dispatch(float)
    def f(self, x):
        print(f"float from B: {x}")


a = A()
a.f(1.0)
a.f("a")
a.f(1)
a.f()

b = B()
b.f(1.0)
b.f("a")
b.f(1)
b.f()

