from Personer import Personer

class Studerende(Personer):
    """Klasse for studerende"""
    def __init__(self):
        self.study_nr = study_nr
        self.semester_nr = semester_nr
        self.education_name = education_name
        self.schedule = schedule
        self.location_for_lessons = location_for_lessons
        self.unsubscribe_from_courses = unsubscribe_from_courses
        self.signup_for_courses = signup_for_courses

        #getters og getters
    def get_study_nr(self): return self.study_nr
    def set_study_nr(self, new_study_nr): self.study_nr = new_study_nr

    def get_semester_nr(self): return self.semester_nr
    def set_semester_nr(self, new_semester_nr): self.semester_nr = new_semester_nr     
        
    def get_education_name(self): return self.education_name
    def set_education_name(self, new_education_name): self.education_name = new_education_name
        
    def get_schedule(self): return self.schedule
    def set_schedule(self, new_schedule): self.schedule = new_schedule
    
    def get_location_for_lessons(self): return self.location_for_lessons
    def set_location_for_lessons(self, new_location_for_lessons): self.location_for_lessons = new_location_for_lessons

    def get_unsubscribe_from_courses(self): return self.unsubscribe_from_courses
    def set_unsubscribe_from_courses(self, new_unsubscribe_from_courses): self.unsubscribe_from_courses = new_unsubscribe_from_courses
                
    def get_signup_for_courses(self): return self.signup_for_courses
    def set_signup_for_courses(self, new_signup_for_courses): self.signup_for_courses = new_signup_for_courses



   
    def __str__(self):
        name = f"{self.firstname} {self.surname}"
        # Address = f"{self.address}"           denne har vi ikke skulle gruppere, hvorfor den er udkommenteret
        general_information = f"{self.sex}, {self.phone_nr}, {self.mail}, {self.study_nr}, {self.semester_nr}, {self.education_name}"
        functionalities = f"{self.signup_for_courses}, {self.schedule}, {self.unsubscribe_from_courses}, {self.location_for_lessons}"

        return f"Name: {name}, Address: {self.address}, CPR-nr: {self.cpr_number}, " \
               f"Information: {general_information}, Functionality: {functionalities}"


