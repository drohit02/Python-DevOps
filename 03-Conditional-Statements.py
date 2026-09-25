# Python Script : Conditional Statement using the if-else,elif

_application_name = str(input("Enter the Name App : "))
_environment = str(input("Enter the Environment : "))
_app_status_code = int(input("App Status Code Received : "))
_cpu_usage = float(input("Enter App Cpu Utilization  : "))
_memory_usage = float(input("Enter App Memory Utilization : "))
_disk_usage = float(input("Total Server Disk Space : "))
_running_instances = int(input("How many App Server running ? : "))
_expected_instances = int(input("How many App Server required ? :"))
_error_received = int(input("How many error reported ? : "))
_warning_received = int(input("How many warning reported ? : "))

_deployement_decision = None


print(f"Checking the App Health Before Deployment.....!!!")

print("################ Deployment Gates #################")

print(f"Application Name : {_application_name}")
print(f"Application Environment : {_environment}")


if _environment.upper() == "PRODUCTION":

    if _app_status_code != 200 or _cpu_usage >= 85 or _memory_usage >= 85 or _disk_usage >= 90 or _running_instances < _expected_instances or _error_received > 10:

        _deployement_decision = "BLOCKED"

        print(f"########### Failed Checked #############")

        if _app_status_code != 200:
            print(f"HTTP Status Code is : {_app_status_code}")

        if _cpu_usage >= 85:
            print(f"CPU Utilization is High : {_cpu_usage}")

        if _memory_usage >= 85:
            print(f"Memory Utilization is High : {_memory_usage}")

        if _disk_usage >= 90:
            print(f"Disk Usage is High : {_disk_usage}")

        if _running_instances < _expected_instances:
            print(f"Running Instances : {_running_instances} is Less than Expected Instances : {_expected_instances}")

        if _error_received > 10:
            print(f"App received huge number of {_error_received} errors")

        print(f"Deployment Status : {_deployement_decision}")

    elif (_cpu_usage >= 70 and _cpu_usage < 85) or (_memory_usage >= 70 and _memory_usage < 85) or (_disk_usage >= 80 and _disk_usage < 90) or _warning_received > 20:

        _deployement_decision = "WARNING"

        print(f"########### Warning Checked #############")

        if _cpu_usage >= 70 and _cpu_usage < 85:
            print(f"CPU Utilization is Abnormal : {_cpu_usage}")

        if _memory_usage >= 70 and _memory_usage < 85:
            print(f"Memory Utilization is Abnormal : {_memory_usage}")

        if _disk_usage >= 80 and _disk_usage < 90:
            print(f"Disk Usage is Abnormal : {_disk_usage}")

        if _warning_received > 20:
            print(f"App received huge number of {_warning_received} warnings")

        print(f"Deployment Status : {_deployement_decision}")

    else:

        _deployement_decision = "ALLOWED"

        print(f"Failed Check : None")
        print(f"Warnings Check : None")
        print(f"Deployment Status : {_deployement_decision}")


elif _environment.upper() == "DEVELOPMENT":

    if _app_status_code != 200 or _cpu_usage >= 95 or _memory_usage >= 95 or _disk_usage >= 95 or _running_instances < _expected_instances or _error_received > 50:

        _deployement_decision = "BLOCKED"

        print(f"########### Failed Checked #############")

        if _app_status_code != 200:
            print(f"HTTP Status Code is : {_app_status_code}")

        if _cpu_usage >= 95:
            print(f"CPU Utilization is High : {_cpu_usage}")

        if _memory_usage >= 95:
            print(f"Memory Utilization is High : {_memory_usage}")

        if _disk_usage >= 95:
            print(f"Disk Usage is High : {_disk_usage}")

        if _running_instances < _expected_instances:
            print(f"Running Instances : {_running_instances} is Less than Expected Instances : {_expected_instances}")

        if _error_received > 50:
            print(f"App received huge number of {_error_received} errors")

        print(f"Deployment Status : {_deployement_decision}")

    elif (_cpu_usage >= 90 and _cpu_usage < 95) or (_memory_usage >= 90 and _memory_usage < 95) or (_disk_usage >= 90 and _disk_usage < 95) or _warning_received > 50:

        _deployement_decision = "WARNING"

        print(f"########### Warning Checked #############")

        if _cpu_usage >= 90 and _cpu_usage < 95:
            print(f"CPU Utilization is Abnormal : {_cpu_usage}")

        if _memory_usage >= 90 and _memory_usage < 95:
            print(f"Memory Utilization is Abnormal : {_memory_usage}")

        if _disk_usage >= 90 and _disk_usage < 95:
            print(f"Disk Usage is Abnormal : {_disk_usage}")

        if _warning_received > 50:
            print(f"App received huge number of {_warning_received} warnings")

        print(f"Deployment Status : {_deployement_decision}")

    else:

        _deployement_decision = "ALLOWED"

        print(f"Failed Check : None")
        print(f"Warnings Check : None")
        print(f"Deployment Status : {_deployement_decision}")


else:
    print(f"No Deployment Stage is available for the Environment : {_environment}")