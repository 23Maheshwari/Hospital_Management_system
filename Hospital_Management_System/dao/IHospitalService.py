from abc import ABC, abstractmethod
from entity.appointment import Appointment

class IHospitalService(ABC):

    @abstractmethod
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        pass

    @abstractmethod
    def get_appointments_for_patient(self, patient_id: int) -> list[Appointment]:
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, doctor_id: int) -> list[Appointment]:
        pass

    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def update_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id: int) -> bool:
        pass
