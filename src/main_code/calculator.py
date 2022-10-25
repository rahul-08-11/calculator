
from qtcalculator import Ui_calculator
import sys
from PyQt5 import  QtWidgets
from functools import partial

from normalcalulation import NormalCalculation
from scientificcalculation import ScientificCalculation

dic_to_store_values={
    "first_value":"",
    "operator":"",
    "second_value":"" 
}

class CalculatorClass(NormalCalculation,ScientificCalculation):
    def __init__(self,ui,dic_to_store_values) -> None:
        print("initializing")
        self.ui=ui
        self.dic=dic_to_store_values
        self.to_output_on_scroll=""
        self.text=""
        self.list_of_elements=[0,1,2,3,4,5,6,7,8,9,"."]
        self.normal_operation_list=["+","-","x","/"]
        self.scientific_normal_operation_list=["tan","sin","cos","ln","log","!"]


        self.ui.button0.clicked.connect(partial(self.checking_inputs,0))
        self.ui.button1.clicked.connect(partial(self.checking_inputs,1))
        self.ui.button2.clicked.connect(partial(self.checking_inputs,2))
        self.ui.button3.clicked.connect(partial(self.checking_inputs,3))
        self.ui.button4.clicked.connect(partial(self.checking_inputs,4))
        self.ui.button5.clicked.connect(partial(self.checking_inputs,5))
        self.ui.button6.clicked.connect(partial(self.checking_inputs,6))
        self.ui.button7.clicked.connect(partial(self.checking_inputs,7))
        self.ui.button8.clicked.connect(partial(self.checking_inputs,8))
        self.ui.button9.clicked.connect(partial(self.checking_inputs,9))
        self.ui.dividebutton.clicked.connect(partial(self.checking_inputs,"/"))
        self.ui.multiplybutton.clicked.connect(partial(self.checking_inputs,"x"))
        self.ui.subtractebutton.clicked.connect(partial(self.checking_inputs,"-"))
        self.ui.addbutton.clicked.connect(partial(self.checking_inputs,"+"))
        self.ui.enterbutton.clicked.connect(self.assign_values_in_dic)
        self.ui.pushButton_5.clicked.connect(self.hide_unhide_calculation_panel)
        self.ui.switchmodetab.activated.connect(self.switch_interface)
        self.ui.tanbutton.clicked.connect(partial(self.checking_inputs,"tan"))
        self.ui.sinbutton.clicked.connect(partial(self.checking_inputs,"sin"))
        self.ui.cosbutton.clicked.connect(partial(self.checking_inputs,"cos"))
        self.ui.lnbutton.clicked.connect(partial(self.checking_inputs,"ln"))
        self.ui.pushButton.clicked.connect(partial(self.checking_inputs,"."))
        self.ui.logbutton.clicked.connect(partial(self.checking_inputs,"log"))
        self.ui.factorialbutton.clicked.connect(partial(self.checking_inputs,"!"))
        self.ui.backspacebutton.clicked.connect(self.one_click_one_ditch)
  

   
    def concatenation(self,value):                                #concatenate the input and set on box
        print("fetching data from user...")
        self.text+=value
        self.ui.inputfield.setText(self.text)

    def checking_inputs(self,value):                                                    
        if value in self.list_of_elements:               #getting values and feeding it into concatenation func
           self.concatenation(f"{value}")
        elif value in self.normal_operation_list or value in self.scientific_normal_operation_list:
           self.concatenation(value)


          
    def assign_values_in_dic(self):

        input_field_text=self.ui.inputfield.text()
        lis=[]
        for operation in self.normal_operation_list:
            lis.append(True) if operation in input_field_text else lis.append(False)

        if True in lis:     
            for value in input_field_text:
                if str.isdigit(value)==False and value!=".":
                    self.dic["first_value"]=input_field_text[:input_field_text.index(value)]
                    self.dic["operator"]=value
                    self.dic["second_value"]=input_field_text[input_field_text.index(value)+1:]
                    self.normal_calculation()
        else:
            self.text=""
            for value in input_field_text:
                if str.isdigit(value):
                    self.text+=value
            self.scientific_calculation(input_field_text)        

       
        
    def hide_unhide_calculation_panel(self):                                          
        check_symbol=self.ui.pushButton_5.text()
        if check_symbol=="↓":
            self.ui.pushButton_5.setText("↑")
            self.ui.scrollArea.setMaximumHeight(90)
            calculator.setFixedHeight(450)


        elif check_symbol=="↑":
            self.ui.pushButton_5.setText("↓")
            self.ui.scrollArea.setMaximumHeight(0)
            calculator.setFixedHeight(363)


    

    def altering_changes(self,shift_value=25):                       #applying changes on window 
        self.ui.pushButton.setFixedHeight(shift_value)  
        self.ui.tanbutton.setFixedHeight(shift_value)
        self.ui.cosbutton.setFixedHeight( shift_value)
        self.ui.sinbutton.setFixedHeight( shift_value)
        self.ui.logbutton.setFixedHeight(shift_value)
        self.ui.factorialbutton.setFixedHeight(shift_value)
        self.ui.lnbutton.setFixedHeight(shift_value)
     

    def switch_interface(self):                            #switching interface ->main function
        mode_name=self.ui.switchmodetab.currentText()
        if mode_name=="Scientific mode":
            self.altering_changes()

        elif mode_name=="Normal mode":
            self.altering_changes(0)    



    def one_click_one_ditch(self):
        split_list=list(self.text)
        split_list.pop()
        clean_up_text="".join(split_list)
        self.ui.inputfield.setText(clean_up_text)
        self.text=clean_up_text
        print("Cleared")


      
app = QtWidgets.QApplication(sys.argv)
calculator = QtWidgets.QMainWindow()
ui = Ui_calculator()
ui.setupUi(calculator)
calculator.show()    
obj=CalculatorClass(ui,dic_to_store_values)


if __name__=="__main__":

    sys.exit(app.exec_())
