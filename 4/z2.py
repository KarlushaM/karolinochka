class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, temp):
        if  temp < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        self.__celsius = temp

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32
    
temp = Temperature(25)
print(temp.fahrenheit)  
temp.celsius = -300