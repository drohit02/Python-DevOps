# PythonScript :  For Loop,range() and counter

#input
_app_service_name = None
_app_status_code = None
_app_response_time = None
_app_cpu_usage = None

#Counter definition
_healthy_app_services = 0
_unhealthy_app_services = 0
_slow_app_services = 0
_high_cpu_app_services = 0

# input for the Services to be monitor
_app_services_count = int(input(f"Enter the App Services Count : "))

for _app_service in range(1 , (_app_services_count+1) ) : 

    print(f"Enter the Following data for App Service : {_app_service}")

    _app_service_name = str(input("Enter the App Service Name ? : "))
    _app_status_code = int(input("Enter the App Status code ? : "))
    _app_response_time = float(input("Give App Response Timein ms ? : "))
    _app_cpu_usage = float(input("Give App CPU Usage ? : "))

    print(f"############################################################")

    if(_app_status_code != 200 or _app_response_time >1000 or _app_cpu_usage >=90.0):

        print(f"App Service : {_app_service_name} System Check ")

        if _app_status_code != 200 : 

            print(f"App Sevice : {_app_service_name} is UNHEALTHY")

            _unhealthy_app_services +=1

        if _app_response_time > 1000 :

            print(f"App Service : {_app_service_name} is SLOW")

            _slow_app_services += 1

        if _app_cpu_usage >= 90 :

            print(f"App Services : {_app_service_name} has HIGH CPU")

            _high_cpu_app_services += 1
    else : 
         print(f"App Service : {_app_service_name} is HEALTHY")
         _healthy_app_services += 1

    print(f"############################################################")

print(f"Total Services Checked Count : {_app_services_count}")

print(f"Number of healthy services : {_healthy_app_services}")

print(f"Number of unhealthy services : {_unhealthy_app_services}")

print(f"Number of slow services : {_slow_app_services}")

print(f"Number of high-CPU services : {_high_cpu_app_services}")

print(f"############################################################")
