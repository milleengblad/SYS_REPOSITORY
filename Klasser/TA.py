class TA:
    """Klasse for TA's"""
    def __init__(self, TA_number, view_available_rooms, book_room, schedule, titel, firstname,
                 surname, cpr_number, sex, address, phone_nr, mail):

        self.book_room = book_room
        self.view_available_rooms = view_available_rooms
        self.schedule = schedule
        self.TA_number = TA_number
        self.titel = titel
        self.firstname = firstname
        self.surname = surname
        self.cpr_number = cpr_number
        self.sex = sex
        self.address = address
        self.phone_nr = phone_nr
        self.mail = mail

        # getters og setters

    def get_titel(self): return self.titel
    def set_titel(self, new_titel): self.titel = new_titel

    def get_firstname(self): return self.firstname
    def set_firstname(self, new_firstname): self.firstname = new_firstname

    def get_surname(self): return self.surname
    def set_surname(self, new_surname): self.surname = new_surname

    def get_cpr_number(self): return self.cpr_number
    def set_cpr_number(self, new_cpr_number): self.cpr_number = new_cpr_number

    def get_sex(self): return self.sex
    def set_sex(self, new_sex): self.sex = new_sex

    def get_address(self): return self.address
    def set_address(self, new_address): self.address = new_address

    def get_phone_nr(self): return self.phone_nr
    def set_phone_nr(self, new_phone_nr): self.phone_nr = new_phone_nr

    def get_mail(self): return self.mail
    def set_mail(self, new_mail): self.mail = new_mail

    def get_book_room(self): return self.book_room
    def set_book_room(self, new_book_room): self.book_room = new_book_room

    def get_view_available_rooms(self): return self.view_available_rooms
    def set_view_available_rooms(self, new_view_available_rooms): self.view_available_rooms = new_view_available_rooms

    def get_schedule(self): return self.schedule
    def set_schedule(self, new_schedule): self.schedule = new_schedule

    def get_TA_number(self): return self.TA_number
    def set_TA_number(self, new_TA_number): self.TA_number = new_TA_number

    def __str__(self):
        name = f"{self.firstname} {self.surname}"
        # Address = f"{self.address}"           denne har vi ikke skulle gruppere, hvorfor den er udkommenteret
        general_information = f"{self.sex}, {self.phone_nr}, {self.mail}, {self.TA_number}"
        functionalities = f"{self.book_room}, {self.view_available_rooms}, {self.schedule}"

        return f"Name: {name}, Address: {self.address}, CPR-nr: {self.cpr_number}, " \
               f"Information: {general_information}, Functionality: {functionalities}"