
class NormalCalculation():

    def normal_calculation(self):
        self.text=""
        self.ui.inputfield.clear()
        operation=self.dic["operator"]
        first_value = float(self.dic["first_value"])
        second_value = float(self.dic["second_value"])
        if operation=="+":
           result=first_value+second_value
        elif operation=="/":
            result=first_value/second_value


        elif operation=="x":
            result=first_value*second_value

        elif operation=="-":
            result=first_value-second_value

        self.ui.inputfield.setText(f"{result}")
        self.to_output_on_scroll+=f"{first_value}{operation}{second_value}   =      {result} \n"
        self.ui.label.setText(f"{self.to_output_on_scroll}")
        print("Success!")
