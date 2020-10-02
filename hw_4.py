# Задание 1
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не
# является числом (любым числом: целым, отрицательным, дробным), то должна выполняться
# конкатенация, т. е. соединение, строк. В остальных случаях введённые числа суммируются.
# a = input("Введите любое число a: ")
# b = input("Введите любое число b: ")
# try:
#     print("Результат: ", int(a)+int(b))
# except ValueError:
#     print("Результат: ", a+b)

# Задание 3. Со значениями по умолчанию
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
# стоит «!». По умолчанию 0
#неадекватный способ)))
# def song(a=3, b=3, flag=False):
#     word = "la"
#     res,result="", ""
#     i,j=1,1
#     a = int(a)
#     b = int(b)
#     while i<=a:
#         while j!=b:
#             result= (word + "-") * j
#             j += 1
#             if(j==b):
#               result+=word
#         if(i!=a):
#             res+=result+"\n"
#         else:
#             res+=result
#         i+=1
#     if flag:
#         res+="!"
#     else:
#         res+="."
#     return res
#
#адекватный способ))
# def laoutput(a=3, b=3, flag=False):
#     if flag:
#         return (("la-"*(b-1)+"la"+"\n")*a).rstrip()+"!"
#     return (("la-"*(b-1)+"la"+"\n")*a).rstrip()+"."
# print(laoutput(5,7,0))

#Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов
#(неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов.

# def second_min_value(*args):
#     l = sorted(list(args))
#     min_count = l.count(min(l))
#     return l[min_count]
#
# print(second_min_value(3,4,9,22,2,2,3,2,2,2,233))

# Задание 3
# Оформляем в функции наши задания с урока и предыдущих ДЗ:
#     1) Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
#     Функция возвращает введённое число.

def user_input_num():
    flag=1
    while flag:
        user_num = input("Введите число: ")
        if user_num.lstrip('-').replace('.','',1).isdigit():
            flag=1
            break
    return user_num
#
# print("Наконец-то: ", user_input_num())

# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!
#     2) Пишем функцию, которая попросит пользователя ввести слово (строка из буквенных символов без пробелов
#     в середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите его ввести.
#     Функция возвращает введённое слово.
# def user_input_num():
#     """function asks the user for a string and checks"""
#     flag=1
#     while flag:
#         user_str = input("Введите строку без пробелов: ").strip()
#         if user_str.count(" ") == 0:
#             flag=0
#             break
#     return user_str
# print("Наконец-то: ", user_input_num())

#     3) Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
#     и False иначе.
# def is_year_leap(years):
#     years = int(years)
#     if years%4==0 and years%100!=0:
#         return True
#     elif years%100==0 and years%400==0:
#         return True
#     else:
#        return False
# print(is_year_leap(2000))

#     4) Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
#     Если треугольник существует, вернёт True, иначе False.
# def is_exist_triangle(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
# print(is_exist_triangle(5,7,10))

#     5) Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
#     и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle
#     (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
# def get_type_triangle(a,b,c):
#     flag = is_exist_triangle(a,b,c)
#     if flag:
#         if a==c and a==b and b==c:
#             print("Equilateral triangle")
#         else:
#             if a==c or a==b or b==c:
#                 print("Isosceles triangle")
#             else:
#                 print("Versatile triangle")
#     else:
#         print("Not a triangle")
# get_type_triangle(5,7,10)


#     6) Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющую
#     расстояние между точками с координатами (x1, y1) и (x2, y2).
# # *Считайте четыре действительных числа от пользователя (перед запуском функции, не внутри функции) и выведите результат
# работы этой функции.
# x, count=[], 0
# while count<4:
#        x.append(user_input_num())
#        count+=1
# print(x)
# def distance(x1,y1,x2,y2):
#     ab = ((x2-x1)**2+(y2-y1)**2)**0.5
#     return ab
# print(distance(2,3,4,5))
#

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
my_words = ["bed", "ed", "e", "google", "device", "dad", "mom","ddddd"]
def match_ends(words):
    count = 0
    for i in range(len(words)):
        if len(words[i])>=2:
            if words[i][0]==words[i][-1]:
                count+=1
    return count
print(match_ends(my_words))


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
li = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
def front_x(words):
    lst_x = []
    for i in words:
        if i[0] =='x':
            lst_x.append(i)
            words.remove(i)
    return lst_x + sorted(words)

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use sorted() function and a custom key= function to extract the last element form each tuple.
lst = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def sort_last(tuples):
    # for i in tuples:
    #     sorted(tuples, key=custom_sort_last_element(i))
    # return tuples
    return sorted(tuples, key=lambda tup: (tup[-1]))
print(sort_last(lst))

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\n', 'front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\n', 'sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
