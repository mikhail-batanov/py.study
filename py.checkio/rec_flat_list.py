# Решение задачи "Flatten a List" в пайчекио
# Задача: py.checkio.org/ru/mission/flatten-list/
# Автор - M. Batanov, 12.09.19


def flat_list(a):
   n=[]
   f(a, n)
   return(n)


def f(a, n):
   for e in a:
      if type(e) == list:
         f(e, n)
    else:
       n.append(e)
       
