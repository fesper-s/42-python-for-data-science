def NULL_not_found(object: any) -> int:
    object_type = type(object)
    output = ''

    if object == None:
        output = "Nothing"
    elif object_type == float:
        output = "Cheese"
    elif object_type == int:
        output = "Zero"
    elif object == '' and object_type == str:
        output = "Empty"
    elif object_type == bool:
        output = "Fake"
    else:
        print("Type not Found")
        return 1

    print(f"{output}: {object} {object_type}")

    return 0
