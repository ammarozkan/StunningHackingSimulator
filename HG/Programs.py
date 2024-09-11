import Gadgets

class ShellCore(Gadgets.Program):
    def __init__(self, work_dir, name):
        self.work_dir = work_dir
        self.name = name
        self.interdatas = []

    def execute_program(self, programname, system : Gadgets.Computer, *inp):
        system.requestProgramRun(self.name, programname, *inp)

    def execute(self, system, *inp):
        if inp[0] == "datas":
            result = "upcame connected datas:\n"
            for interdata in self.interdatas:
                result += f"\t{interdata}\n"
            system.requestStdOut(self.name, result)
            return

        com = system.requestStdIn(self.name, self.work_dir+"#"+inp[0]+":")
        com = com.split(" ")
        self.execute_program(com[0], system, *(com[1:]))
        print(inp[0],":",system.stdout())

    def parallelExecute(self, system, *inp):
        pass

class InterConnector(Gadgets.Program):
    def __init__(self, work_dir, name):
        self.work_dir = work_dir
        self.name = name
        self.interdatas = []

    def connect(self, system, port, programname):
        return system.requestConnectProgram(self.name, port, programname)

    def execute(self, system, *com):
        if com[0] == "--help":
            system.requestStdOut(self.name, "[programname] port program")
        if len(com) < 2: return
        
        if self.connect(system, com[0], com[1]) == 0:
            system.requestStdOut(self.name, "Connection succesful.")

    def parallelExecute(self, system, *inp):
        pass

class InterSender(Gadgets.Program):
    def __init__(self, work_dir, name):
        self.work_dir = work_dir
        self.name = name
        self.interdatas = []

    def execute(self, system, *com):
        address = system.requestStdIn(self.name, "address:")
        port = system.requestStdIn(self.name, "port:")
        message = system.requestStdIn(self.name, "message:")
        system.requestModemOutput(self.name, f"INTERNET:{address}:{port}:{message}")

    def parallelExecute(self, system, *inp):
        pass

class PingProgram(Gadgets.Program):
    def __init__(self, work_dir, name):
        self.work_dir = work_dir
        self.name = name
        self.interdatas = []

    def execute(self, system, *com):
        pass

    def parallelExecute(self, system, *inp):
        if len(self.interdatas) == 0: return

        for interdata in self.interdatas:
            sper = interdata.split(":")
            data = f"INTERNET:{sper[3]}:{sper[2]}:{sper[1]}"
            system.requestModemOutput(self.name, data)
        self.interdatas = []

class NetworkMapper(Gadgets.Program):
    def __init__(self, work_dir, name):
        self.work_dir = work_dir
        self.name = name
        self.interdatas = []

    def execute(self, system, *com):
        if len(com) == 0:
            system.requestStdOut(self.name, "[programname] ping to all over the place")
            return
        if len(com) == 2:
            if com[0] == "ping":
                for i in range(0,255):
                    data = f"INTERNET:192.168.1.{i}:1:{com[1]}"
                    r = system.requestModemOutput(self.name, data)
                    if r == 0:
                        system.requestStdOut(self.name, f"sending ping pkg to 192.168.1.{i}")

    def parallelExecute(self, system, *inp):
        pass
