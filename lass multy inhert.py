#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird
#如果需要“混入”额外的功能，通过多重继承就可以实现，
## 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass