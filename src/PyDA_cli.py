import json

# Loads a dfa from a given json formatted file
#
# If the file loads and parses correctly, the pyda json structure is returned. 
# If there was an error loading or parsing the file, None is returned.
def load_dfa(filename):
    try:
        json_data = open(filename)
        pyda_struct = json.load(json_data)
        json_data.close()
    except Exception:
        return None

    return pyda_struct
