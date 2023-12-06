from lab7.commands import CREATE, READ, UPDATE, DELETE

create = CREATE()
read = READ()
update = UPDATE()
delete = DELETE()


def resident():
    name = input("Input name: ")
    how_long = input("Input how long live/y: ")
    email = input("Input email: ")
    phone = input("Input phone: ")
    number = input("Input apartment number: ")
    return {
      "name": f"{name}",
      "how_long_live/y": how_long,
      "contacts": {
        "email": f"{email}",
        "phone": f"{phone}"
      },
      "apartment_number": number
    }


def apartment():
    square = input("Input square: ")
    floor = input("Input floor: ")
    entrance = input("Input entrance: ")
    return {
      "square": {square},
      "position": {
        "floor": f"{floor}",
        "entrance": f"{entrance}"
      }
    }


def employees():
    name = input("Input name: ")
    job = input("Input job: ")
    phone = input("Input phone: ")
    email = input("Input email: ")
    return {
          "name": f"{name}",
          "job": f"{job}",
          "contacts": {
            "phone": f"{phone}",
            "email": f"{email}"
          }
        }


while True:
    try:
        command = input("Input command: create, read, update or delete ").lower()
        who = input("Input for whom: r (for resident), e (for employees) or a (for apartments) ").lower()
        action = input("Input action (id or nothing): ").lower()
        if command not in ["create", "read", "update", "delete"]:
            print("Unknown command")
        else:
            match command:
                case "create":
                    match who:
                        case "r":
                            create.create_one_resident(resident())
                        case "e":
                            create.create_one_employees(employees())
                        case "a":
                            create.create_one_apartments(apartment())
                        case _:
                            print("Error")
                case "read":
                    if action == "all" or action == "":
                        match who:
                            case "r":
                                print(read.get_all_residents())
                            case "e":
                                print(read.get_all_employees())
                            case "a":
                                print(read.get_all_apartments())
                            case _:
                                print("Error")
                    else:
                        match who:
                            case "r":
                                print(read.get_by_id_residents(int(action)))
                            case "e":
                                print(read.get_by_id_employees(int(action)))
                            case "a":
                                print(read.get_by_id_apartments(int(action)))
                            case _:
                                print("Error")
                case "update":
                    match who:
                        case "r":
                            print(update.update_by_id_residents(int(action), resident()))
                        case "e":
                            print(update.update_by_id_employees(int(action), employees()))
                        case "a":
                            print(update.update_by_id_apartments(int(action), apartment()))
                        case _:
                            print("Error")
                case "delete":
                    match who:
                        case "r":
                            print(delete.delete_by_id_residents(int(action)))
                        case "e":
                            print(delete.delete_by_id_employees(int(action)))
                        case "a":
                            print(delete.delete_by_id_apartments(int(action)))
                        case _:
                            print("Error")
    except BaseException as e:
        print(f"Error: {e}")