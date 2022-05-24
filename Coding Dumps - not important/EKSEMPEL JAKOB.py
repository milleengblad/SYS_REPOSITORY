from Employee import Employee


class AdminPersonal(Employee):
    """
    Represents an employee at an educational institution
    AdminPersonal will have a set of course request to process, and can accept a course request or deny it

    """
    def __init__(self, institute_id, course_requests: list,
                 first_name: str, last_name: str, cpr_number: str, phone: str, email: str):
        super().__init__(first_name,last_name,cpr_number,phone,email)
        self.__instituteID = institute_id
        self.__course_requests = course_requests


    def __str__(self):
        # returnér parents str form og tilføj denne klasses attributter
        result=super(AdminPersonal,self).__str__() + f", institute: {self.__instituteID}" + f", kurser: {self.__course_requests}"
        return result