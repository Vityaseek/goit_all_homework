class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id[:2] == "01":
        id_list.append(employee_id)
    else:
        raise IDException
    return id_list


print(add_id([], '0256456464'))
