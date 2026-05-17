# Merge 2 dictionaries

# Way 1 : using Union Operator |

def merge_dict_1(d1, d2):
    merged = d1 | d2
    return merged

# Way 2 : using unpacking **

def merged_dict_2(d1, d2):
    merged = {**d1, **d2}
    return merged

# Way 3 : using update (no new dictionary)

def merged_dict_3(d1, d2):
    d1.update(d2)
    return d1

user_dict1 = {
    "username": "coder_99",
    "age": 28,
    "email": "alex@email.com",
    "skills": ["Python", "SQL", "Git"],
    "is_active": True
}

user_dict2 = {
    "prod_101": {
        "name": "Wireless Mouse",
        "price": 29.99,
        "stock": 45
    },
    "prod_102": {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "stock": 12
    }
}

print("Way 1 : ", merge_dict_1(user_dict1, user_dict2))
print("\n\nWay 2 : ", merged_dict_2(user_dict1, user_dict2))
print("\n\nWay 3 : ", merged_dict_3(user_dict1, user_dict2))
