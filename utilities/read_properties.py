import configparser

config= configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def get_application_url():
        url = config.get('common info','base_url')
        return url

    @staticmethod
    def get_application_useremail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def get_application_password():
        password = config.get('common info','password')
        return password


    

