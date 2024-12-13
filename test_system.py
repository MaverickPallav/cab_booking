import unittest
from models import CabBookingSystem
from services import user_service, driver_service, ride_service

class TestCabBookingSystem(unittest.TestCase):
    def setUp(self):
        self.system = CabBookingSystem()

    def test_add_user(self):
        user_service.add_user(self.system, "Abhay, M, 23")
        self.assertIn("Abhay", self.system.users)

    def test_update_user_location(self):
        user_service.add_user(self.system, "Abhay, M, 23")
        user_service.update_user_location(self.system, "Abhay", (10, 10))
        self.assertEqual(self.system.users["Abhay"].location, (10, 10))

    def test_add_driver(self):
        driver_service.add_driver(self.system, "Driver1, M, 22", "Swift, KA-01-12345", (10, 1))
        self.assertIn("Driver1", self.system.drivers)

    def test_find_ride(self):
        user_service.add_user(self.system, "Abhay, M, 23")
        user_service.update_user_location(self.system, "Abhay", (0, 0))
        driver_service.add_driver(self.system, "Driver1, M, 22", "Swift, KA-01-12345", (1, 1))
        available_rides = ride_service.find_ride(self.system, "Abhay", (0, 0), (10, 10))
        self.assertEqual(len(available_rides), 1)

    def test_choose_ride(self):
        user_service.add_user(self.system, "Vikram, M, 29")
        user_service.update_user_location(self.system, "Vikram", (10, 0))
        driver_service.add_driver(self.system, "Driver1, M, 22", "Swift, KA-01-12345", (10, 1))
        ride_service.choose_ride(self.system, "Vikram", "Driver1")
        self.assertEqual(self.system.users["Vikram"].location, (10, 1))
        self.assertEqual(self.system.drivers["Driver1"].location, (10, 1))

    def test_calculate_bill(self):
        user_service.add_user(self.system, "Vikram, M, 29")
        user_service.update_user_location(self.system, "Vikram", (10, 0))
        driver_service.add_driver(self.system, "Driver1, M, 22", "Swift, KA-01-12345", (10, 1))
        ride_service.choose_ride(self.system, "Vikram", "Driver1")
        bill = ride_service.calculate_bill(self.system, "Vikram")
        self.assertEqual(bill, 10)  # Bill should be based on the distance between Vikram and Driver1 (distance = 1)

if __name__ == "__main__":
    unittest.main()
