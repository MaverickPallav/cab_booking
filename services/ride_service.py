# services/ride_service.py
from models import CabBookingSystem
from services.user_service import update_user_location
from services.driver_service import update_driver_location

def find_ride(system, username, source, destination):
    if username not in system.users:
        print(f"User {username} not found!")
        return []

    available_rides = []
    
    system.users[username].destination = destination

    for driver in system.drivers.values():
        if driver.status and CabBookingSystem.calculate_distance(source, driver.location) <= 5:
            available_rides.append((driver.name, CabBookingSystem.calculate_distance(source, driver.location)))

    available_rides.sort(key=lambda x: x[1])  # Sort by distance
    if not available_rides:
        print("No ride found")
    else:
        print(f"Available rides: {', '.join([f'{ride[0]} [Available]' for ride in available_rides])}")
    return available_rides

def choose_ride(system, username, driver_name):
    if username not in system.users:
        print(f"User {username} not found!")
        return

    if driver_name not in system.drivers:
        print(f"Driver {driver_name} not found!")
        return

    driver = system.drivers[driver_name]
    user = system.users[username]
    
    if driver.status:
        print(f"Ride Started with {driver_name}")

        user.assigned_driver = driver_name
        update_user_location(system, username, user.destination)
        update_driver_location(system, driver_name, user.destination)
        
    else:
        print(f"Driver {driver_name} is not available")

def calculate_bill(system, username):
    if username not in system.users:
        print(f"User {username} not found!")
        return

    user = system.users[username]
    driver = system.drivers[user.assigned_driver]  # Assuming driver is assigned to the user
    # Calculate the distance between user and driver

    distance = CabBookingSystem.calculate_distance(user.location, driver.location)
    # Assuming Rs 10 per unit distance

    fare = distance * 10  # Fare calculation
    driver.calculate_earnings(fare)  # Update driver's earnings
    return fare
