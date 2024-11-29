class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", 
        "Production", "Legal", "Finance", "Sales", 
        "General Management", "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Admin"):
        self.name = name  # Calls the name setter
        self.job = job  # Calls the job setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Save name in title case
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value  # Save the job if valid
        else:
            print("Job must be in list of approved jobs.")
