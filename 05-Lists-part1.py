# List : DevOps Service Inventory

_service_count = 0
_service_list = list()
_app_service_name =  None
_is_service_present = False

_service_count =  int(input("Enter the Num of the Services ? : "))

for _app_service in range(1 , _service_count+1) :
    
    _app_service_name = str(input(f"Enter the Name of App : {_app_service} => "))
    _service_list.append(_app_service_name)

print("-------------------------------------------------------------------------")
print(f"Total Number of Services : {len(_service_list)}")
print("-------------------------------------------------------------------------")

for _app_service in range(0 , len(_service_list)) : 
    print(f"App Service in Service List at : {_app_service+1} location => {_service_list[_app_service]}\n")

print("-------------------------------------------------------------------------\n")

_locate_service = str(input("Enter the Service need to found in Service-List ? : "))

for _app_service in range(0 , len(_service_list)) : 

    if (_service_list[_app_service].lower() == _locate_service.lower()) : 
        _is_service_present = True
        break
       


if(_is_service_present) :
    print(f"App Service found at Index : {_app_service} i.e. location => {_app_service+1} : {_locate_service}")
else :
    print(f"App Service Not Found in Service List")