from utils.constante import FILE_ADMIN
import json

class Administrator:
    def __init__(self, id, name, surname):
        self.id = id
        self.name= name
        self.surname = surname


    def __str__(self):
        return f"ID : {self.id}, Nom : {self.surname}, Prenom : {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "surname": self.surname,
            "name": self.name
        }

    def save(self):
        admin_list = self.load_json()
        admin_list.append(self)
        admins_data = [admin.to_dict() for admin in admin_list]
        with open(FILE_ADMIN, "w") as file:
            json.dump(admins_data, file, indent=4)

    @staticmethod
    def load_json():
        with open(FILE_ADMIN, "r") as file:
            admins_data = json.load(file)
            admin_list = []
            for admin_data in admins_data:
                admin = Administrator(
                    admin_data["id"],
                    admin_data["surname"],
                    admin_data["name"])
                admin_list.append(admin)
            return admin_list



admin = Administrator(2312, "Jonas", "Carter")
#admin.save()