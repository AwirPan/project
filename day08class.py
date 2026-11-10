class Phone:
    IMEI=None
    producer="IDcast"
    def call_by_4g(self):
        print("4G通话")

class Phone2022(Phone):
    face_id="10001"
    def call_by_5g(self):
        print("2022年新功能:5G开通")

phone=Phone2022()
print(phone.IMEI)
print(phone.producer)
print(phone.face_id)
phone.call_by_4g()
phone.call_by_5g()

class NFCReader:
    nfc_type="第五代"
    producer="HM"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass

myPhone=MyPhone()
myPhone.call_by_4g()
myPhone.read_card()
myPhone.write_card()
myPhone.control()
print(myPhone.producer)