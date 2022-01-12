
def bill_data():
    data = {"age": 29, "favourite colour" : "blue"}
    return data


def viola_data():
    data = {"age": 29, "favourite colour" : "blue"}
    return data


def rizzy_data():
    data = {"age": 29, "favourite colour" : "blue"}
    return data


def assemble():
    return {
        "bill": bill_data(),
        "viola" : viola_data(),
        "rizzy" : rizzy_data()
    }


def display():
    test = assemble()
    for i in test:
        print(i)
    for key, value in assemble().items():
        print(f"{key}:{value}")

