class BinaryColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def __init__(self, className):
        self._className = className

    def log(self, identifiers, msg, error=False):
        logMsg = BinaryColors.FAIL if error else BinaryColors.OKCYAN

        logMsg += "[" + self._className + " | "

        for identifier in identifiers:
            logMsg += str(identifier)
        
        logMsg += "] " + msg

        print(logMsg) 


