from dao.IHospitalService import IHospitalService
from entity.appointment import Appointment
from util.db_conn_util import DBConnUtil
from exception.patient_not_found_exception import PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):

    def schedule_appointment(self, appointment: Appointment) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO appointment (appointment_id, patient_id, doctor_id, appointment_date, description)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                appointment.get_appointment_id(),
                appointment.get_patient_id(),
                appointment.get_doctor_id(),
                appointment.get_appointment_date(),
                appointment.get_description()
            )

            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Error scheduling appointment: {e}")
            return False

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM appointment WHERE appointment_id = %s"
            cursor.execute(query, (appointment_id,))
            row = cursor.fetchone()

            if row:
                return Appointment(*row)
            else:
                raise Exception("Appointment not found")

        except Exception as e:
            print(f"Error: {e}")
            return None

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_appointments_for_patient(self, patient_id: int) -> list[Appointment]:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM appointment WHERE patient_id = %s"
            cursor.execute(query, (patient_id,))
            rows = cursor.fetchall()

            if not rows:
                raise PatientNumberNotFoundException("Patient ID not found!")

            return [Appointment(*row) for row in rows]

        except PatientNumberNotFoundException as e:
            print(e)
            return []

        except Exception as e:
            print(f"Error: {e}")
            return []

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_appointments_for_doctor(self, doctor_id: int) -> list[Appointment]:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM appointment WHERE doctor_id = %s"
            cursor.execute(query, (doctor_id,))
            rows = cursor.fetchall()

            return [Appointment(*row) for row in rows]

        except Exception as e:
            print(f"Error: {e}")
            return []

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def update_appointment(self, appointment: Appointment) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE appointment
                SET patient_id = %s, doctor_id = %s, appointment_date = %s, description = %s
                WHERE appointment_id = %s
            """
            values = (
                appointment.get_patient_id(),
                appointment.get_doctor_id(),
                appointment.get_appointment_date(),
                appointment.get_description(),
                appointment.get_appointment_id()
            )

            cursor.execute(query, values)
            conn.commit()

            return cursor.rowcount > 0

        except Exception as e:
            print(f"Error updating appointment: {e}")
            return False

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def cancel_appointment(self, appointment_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()

            query = "DELETE FROM appointment WHERE appointment_id = %s"
            cursor.execute(query, (appointment_id,))
            conn.commit()

            return cursor.rowcount > 0

        except Exception as e:
            print(f"Error cancelling appointment: {e}")
            return False

        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()
