import json

FILE_NAME: str = 'my_data.json'
MENU = """
---- Student GPAs ----
   Select from the following menu:
    1. Show current data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
"""

student_table: list = []

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter 
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")
        
    @property
    def last_name(self):
        return self.__last_name.title()

    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
        
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

class Student(Person):
    def __init__(self, first_name: str, last_name: str, gpa: float):
        super().__init__(first_name=first_name, last_name=last_name)
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        try:
            self.__gpa = float(value)
        except ValueError:
            raise ValueError("GPA must be a numeric value.")
        
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.gpa}"

class FileProcessor:

    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_dictionary_data: list = []
            for student in student_data:
                student_json: dict = {"FirstName": student.first_name, "LastName": student.last_name, "GPA": student.gpa}
                list_of_dictionary_data.append(student_json)
            
            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError as error_details:
            IO.output_error_messages("Please check that the data is a valid JSON format", error_details)
        except Exception as error_details:
            IO.output_error_messages("There was a non-specific error!", error_details)
        finally:
            if file.closed == False:
                file.close()

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("-- Exception details --")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def input_data_to_table(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            gpa = input("Enter the student's gpa: ")

            new_student = Student(student_first_name, student_last_name, gpa)

            student_data.append(new_student)
        except ValueError as error_details:
            IO.output_error_messages("Only use names without numbers", error_details)
        except Exception as error_details:
            IO.output_error_messages("There was a non-specific error when adding data", error_details)

        return student_data

if __name__ == "__main__":
    while True:
        student_table = IO.input_data_to_table(student_data=student_table)
        for student in student_table:
            print(student.first_name, student.last_name, student)
        if input("Add another? (y/n)".lower()) != 'y':
            break

    if input("Do you want to save the data? (y/n)".lower()) == 'y':
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)
