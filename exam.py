class Exam:
    def __init__(self, subject, time, hall):
        self.subject = subject
        self.time = time
        self.hall = hall

    def get_details(self):
        return f"Subject: {self.subject}, Time: {self.time}, Hall: {self.hall.hall_name}"
