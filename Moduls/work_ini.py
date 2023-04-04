import configparser

config = configparser.ConfigParser()
config.read(r"\LR BD new\Settings\default_settigs.ini")

def get_db_link():
    return config["db"]["db_link"]

def get_backup_data():
    return config["db"]["date_backup"]

def get_db_link():
    return config["db"]["db_link"]

def get_backup_folder():
    return config["db"]["backup_db"]

def get_pass_email_from():
    return config["posts"]["send_pass"]

def get_email_from():
    return config["posts"]["send_email"]

def get_email_to():
    return config["posts"]["to_email"]      
    