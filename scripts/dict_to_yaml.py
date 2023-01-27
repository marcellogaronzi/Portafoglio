import yaml

def dict_to_yaml(dictionary, filename):
    with open(filename, 'w') as outfile:
        yaml.dump(dictionary, outfile)