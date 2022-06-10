# create function that filter given data by string or number
# with string filter it needs at least 3 characters to filter values
# with int or float filter it needs at least single digit nmber


data = [
{
    "_id": "5e985a07feddae7617ac44f6",
    "age": 24,
    "eyeColor": "brown",
    "name": "Cummings Baxter",
    "gender": "male",
    "company": "VELOS",
    "email": "cummingsbaxter@velos.com",
    "phone": "+1 (907) 482-2451",
    "tags": [
    "labore",
    "elit",
    "excepteur",
    "nisi",
    "mollit",
    "anim",
    "aliquip"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Sheppard Jensen"
    }
    ]
},
{
    "_id": "5e985a0709dfa1e6fd93c6ad",
    "age": 32,
    "eyeColor": "brown",
    "name": "Madelyn Dickson",
    "gender": "female",
    "company": "KENGEN",
    "email": "madelyndickson@kengen.com",
    "phone": "+1 (984) 521-2439",
    "tags": [
    "nisi",
    "veniam",
    "dolore",
    "officia",
    "ex",
    "non",
    "pariatur"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Bruce Barton"
    },
    {
        "id": 1,
        "name": "Juliet Schmidt"
    },
    {
        "id": 2,
        "name": "Horton Haley"
    },
    {
        "id": 3,
        "name": "Herminia Witt"
    }
    ]
},
{
    "_id": "5e985a0737e2306e9aef6ecd",
    "age": 26,
    "eyeColor": "blue",
    "name": "Mcguire Mercado",
    "gender": "male",
    "company": "LINGOAGE",
    "email": "mcguiremercado@lingoage.com",
    "phone": "+1 (963) 450-2194",
    "tags": [
    "cupidatat",
    "occaecat",
    "amet",
    "qui",
    "elit",
    "esse",
    "deserunt"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Loraine Harper"
    },
    {
        "id": 1,
        "name": "Luann Randall"
    },
    {
        "id": 2,
        "name": "Obrien Rich"
    },
    {
        "id": 3,
        "name": "Noble Wilkerson"
    }
    ]
},
{
    "_id": "5e985a07148cfba58c860ec2",
    "age": 26,
    "eyeColor": "brown",
    "name": "Marina Porter",
    "gender": "female",
    "company": "GORGANIC",
    "email": "marinaporter@gorganic.com",
    "phone": "+1 (867) 417-3497",
    "tags": [
    "laborum",
    "aliquip",
    "sit",
    "adipisicing",
    "aute",
    "cupidatat",
    "aliquip"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Blair Hill"
    },
    {
        "id": 1,
        "name": "Ebony Jimenez"
    }
    ]
},
{
    "_id": "5e985a074984f9f08ccaaa4c",
    "age": 25,
    "eyeColor": "green",
    "name": "Barlow Ferguson",
    "gender": "male",
    "company": "TOYLETRY",
    "email": "barlowferguson@toyletry.com",
    "phone": "+1 (837) 484-2231",
    "tags": [
    "est",
    "dolor",
    "minim",
    "ut",
    "anim",
    "culpa",
    "non"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Delacruz Acevedo"
    },
    {
        "id": 1,
        "name": "Gloria Tanner"
    },
    {
        "id": 2,
        "name": "Cantrell Myers"
    },
    {
        "id": 3,
        "name": "Fisher Leonard"
    }
    ]
}
]


def filter_dict(list_, search_item):
    if isinstance(search_item, str) and len(search_item) >= 3:
        filt_dict_with_str = dict(filter(lambda item: search_item.lower() in str(item[1]).lower(), list_.items()))
        return filt_dict_with_str
    elif isinstance(search_item, (int, float)):
        filt_dict_with_num = dict(filter(lambda item: item == search_item , list_.values()))
        return filt_dict_with_num

def filter_list(list_, search_item):
    result_all = []
    for item in list_:
        result = filter_dict(item, search_item)
        if result:
            result_all.append(result)
    return result_all


print(filter_list(data, "Fer"))
print(filter_list(data, "min"))
print(filter_list(data, 32))
