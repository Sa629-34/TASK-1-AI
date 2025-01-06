class Student:
    def init(self, name, age, grades):  # Corrected __init method
        """
        Initialize a Student object with name, age, and grades.
        :param name: str - Student's name
        :param age: int - Student's age
        :param grades: list - List of grades
        """
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        """
        Display the details of the student.ss
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        """
        Calculate and return the average of the grades.
        :return: float - Average grade
        """
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0  # Return 0.0 if there are no grades


def main():
    # Create instances of the Student class
    student1 = Student("Alice", 20, [85, 90, 88])
    student2 = Student("Bob", 22, [78, 80, 82])

    # Display details of each student
    print("Details of Student 1:")
    student1.display_details()
    print(f"Average Grade: {student1.calculate_average():.2f}")

    print("\nDetails of Student 2:")
    student2.display_details()
    print(f"Average Grade: {student2.calculate_average():.2f}")


if _name_ == "main":
    main()
