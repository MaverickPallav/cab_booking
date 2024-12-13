def find_total_earnings(system):
    print("Total earnings by drivers:")
    for driver in system.drivers.values():
        print(f"{driver.name} earned Rs {driver.earnings}")
