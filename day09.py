class Phone:
    IMEI=None
    producer="itcast"

    def call_by_5g(self):
        print("使用5g进行通话")

class MyPhone(Phone):
    producer = "itheima"
    def call_by_5g(self):
        print("开启CPU单核模式")
        print("使用5g进行通话")
        print("关闭CPU单核模式")
    def call(self):
        print(Phone.producer)
        super().call_by_5g()

myPhone = MyPhone()
print(myPhone.producer)
myPhone.call_by_5g()
myPhone.call()