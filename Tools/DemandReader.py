import json

def read_demand(file_path="Data/Demand.json"):

    with open(file_path, "r") as f:
        demand = json.load(f)
    return demand