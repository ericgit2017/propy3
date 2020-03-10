# coding:utf-8
"""
@author: Wonder
@file: Exam06.py.py
@time: 2020/03/05
"""
from decimal import Decimal


class Person:
    country = "中国"

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @classmethod
    def get_country(cls):
        country = cls.country
        return country

    @staticmethod
    def get_person_country():
        return divmod(10, 3)


def main():
    a = 0b01011010
    b = 0b10010011
    p1 = Person('zhangs', 35)
    p2 = Person()
    dict1 = {"name": "jack", "age": 92}

    print(p1.get_name(), p2.get_name())
    print("类方法调用：", Person.get_country())
    print(Person.get_person_country())
    print(0.1+0.1+0.1-0.3)
    print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
    print("a&b", bin(a & b))
    print("a|b", bin(a | b))
    print("a^b", bin(a ^ b))
    print("a>>2", bin(a >> 2))
    print("a<<2", bin(a << 2))
    print("~a", bin(~a))
    print("5>3?'good':'bad'", "good" if 5 > 3 else "bad")
    print("格式化：i am %(name)s, age %(age)d" % dict1)


if __name__ == '__main__':
    main()
