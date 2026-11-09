class Phone:
    __current_voltage=20
    def __keep_singal_core(self):
        print("让CPU以单核运行")
    def call_by_5G(self):
        if self.__current_voltage>0:
            print("5G通话已开启")
        else:
            self.__keep_singal_core()
            print("电量不足，已切换为单核模式运行")
phone=Phone()
phone.call_by_5G()