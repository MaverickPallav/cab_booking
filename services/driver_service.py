from models import Driver

def add_driver(system, driver_detail, vehicle_detail, location):
    name, gender, age = driver_detail.split(",")
    system.drivers[name.strip()] = Driver(name.strip(), gender.strip(), int(age.strip()), vehicle_detail.strip(), location)

def update_driver_location(system, driver_name, location):
    if driver_name in system.drivers:
        system.drivers[driver_name].update_location(location)
    else:
        print(f"Driver {driver_name} not found!")

def change_driver_status(system, driver_name, status):
    if driver_name in system.drivers:
        system.drivers[driver_name].change_status(status)
    else:
        print(f"Driver {driver_name} not found!")
