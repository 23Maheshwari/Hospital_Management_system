from dao.hospital_service_impl import HospitalServiceImpl
from exception.patient_not_found_exception import PatientNumberNotFoundException
from entity.appointment import Appointment


USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "doctor1": {"password": "doc123", "role": "Doctor"},
    "patient1": {"password": "pat123", "role": "Patient"},
}


def login():
    print("===== Hospital Management System Login =====")
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        user = USERS.get(username)
        if user and user["password"] == password:
            print(f"\nLogin successful! Welcome {username} ({user['role']})")
            return user["role"]
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts remaining: {attempts}\n")
    return None

# Main Function
def main():
    role = login()
    if not role:
        print("Too many failed login attempts. Exiting system.")
        return

    service = HospitalServiceImpl()

    while True:
        print("\n===== Hospital Management System =====")
        if role == "Admin":
            print("1. Get Appointment by ID")
            print("2. Get Appointments for Patient")
            print("3. Get Appointments for Doctor")
            print("4. Schedule Appointment")
            print("5. Update Appointment")
            print("6. Cancel Appointment")
            print("7. Exit")
        elif role == "Doctor":
            print("1. View Your Appointments")
            print("2. Exit")
        elif role == "Patient":
            print("1. View Your Appointments")
            print("2. Schedule Appointment")
            print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if role == "Admin":
                if choice == "1":
                    appointment_id = int(input("Enter appointment ID: "))
                    appt = service.get_appointment_by_id(appointment_id)
                    print(appt if appt else "No appointment found.")
                elif choice == "2":
                    patient_id = int(input("Enter patient ID: "))
                    appts = service.get_appointments_for_patient(patient_id)
                    if appts:
                        for appt in appts:
                            print(appt)
                    else:
                        raise PatientNumberNotFoundException("Patient not found in database.")
                elif choice == "3":
                    doctor_id = int(input("Enter doctor ID: "))
                    appts = service.get_appointments_for_doctor(doctor_id)
                    for appt in appts:
                        print(appt)
                elif choice == "4":
                    patient_id = int(input("Enter patient ID: "))
                    doctor_id = int(input("Enter doctor ID: "))
                    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                    description = input("Enter description: ")
                    appointment = Appointment(None, patient_id, doctor_id, appointment_date, description)
                    print("Appointment scheduled." if service.schedule_appointment(appointment) else "Failed to schedule.")
                elif choice == "5":
                    appointment_id = int(input("Enter appointment ID: "))
                    patient_id = int(input("Enter updated patient ID: "))
                    doctor_id = int(input("Enter updated doctor ID: "))
                    appointment_date = input("Enter updated date (YYYY-MM-DD): ")
                    description = input("Enter updated description: ")
                    appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
                    print("Appointment updated." if service.update_appointment(appointment) else "Update failed.")
                elif choice == "6":
                    appointment_id = int(input("Enter appointment ID to cancel: "))
                    print("Cancelled." if service.cancel_appointment(appointment_id) else "Cancel failed.")
                elif choice == "7":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

            elif role == "Doctor":
                if choice == "1":
                    doctor_id = int(input("Enter your doctor ID: "))
                    appts = service.get_appointments_for_doctor(doctor_id)
                    for appt in appts:
                        print(appt)
                elif choice == "2":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

            elif role == "Patient":
                if choice == "1":
                    patient_id = int(input("Enter your patient ID: "))
                    appts = service.get_appointments_for_patient(patient_id)
                    for appt in appts:
                        print(appt)
                elif choice == "2":
                    patient_id = int(input("Enter your patient ID: "))
                    doctor_id = int(input("Enter doctor ID: "))
                    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                    description = input("Enter description: ")
                    appointment = Appointment(None, patient_id, doctor_id, appointment_date, description)
                    print("Appointment scheduled." if service.schedule_appointment(appointment) else "Failed to schedule.")
                elif choice == "3":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

        except PatientNumberNotFoundException as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
