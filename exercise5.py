# create a laptop class with attributes like brand name,model name and price
# create two objects of your laptop class
class Laptop:
    def __init__(self,Brand_Name,Model_Name,Price):
        self.Brand_Name = Brand_Name
        self.Model_Name = Model_Name
        self.Price = Price
    def Lap_Com_Info(self):
        return f"Brand name is {self.Brand_Name} of model {self.Model_Name} and price is {self.Price}"
Lp1 = Laptop("Google","Chrome Book",120000)
Lp2 = Laptop("HP","Elite Book",500000) 
print(Laptop.Lap_Com_Info(Lp1))
print(Laptop.Lap_Com_Info(Lp2))
###########################################################################
class Laptop:
    def __init__(self,Brand_Name,Model_Name,Price):
        self.Brand_Name = Brand_Name
        self.Model_Name = Model_Name
        self.Price = Price
        self.Lp_Full_Info
    def Lap_Com_Info(self):
        return f"Brand name is {self.Brand_Name} of model {self.Model_Name} and price is {self.Price}"
Lp1 = Laptop("Google","Chrome Book",120000)
Lp2 = Laptop("HP","Elite Book",500000) 
print(Laptop.Lap_Com_Info(Lp1))
print(Laptop.Lap_Com_Info(Lp2))