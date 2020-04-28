class Phone: # parent class / base class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
    def make_a_call(self,p_number):
        return f"calling {p_number} ........"
    def fullname(self):
        return f"{self.brand} {self.model_name}"
class Phone1: # parent class / base class
    def __init__(self,glass,secondary_mic,primary_mic):
        self.glass = glass
        self.secondary_mic = secondary_mic
        self.primary_mic = primary_mic
    def comp_spec(self):
        return f"{self.glass} , {self.primary_mic} and {self.secondary_mic}"
    def features(self):
        return f"Secondary mix {self.secondary_mic} and primary mic {self.primary_mic}"

class Smartphone(Phone,Phone1): # derived class / child class
    def __init__(self,brand,model_name,price,glass,secondary_mic,primary_mic,ram,internal_m,rare_cam):
        super().__init__
        self.ram = ram
        self.internal_m = internal_m
        self.rare_cam = rare_cam
   
ob2 = Smartphone("OnePlus","Note 8",50000,"Non-Gorilla Glass","Yes","Yes","12 GB","21 GB","90 MP")
 
print(ob2.fullname())
# print(ob2.make_a_call(4220107239559))
# print(f"{ob1.fullname()} and price is {ob1._price}")
# print(ob2.primary_mic)
# print(ob2.features())
# print(ob2.comp_s