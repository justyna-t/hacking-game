import os.path
import pickle


def check_file(file_name, data):
    # Check whether a file exist and if so load it, if not save the file with
    # given data and return data from this file
    # - file_name is string containing the file name to load or save
    # - data to be saved in the file
    if os.path.isfile(file_name):
        data = load_file(file_name)
    else:
        data = save_file(file_name, data)
    return data


def load_file(file_name):
    # Load a file and return data from it
    # - file_name is string containing the file name to load
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
        f.close()
        return data


def save_file(file_name, data):
    # Save a file and return data from it
    # - file_name is string containing the file name to save
    # - data to be saved in the file
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
        f.close()
        return data
