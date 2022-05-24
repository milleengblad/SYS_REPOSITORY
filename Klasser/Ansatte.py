from datetime import date
from stdnum.dk import cpr
from Personer import Personer

class Ansatte(Personer):
    """Klasse for ansatte"""
    def __init__(self, employee_number, date_of_employment, education_name, language, salary):
        self.employee_number = employee_number
        self.date_of_employment = date_of_employment
        self.education_name = education_name
        self.language = language
        self.salary = salary

        #getters og setters

    def get_employee_number(self): return self.employee_number
    def set_employee_number(self, new_employee_number): self.employee_number = new_employee_number

    def get_date_of_employment(self): return self.date_of_employment
    def set_date_of_employment(self, new_date_of_employment): self.date_of_employment = new_date_of_employment
    def get_education_name(self): return self.education_name
    def set_education_name(self, new_education_name): self.education_name = new_education_name
    def get_language(self): return self.language
    def set_language(self, new_language): self.language = new_language
    def get_salary(self): return self.salary
    def set_salary(self, new_salary): self.salary = new_salary

    def __str__(self):
        Information_ansat = f"{self.employee_number},{self.date_of_employment},{self.education_name},{self.language},{self.salary}"
        return f"Information_ansatte {Information_ansat}"

   #  def __str__(self):
   #     result=super(Ansatte,self).__str__() + f",employee_number: {self.employee_number}" + f",date_of_employment: {self.date_of_employment}" + f",education_name: {self.education_name}" + f",language: {self.language}" + f"f,salary: {self.salary}"
   #     return result