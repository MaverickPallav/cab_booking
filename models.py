import math
import threading

class User:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.assigned_driver = None
        self.location = (0, 0)
        self.destination = (0, 0)  # Fixed the spelling of 'destination'
        self.lock = threading.Lock()  # Lock for thread-safety
        
    def update_location(self, new_location):
        with self.lock:
            self.location = new_location

class Driver:
    def __init__(self, name, gender, age, vehicle_details, location):
        self.name = name
        self.gender = gender
        self.age = age
        self.vehicle_details = vehicle_details
        self.location = location
        self.status = True  # Driver is initially available
        self.earnings = 0
        self.lock = threading.Lock()  # Lock for thread-safety

    def update_location(self, new_location):
        with self.lock:
            self.location = new_location

    def change_status(self, status):
        with self.lock:
            self.status = status

    def calculate_earnings(self, fare):
        with self.lock:
            self.earnings += fare

class CabBookingSystem:
    def __init__(self):
        self.users = {}  # A dictionary to store users by name
        self.drivers = {}  # A dictionary to store drivers by name
        self.lock = threading.Lock()  # Lock for thread-safety on the entire system

    @staticmethod
    def calculate_distance(location1, location2):
        return math.sqrt((location2[0] - location1[0]) ** 2 + (location2[1] - location1[1]) ** 2)
