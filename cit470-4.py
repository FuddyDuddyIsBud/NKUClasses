import subprocess

def main_menu():
    while True:
        print("Please select an option:")
        print("1) Start service")
        print("2) Stop service")
        print("3) Restart service")
        print("4) Enable service")
        print("5) Check service status")
        print("6) Clear screen")
        print("7) Exit script")
        choice = input()
        if choice == '1':
            service_handler("start")
        elif choice == '2':
            service_handler("stop")
        elif choice == '3':
            service_handler("restart")
        elif choice == '4':
            service_handler("enable")
        elif choice == '5':
            check_status()
        elif choice == '6':
            clear = subprocess.run(['clear'])
        elif choice == '7':
            exit()
        else:
            print("Invalid choice. Please try again.")

def service_handler(action):
    service = input("Enter the name of the service to {}: ".format(action))
    if not service_exists(service):
        return
    res = subprocess.run(["systemctl", action, service])
    if res.returncode == 0:
        print("Successfully {}d {} service.".format(action, service))
    else:
        print("Failed to {} {} service with error:{}".format(action, service, res.stderr.decode()))

def check_status():
    service = input("Enter the name of the service to check status: ")
    if not service_exists(service):
        return
    res = subprocess.run(["systemctl", "status", service], stdout=subprocess.PIPE)
    print(res.stdout.decode())

def service_exists(service):
    res = subprocess.run(["systemctl", "list-units", "--all"], stdout=subprocess.PIPE)
    units = res.stdout.decode().split("\n")
    for unit in units:
        if service in unit:
            return True
    print("Service does not exist.")
    return False

main_menu()
