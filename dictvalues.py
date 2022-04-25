# get budget from a provided list of dict values
#  method one

def get_budget(lst):
    return sum([x['budget'] for x in lst if 'budget' in x])


get_budget([{"name": "John",  "age": 21, "budget": 10234}, {"name": "Steve",  "age": 32, "budget": 21754}, {"name": "Martin",  "age": 16, "budget": 4935}])