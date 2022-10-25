from math import *
class ScientificCalculation():

    def scientific_calculation(self,input_field_text):
        number=self.text
        self.text=""
        number=int(number)
        if "tan" in input_field_text:
            result=tan(number)
            format_str=f"tan({number})"
        elif "cos" in input_field_text:
            result =cos(number)
            format_str=f"cos({number})"
        elif "sin" in input_field_text:
            result= sin(number)
            format_str=f"sin({number})"
        elif "ln" in input_field_text:
            result=log(number)
            format_str=f"ln({number})"
        elif "log" in input_field_text:
            result=log10(number)
            format_str=f"log({number})"
        elif input_field_text.index("!")==len(input_field_text)-1:
            result =factorial(number)
            format_str=f"{number}!" 

        self.ui.inputfield.setText(f"{result}")
        self.to_output_on_scroll+=f"{format_str}     =      {result} \n"
        self.ui.label.setText(f"{self.to_output_on_scroll}")
        print("Success!")