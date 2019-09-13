class Joe(object):

    greeting = 'Hello, Joe'

    # whenever a function is defined in the python class
    # the current instance is passed to it by default
    # notice the self key word in the function which
    # is not sent through tbe function, but throws an
    # error when not removed from the definition inside the class
    # Because of this automatic passing of the instance instance methods are called "bound" methods.

    def call_me_from_the_class(self):
        print('calling the function')


joe_obj = Joe()
print(joe_obj.greeting)

# whenever instance method is called from the object's members the instance is
# passed implicitly.

joe_obj.call_me_from_the_class()


