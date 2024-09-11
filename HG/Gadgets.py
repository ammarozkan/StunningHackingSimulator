import Core

# COMPUTER

class File:
    def __init__(self, data, perm):
        self.data = data
        self.perm = perm
    def see(self, perm):
        if self.perm > perm: return None
        else: return self.data

class Program:
    def __init__(self, programCore, perm):
        self.programCore = programCore
        self.perm = perm
        pass
    def execute(self, system, *inp):
        self.programCore.execute(system, *inp)

    def parallelExecute(self, system, *inp):
        self.programCore.parallelExecute(system, *inp)

class Computer:
    def __init__(self):
        self.connections = dict()
        self.programs = dict()
        self.files = dict()
        self._stdin = ""
        self._stdout = ""
        self.stdinperm = 0
        self.stdoutperm = 0
        self.modemoutperm = 0
        self.connectorperm = 0
        self.modem = None

    def setModem(self, modem):
        self.modem = modem

    def addPortConnection(self, port, programname):
        self.connections[port] = programname

    def nonRootFileExplorer(path):
        if path in self.files:
            pass
        pass

    def stdout(self):
        result = self._stdout
        self._stdout = ""
        return result

    def serialData(self, data : Core.SerialData):
        if data.data.split(":")[0] == "INTERNET":
            if data.data.split(":")[2] in self.connections:
                self.programs[self.connections[data.data.split(":")[2]]].programCore.interdatas+=[data.data]
            else:
                port = data.data.split(":")[2]
                self._stdout += f"an serial internet data came to a non-connected port({port}).\n"

    def requestStdIn(self, requester, st):
        if self.programs[requester].perm < self.stdinperm:
            self._stdout += "Doesnt have the perm to get std input.\n"
            return
        return input(st)

    def requestStdOut(self, requester, st):
        if self.programs[requester].perm < self.stdoutperm:
            self._stdout += "Doesnt have the perm to get std output.\n"
            return
        self._stdout += st+"\n"


    def requestProgramRun(self, requester, programname, *inp):
        if programname not in self.programs:
            self._stdout += programname + " is not a program.\n"
            return
        if self.programs[programname].perm > self.programs[requester].perm: return
        self.programs[programname].execute(self, *inp)

    def requestConnectProgram(self, requester, port, programname):
        if self.programs[requester].perm < self.connectorperm: 
            self._stdout += "Doesnt have the perm to connect.\n"
            return -1
        self.addPortConnection(port, programname)
        return 0

    def requestModemOutput(self, requester, data : str):
        if self.programs[requester].perm < self.modemoutperm:
            self._stdout += "Doesnt have the perm to modem out.\n"
            return -1
        if self.modem != None:
            self.modem.serialData(Core.SerialData(data))
            return 0
        return -2

    def parallelExecute(self):
        for p in self.programs:
            self.programs[p].parallelExecute(self)


# SERIAL DISTRUBUTER


class SD:
    def __init__(self):
        self.objects = dict()

    def addSerialObject(self, address, gadget):
        self.objects[address] = gadget

    def serialData(self, data : Core.SerialData):
        infos = data.data.split(":")
        if infos[0] == "INTERNET":
            self.serialInternetData(data)

    def serialInternetData(self, data : Core.SerialData): #["INTERNET:192.168.1.1:80:MESSAGE"]
        infos = data.data.split(":")
        if infos[1] in self.objects:
            self.objects[infos[1]].serialData(data)
