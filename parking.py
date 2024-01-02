import time
import random
from datetime import datetime, timedelta
import pytesseract
from PIL import Image

class ParkingSystem:
    def __init__(self):
        self.vehicles = []

    def vehicle_entry(self):
        license_plate = self.recognize_license_plate()
        qr_code = self.generate_qr_code()
        entry_time = datetime.now()

        vehicle = {
            "license_plate": license_plate,
            "qr_code": qr_code,
            "entry_time": entry_time,
        }

        self.vehicles.append(vehicle)

        print(f"Vehicle entered. License Plate: {license_plate}, QR Code: {qr_code}")

    def vehicle_exit(self):
        license_plate = input("Enter vehicle license plate for exit: ")

        for vehicle in self.vehicles:
            if vehicle["license_plate"] == license_plate:
                exit_time = datetime.now()
                time_difference = exit_time - vehicle["entry_time"]
                amount_due, hourly_rate, total_hours_parked = self.calculate_parking_fee(time_difference)

                print(f"License Plate: {license_plate}")
                print(f"Hours Parked: {total_hours_parked:.2f} hours")
                print(f"Amount Due: ₹{amount_due:.2f}")
                print(f"Hourly Rate: ₹{hourly_rate:.2f}")
                payment_method = input("Choose payment method (cash/online): ")

                if payment_method == "cash":
                    self.open_cash_box()
                    self.close_cash_box()
                elif payment_method == "online":
                    payment_success = self.process_online_payment()
                    if payment_success:
                        print("Payment successful. Thank you!")
                        self.open_exit_barrier()
                        self.close_exit_barrier()
                    else:
                        print("Payment failed. Please try again.")
                else:
                    print("Invalid payment method.")

                self.vehicles.remove(vehicle)
                return

        print("Vehicle not found.")

    def recognize_license_plate(self):
        # Simulated OCR using a random license plate for demonstration purposes
        # In a real system, you would capture an image and use pytesseract on that image
        fake_license_plate = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000, 9999)}"
        return fake_license_plate

    def generate_qr_code(self):
        # Simplified QR code generation (use a proper library in a real system)
        return random.randint(100000, 999999)

    def calculate_parking_fee(self, duration):
        # Simplified fee calculation (use a proper algorithm in a real system)
        hourly_rate = 0.0001  # Adjust this based on your actual hourly rate
        total_seconds = duration.total_seconds()
        total_hours_parked = total_seconds / 3600
        amount_due = total_hours_parked * hourly_rate + 20  # Add a fixed amount of 20

        return amount_due, hourly_rate, total_hours_parked

    def open_cash_box(self):
        print("Opening cash box...")

    def close_cash_box(self):
        time.sleep(5)  # Simulate the time it takes for a cash transaction
        print("Closing cash box...")

    def process_online_payment(self):
        # Simulate online payment processing
        return random.choice([True, False])

    def open_exit_barrier(self):
        print("Opening exit barrier...")

    def close_exit_barrier(self):
        time.sleep(20)  # Simulate the time it takes for the barrier to close
        print("Closing exit barrier...")

# Example usage
parking_system = ParkingSystem()

while True:
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Exit Program")
    choice = input("Enter your choice: ")

    if choice == "1":
        parking_system.vehicle_entry()
    elif choice == "2":
        parking_system.vehicle_exit()
    elif choice == "3":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
