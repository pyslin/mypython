

class Dict(dict):

    def __init__(self,**kw):
        super().__init__(**kw)
#get方法，要传入self 和key 得到self[ket]
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict'object has no attribute'%s'"%key)

    def __setattr__(self,key,value):
        self[key] = value




