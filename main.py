from services import user_service, driver_service, ride_service, earnings_service
from models import CabBookingSystem

def main():
    system = CabBookingSystem()

    # Onboard users
    user_service.add_user(system, "Abhay, M, 23")
    user_service.update_user_location(system, "Abhay", (0, 0))

    user_service.add_user(system, "Vikram, M, 29")
    user_service.update_user_location(system, "Vikram", (10, 0))

    user_service.add_user(system, "Kriti, F, 22")
    user_service.update_user_location(system, "Kriti", (15, 6))

    # Onboard drivers
    driver_service.add_driver(system, "Driver1, M, 22", "Swift, KA-01-12345", (10, 1))
    driver_service.add_driver(system, "Driver2, M, 29", "Swift, KA-01-12345", (11, 10))
    driver_service.add_driver(system, "Driver3, M, 24", "Swift, KA-01-12345", (5, 3))

    # Test finding and choosing rides
    ride_service.find_ride(system, "Vikram", (10, 0), (15, 3))
    ride_service.choose_ride(system, "Vikram", "Driver1")
    ride_service.calculate_bill(system, "Vikram")

    # Change driver status and try again
    driver_service.change_driver_status(system, "Driver1", False)
    ride_service.find_ride(system, "Kriti", (15, 6), (20, 4))

    # Calculate total earnings
    earnings_service.find_total_earnings(system)

if __name__ == "__main__":
    main()
