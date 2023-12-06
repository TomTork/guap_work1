import mUtils.json_service as json_service


class CREATE:
    def __init__(self):
        self.read = READ()

    def create_one_resident(self, complex):
        db = json_service.get_database()
        last_resident_id = self.read.get_all_residents()[-1]["id"]
        db["residents"].append({"id": last_resident_id + 1, **complex})
        json_service.set_database(db)

    def create_one_apartments(self, complex):
        db = json_service.get_database()
        last_apartment_id = self.read.get_all_apartments()[-1]["id"]
        db["apartments"].append({"id": last_apartment_id + 1, **complex})
        json_service.set_database(db)

    def create_one_employees(self, complex):
        db = json_service.get_database()
        last_employees_id = self.read.get_all_employees()[-1]["id"]
        db["employees"].append({"id": last_employees_id + 1, **complex})
        json_service.set_database(db)


class READ:
    def get_all_residents(self):
        db = json_service.get_database()
        return db["residents"]

    def get_all_apartments(self):
        db = json_service.get_database()
        return db["apartments"]

    def get_all_employees(self):
        db = json_service.get_database()
        return db["employees"]

    def get_by_id_residents(self, id):
        db = json_service.get_database()
        for elem in db["residents"]:
            if elem["id"] == id:
                return elem
        return {"message": f"Элемент с {id} не найден"}

    def get_by_id_apartments(self, id):
        db = json_service.get_database()
        for elem in db["apartments"]:
            if elem["id"] == id:
                return elem
        return {"message": f"Элемент с {id} не найден"}

    def get_by_id_employees(self, id):
        db = json_service.get_database()
        for elem in db["employees"]:
            if elem["id"] == id:
                return elem
        return {"message": f"Элемент с {id} не найден"}


class UPDATE:
    def update_by_id_residents(self, id, complex):
        db = json_service.get_database()
        for i, elem in enumerate(db["residents"]):
            if elem["id"] == id:
                elem["name"] = complex["name"]
                elem["contacts"] = complex["contacts"]
                elem["how_long_live/y"] = complex["how_long_live/y"]
                elem["apartment_number"] = complex["apartment_number"]
                json_service.set_database(db)
                return elem
        return {"message": f"Элемент с {id} не найден"}

    def update_by_id_apartments(self, id, complex):
        db = json_service.get_database()
        for i, elem in enumerate(db["apartments"]):
            if elem["id"] == id:
                elem["square"] = complex["square"]
                elem["position"] = complex["position"]
                json_service.set_database(db)
                return elem
        return {"message": f"Элемент с {id} не найден"}

    def update_by_id_employees(self, id, complex):
        db = json_service.get_database()
        for i, elem in enumerate(db["employees"]):
            if elem["id"] == id:
                elem["name"] = complex["name"]
                elem["job"] = complex["job"]
                elem["contacts"] = complex["contacts"]
                json_service.set_database(db)
                return elem
        return {"message": f"Элемент с {id} не найден"}


class DELETE:
    def delete_by_id_residents(self, id):
        db = json_service.get_database()
        for i, elem in enumerate(db["residents"]):
            if elem["id"] == id:
                candidate = db["residents"].pop(i)
                json_service.set_database(db)
                return candidate
        return {"message": f"Элемент с {id} не найден"}

    def delete_by_id_apartments(self, id):
        db = json_service.get_database()
        for i, elem in enumerate(db["apartments"]):
            if elem["id"] == id:
                candidate = db["apartments"].pop(i)
                json_service.set_database(db)
                return candidate
        return {"message": f"Элемент с {id} не найден"}

    def delete_by_id_employees(self, id):
        db = json_service.get_database()
        for i, elem in enumerate(db["employees"]):
            if elem["id"] == id:
                candidate = db["employees"].pop(i)
                json_service.set_database(db)
                return candidate
        return {"message": f"Элемент с {id} не найден"}

