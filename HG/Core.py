class SerialData: # ["UDP:192.168.1.1:80:JOHNISGREAT"]
    def __init__(self, data : str):
        self.data = data

class Connection:
    def __init__(self, responder : str):
        self.responder = responder