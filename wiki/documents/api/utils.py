import json

def is_json(data):
    try:
      real_json=json.loads(data)
      is_valid=True
    except ValueError:
      is_valid=False
    return is_valid
