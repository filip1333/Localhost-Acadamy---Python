# Create function that returns all given parameters in dict:
# {
#   key:value
# }
# if parameter is unnamed, it's index is key
#               

def arguments(*args, **kwargs):
    f = {index:a for index, a in enumerate(args)}
    f.update(kwargs)
    return f

def func(*args, **kwargs):
    temp_dict = { i:e for i, e in enumerate(args)}
    for k, e in temp_dict.items():
        kwargs[k] = e
    
    return kwargs

print(arguments('Norwish', 'count', en=1, to=2, tolv='', tre=3, tretten=None))
# {'Norwish': None, 'count': None, 'en': 1, 'to': 2, 'tolv': '', 'tre': 3, 'tretten': None}
