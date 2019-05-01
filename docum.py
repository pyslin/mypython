import re
m = re.search('(?<=abc)def','abcdef')
print(m.group(0))

def abd(n):
    '''
    Function to get absolute value of number.
    Exampel:
    >>>abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    '''
    return n if n>=0 else (-n)
#Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
class Dict(dict):
    """
    Simple dict but also support access x.y style.
    >>>d1 = Dict()
    >>>d1['x'] = 100
    >>>d1.x
    100
    >>>d1.y = 200
    >>>d1['y']
    200
    >>>d2 = Dict(a = 1,b = 2,c = '3')
    >>>d2.c
    '3'
    >>>d2['empty']
    Traceback(most recent call last):
        ...
    KeyError:'empty'
    >>>d2.empty
    Taceback(most recent call last):
        ...
    AttributeError:'Dict' object has no attribute 'empty'
    """

    def __init(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

    def __setattr__(self,key,value):
        self[key] = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()