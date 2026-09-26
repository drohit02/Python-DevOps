# Python Script : List part 2 : len()
# Create a script that validates a list of application services before deployment.

_service_count = int(input("Enter the Service for the Deployment Status Check ? : "))

_app_service_list = list()

_app_service_name = None
_app_status_code = 0
_app_running_instances = 0
_app_expected_instanes = 0

_ready_app_services = 0
_failed_app_services = 0
_failed_app_services_name = list()


for _app_service in range(0, _service_count):

    print("------------------------------------------------------------")
    print(f"START: App Service {(_app_service + 1)}")
    print("------------------------------------------------------------")

    _app_service_name = str(input(f"Give the App Name : {_app_service + 1} => "))
    _app_status_code = int(input(f"Status Code Returned By App : {_app_service + 1} => "))
    _app_running_instances = int(input(f"How many running instances for App : {_app_service + 1} => "))
    _app_expected_instanes = int(input(f"How many instances need to run for App : {_app_service + 1} => "))

    print("------------------------------------------------------------")
    print(f"END: App Service {(_app_service + 1)}")
    print("------------------------------------------------------------")


    if _app_service_name:

        _app_service_list.append(_app_service_name)

        if _app_status_code != 200 or _app_running_instances < _app_expected_instanes:

            _failed_app_services_name.append(_app_service_name)
            _failed_app_services += 1

        else:

            _ready_app_services += 1

    else:

        print(f"Name is not Given to the App {_app_service + 1}. Not Adding into the list")


print("============================================================")
print(f"Total Number of the Service : {len(_app_service_list)}")
print(f"Ready Services Count : {_ready_app_services}")
print(f"Failed Services Count : {_failed_app_services}")
print(f"Failed Services Names : {_failed_app_services_name}")
print("============================================================")