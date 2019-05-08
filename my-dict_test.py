import unittest

from mydict import Dict

#编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1,b='test')
#self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
#测试d是否 dict类型
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
#d['key'] ='value' 情况下 d.key是否等于value
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key ='value'
#d.key = value情况下，后面是否
        self.assertTrue('key'in d )
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
# 通过d['empty'] 访问不存在的key时，断言会抛出KeyError
        with self.assertRaises(KeyError):
            value = d.empty

    def test_attrerror(self):
        d = Dict()
        with self.assertRaise(AttributeError):
            value = d.empty
#设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，
# 在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()



