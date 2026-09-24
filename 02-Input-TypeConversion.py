# Python Script :  input() fucnton ,Type Conversion(type casting in python) and type() function

#Accepting the input

_application_name =  input(f"Enter the App Name : ")
_app_port = input(f"Enter the App Port : ")
_environment = input(f"Enter environment whee App needs to Run : ")
_version = input(f"Enter the App Verison : ")
_app_status = input("Enter app status : ")

# Type Converison in Python and Reassingment
print("+++++++++++++++ Started The Type Conversion +++++++++++++++++++++")
_application_name = str(_application_name)
_app_port = int(_app_port)
_environment = str(_environment)
_version = float(_version)
_app_status = bool(_app_status)

print("+++++++++++++++ Ended The Type Conversion +++++++++++++++++++++")

# Printing the Type of the variable(object) using the type()

print(f"Application Name Data Type : {type(_application_name)}")
print(f"Application Port Data Type : {type(_app_port)}")
print(f"App Environment : {type(_environment)}")
print(f"Application verison : {type(_version)}")
print(f"Application Run status : {type(_app_status)}")