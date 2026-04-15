import logging

class Log_generation:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log", format='%(asctime)s: %(levelname)s', datefmt='%m%d%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)
        logger.setLevel(logging.DEBUG)
        return logger 