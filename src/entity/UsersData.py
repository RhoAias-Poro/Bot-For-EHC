class Users:

    def __init__(self):
        self.Login = None
        self.port = None
        self.portNumber = None

    def setLogin(self, Login):
        self.Login = Login

    def setPort(self, port):
        self.port = port

    def setPortNumber(self, portNumber):
        self.portNumber = portNumber

    def getLogin(self):
        return self.Login

    def getPort(self):
        return self.port

    def getPortNumber(self):
        return self.portNumber
