"""
    shellからの呼び出し引数は、sys.argvで受け取れることを確認する


"""


# https://docs.python.org/ja/3.7/tutorial/interpreter.html#argument-passing
import sys

print("sys.argv[0] = " + sys.argv[0] )
print("sys.argv[1] = " + sys.argv[1] )
print("sys.argv[2] = " + sys.argv[2] )



print('hello = ' + sys.argv[1] )
