class Bus():
    def __init__(self,bus_name,bus_model):
        self.bus_name=bus_name
        self.bus_model=bus_model
        
    def display(self):
        print(f"my bus name is {self.bus_name} and bus model is {self.bus_model}")