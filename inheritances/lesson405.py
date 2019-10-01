# multiple inheritance in python
# the method resolution order is depth first
# meaning it will search for the desired class from which it inherits
# and then the parent class if it has inherited, if not then it will search
# in the other class, example may serve good


class A(object):

    def do_this(self):
        print('doing this in A')

# Here the class B inherits from A


class B(A):
    pass


class C(object):

    def do_this(self):
        print('doing this in C')

# here the class D inherits from both, and the both classes C and A have
# the function identical to each other, to verify which one gets called first
# the method resolution order is D-B-A-C


class D(B,C):
    pass


d_instance = D()
d_instance.do_this()
print(D.mro())

# Diamond Shape inheritance


class R(object):

    def do_this(self):
        print('doing this in A')

# Here the class B inherits from A


class S(R):
    pass


class T(R):

    def do_this(self):
        print('doing this in C')

# here if the same class appears in a method resolution order
# the earlier occurrences of that is removed from mro


class U(S, T):
    pass


u_instance = U()
u_instance.do_this()
print(U.mro())



