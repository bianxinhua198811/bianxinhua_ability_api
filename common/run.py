# @Time     :2019/10/12 11:25
# @Author   :dengyuting
# @File     :run.py
import os
import random
import sys
import time

# print(os.path.exists('testcases/manager_solution/managersolution_testcases.yml'))
#
# print(os.getcwd())
#
# print(sys.platform)
# print(sys.version)
#
# print(os.environ)
# print(os.getenv("ANDROID_HOME"))
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
# help(random.randint)
# help(range)


# b = a
# c = a.copy()
def search(phrase,letters='aeiou'):
    return set(letters).intersection(phrase)
    # a = ['a', 'e', 'i', 'o', 'u']
    # word = "Don't panic,hello,u!"
    # b = {}
    # for letter in word:
    #     if letter in a:
    #         b.setdefault(letter,0)
    #         # if letter not in b:
    #         #     b[letter]=1
    #         # else:
    #         b[letter]+=1
    # for k,v in sorted(b.items()):
    #     print(k, 'was found', v, "times")

        # if letter in sorted(b):
        #     b[letter] += 1
        #     print(letter, 'was found' , b[letter],"times")

#         if letter not in b:
#             b.append(letter)
# print(b)
# a.remove("o")
# print(a)
# print(a.pop())
# a.append([4,5,6])
# a.extend([1,2,3])
# a.append([])
# list_word = list(word)
# for i in range(4):
#     list_word.pop()
# list_word.pop(0)
# list_word.remove("'")
# list_word.extend([list_word.pop(),list_word.pop()])
# list_word.remove(' ')
# list_word.insert(2,' ')
# new_list_word = ''.join(list_word)

# list_word1 = ''.join(list_word[1:3:1])
# new_list_word = list_word1 +''.join([list_word[5],list_word[4],list_word[-5],list_word[-6]])
# print(new_list_word)
# # print(a.pop())
# help(''.join)
#
#
# b.append("123")
# print(b)
# print(a)
# print(c)