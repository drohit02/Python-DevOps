#Python Script :  Variable,Data-Type,Print() function

# 1. Variable Declaration ,Assignment and Data-Type 

_application_name = "UserLoginServiceApp"   # DataType : String
_port = 8080                                # DataType : Number
_environment = "Production"                 # DataType : String
_version = 3.12                             # DataType : Float 
_running = True                             # DataType : Boolean


print("######################## Python App Details ########################\n" \
"Application Name : " + _application_name + "\n"
"Application Port : " + str(_port) + "\n"
"Environment : " + _environment + "\n" 
"Version : " + str(_version) + "\n"
"App Status : " + str(_running)
)

print(f"{_application_name} running on {_port} Port in the {_environment} with the Python Version : {_version}")