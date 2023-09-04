# define class Patient
class Patient:
    # patient constructor
    def __init__(self, patientId, name, age, phoneNumber, positiveForCOVID):
        self.patientId = patientId
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber
        self.positiveForCOVID = positiveForCOVID

    # overloading repr method for printing
    def __repr__(self):
        return f"Patient ID: {self.patientId}\n" \
               f"Patient Name: {self.name}\n" \
               f"Patient Age: {self.age}\n" \
               f"Patient Phone Number: {self.phoneNumber}\n" \
               f"Positive for COVID: {self.positiveForCOVID}\n"

# define main function
def main():
    # create Patient objects
    patient1 = Patient(1, "Clancy Wiggum", 43, "315-292-9445", True)
    patient2 = Patient(2, "Ralph Wiggum", 8, "315-332-9631", False)
    patient3 = Patient(3, "Sarah Wiggum", 39, "315-996-4912", False)

    # display patient information for patients 1-3
    print("Patient 1:")
    print(patient1)

    print("Patient 2:")
    print(patient2)

    print("Patient 3:")
    print(patient3)

# call main function
main()