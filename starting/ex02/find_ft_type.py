def all_thing_is_obj(object: any) -> int:
    object_type = type(object)

    if object_type == list:
        print(f"List : {object_type}")
    elif object_type == tuple:
        print(f"Tuple : {object_type}")
    elif object_type == set:
        print(f"Set : {object_type}")
    elif object_type == dict:
        print(f"Dict : {object_type}")
    elif object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type not found")

    return 42
