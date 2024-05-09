# # # a, b = (1, 2)  # unpacking
# # #
# # #
# # # def func(*args):
# # #     pass
# # #
# # #
# # # values = (1, 2, 3, 4, 5)  # unpacking
# # # func(*values)
# # #
# # # my_tuple = 1, 2, 3, 4, 5, 6  # packing
# #
# #
# # # mutable - o'zgaruvchan -  list, dict, set , tuple[mutable]
# # # immutable - o'zgarmas - tuple, primitive types (string, integer, boolean, complex, float)
# #
# # t = (123, [])
# # t[1].append("Hello")
# # print(t)
# #
# # # tuple, list: xotiradan kam yoki ko'p joy olishini isbotlab berish
# # my_tuple = tuple(range(1, 2))
# # my_list = list(range(1, 2))
# # print(my_tuple.__sizeof__())
# # print(my_list.__sizeof__())
# #
# #
# # # p = {[], 1, 2, 3}
# # # print(p)
# #
# # # Stack, Heap
# # # def function(q, /, w, *, e, r):
# # #     pass
# # #
# # #
# # # # type hint
# # #
# # # a: int
# # # a = "10"
# #
# # # OOP - Object Oriented Programming
# #
# # # 1. Encapsulation:
# # #   barcha class o'ziga tegishli bo'lgan barcha parametr va
# # #   hususiyatlarni saqlashi va data hiding ni ham o'z ichiga oladi.
# # class Dog:
# #     def __init__(self, name, age, color):
# #         self.name = name
# #         self._age = age
# #         self.__color = color
# #
# #     def sound(self):
# #         print("woof, woof")
# #
# #
# # # 2. Abstraction:
# # #   Murakkab tizimlarni soddalashtirib, bizga muhim bo'lgan paremetr
# # #   va hususiyatlarni ko'rsatib, kerakmaslarini yasharishiga aytiladi.
# #
# # from abc import ABC, abstractmethod
# #
# #
# # class A(ABC):
# #     @abstractmethod
# #     def my_method(self):
# #         pass
# #
# #
# # class B(A):
# #
# #     def my_method(self):
# #         pass
# #
# #
# # # 3. Inheritance:
# # #   DRY prinsipiga asoslanib, otasida barcha
# # #   parametr va hususiyatlarni o'zizga meros qilib olishiga aytiladi.
# #
# # class X:
# #     def my_method(self):
# #         print("X method")
# #
# #
# # class Y:
# #     pass
# #
# #
# # # y = Y()
# # # print(y.my_method())
# #
# # # class E(X, Y):
# # #     def y_method(self):
# # #         super(Y, self).my_method()
# # #
# # #
# # # E().y_method()
# #
# # # 4. Polymorphism:
# # #   Ota-onasidan o'tgan hususiyatni bolasida o'zgarib ketishiga aytiladi.
# #
# # # class Alfa:
# # #     def my_method(self):
# # #         print("Hello world")
# # #
# # #
# # # class Betta(Alfa):
# # #     def my_method(self):
# # #         print("Hello Python")
# # #
# # #
# # # y = Y()
# # # print(y.my_method())
# #
# #
# # class G:
# #     pass
# #
# #
# # class U(G):
# #     pass
# #
# #
# # class C(G):
# #     pass
# #
# #
# # class P(U, C):
# #     pass
# #
# #
# # print(P.mro())
# #
# #
# # def i(a, b):
# #     pass
# #
# #
# # def i(a):
# #     pass
# #
# #
# # i(1, 2)
# #
# # # pythonda  Overrite ishlaydi Overload ishlamaydi.
# #
# import asyncio
#
#
# # GC - garbage collector
# # reference count -
#
#
# # process, thread
#
#
# # context manager
#
# # class A:
# #     __slots__ = ['name']
# #
#
#
# async def generate():
#     for i in range(1, 20):
#         yield i
#
#
# async def f():
#     async for i in generate():
#         print(i)
#
#
# if __name__ == '__main__':
#     asyncio.run(f())


'''
http method

volume, image, container

'''
# """SELECT COUNT(name) FROM users WHERE name=(SELECT name FROM users WHERE id=1)"""

# SELECT category.name FROM category JOIN product ON category.name == product.category.name;
# view