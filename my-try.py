

try:
    print('try...')
    r = 10 / 0
    print('result',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
#当错误发生时，后续语句print('result:', r)不会被执行
#except由于捕获到ZeroDivisionError，因此被执行
#最后，finally语句被执行。
#可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
def foolist():
    pass
try:
    foolist()
except ValueError as e:
    print('ValueError:',e)
except UnicodeError as e:
    print('UnicodeError:',e)
#Python的错误其实也是class，所有的错误类型都继承自BaseException
#使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
print('####')
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try :
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')

main()
