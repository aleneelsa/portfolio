from breezypythongui import EasyFrame

class NumberFieldDemo(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Temperature Conversion")
        self.addLabel(text = "Celsius", row = 0, column = 0)
        self.celsiusField = self.addIntegerField(value = 0, row = 0, column = 1,width = 10)

        self.far = self.addLabel(text = "Fahrenheit", row = 1, column = 0)
        self.fahrenField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, precision = 2)

# The command button
        self.addButton(text = ">>>>>", row = 2, column = 0, columnspan = 2, command = self.computefahr)

        self.addButton(text = "<<<<<", row = 2, column = 1, columnspan = 2,command = self.computecelsius)

# The event handling method for the button
    def computefahr(self):
        number = self.celsiusField.getNumber()
        result = number * 1.8 + 32
        self.fahrenField.setNumber(result)

    def computecelsius(self):
        number = self.fahrenField.getNumber()
        result = ((number - 32) * 5) / 9
        self.celsiusField.setNumber(result)
