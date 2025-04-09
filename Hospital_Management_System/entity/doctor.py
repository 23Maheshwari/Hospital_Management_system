class Doctor:
    def __init__(self, doctor_id=None, first_name="", last_name="", specialization="", contact_number=""):
        self.__doctor_id = doctor_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialization = specialization
        self.__contact_number = contact_number

    # Getters
    def get_doctor_id(self):
        return self.__doctor_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_specialization(self):
        return self.__specialization

    def get_contact_number(self):
        return self.__contact_number

    # Setters
    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def __str__(self):
        return f"Doctor [ID={self.__doctor_id}, Name={self.__first_name} {self.__last_name}, Specialization={self.__specialization}, Contact={self.__contact_number}]"
