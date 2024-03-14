class Instructor:
    followers = 0
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject_name):
        print(f"Hi Iam{self.name} and I will teach{subject_name}")

    def update_followers(self,followers_name):
        self.followers+=1
Instructor_1=Instructor("rohith","Kerala")
print(Instructor_1.name)

