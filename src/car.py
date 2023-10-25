class Car():
    def __init__(self,car_name,car_model):
        self.car_name=car_name
        self.car_model=car_model
        
    def display(self):
        print(f"my car model is {self.car_name} and car model is {self.car_model}")