import json 

def main(config):
    # everything in the main function will be executed
    # it is totally isolated!
    # now it is just a simple print statement, but it is a reflection of complex production scripts.
    print(config['message'])

def read_config(config_path):
    # we will use this function to define the configuration.json file
    with open(config_path, "r") as f:
        retval = json.load(f)
        return retval

if __name__ == "__main__":
    # let's read our config, and execute the main function based on our config!
    config = read_config("hello_new_config.json")
    main(config)