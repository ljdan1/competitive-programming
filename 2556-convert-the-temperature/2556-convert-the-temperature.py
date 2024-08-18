class Solution(object):
    def convertTemperature(self, celsius):

        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00  
        return [Kelvin,Fahrenheit]
celsius1 = 36.50
celsius2 = 122.11
first=Solution()
a=first.convertTemperature(celsius1)
b=first.convertTemperature(celsius2)