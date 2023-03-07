from abstract import is_monoid
from random import randint

def test1():
    def gen():
        return randint(0,100-1)
    
    def member(x):
        return 0 <= x < 100
    
    def monoid_plus(x,y):
        return (x + y) % 100
    
    assert is_monoid(gen, member, 0, monoid_plus)

def test2():
    def gen():
        return randint(0,100-1)
    
    def member(x):
        return 0 <= x < 100
    
    def monoid_times(x,y):
        return (x * y) % 100
    
    assert is_monoid(gen, member, 1, monoid_times)


test1()
test2()