class Patient:
    def __init__(self, patient_id=None, first_name="", last_name="", date_of_birth="", gender="", contact_number="", address=""):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_number = contact_number
        self.__address = address

    # Getters
    def get_patient_id(self):
        return self.__patient_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_gender(self):
        return self.__gender

    def get_contact_number(self):
        return self.__contact_number

    def get_address(self):
        return self.__address

    # Setters
    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_gender(self, gender):
        self.__gender = gender

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Patient [ID={self.__patient_id}, Name={self.__first_name} {self.__last_name}, DOB={self.__date_of_birth}, Gender={self.__gender}, Contact={self.__contact_number}, Address={self.__address}]"
