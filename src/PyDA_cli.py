import json

# Loads a dfa from a given json formatted file
def load_dfa(filename):
    json_data = open(filename)
    pyda_struct = json.load(json_data)
    json_data.close()
    return pyda_struct
