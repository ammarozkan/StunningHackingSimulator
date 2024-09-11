

import Gadgets, Programs, Core


modem = Gadgets.SD()

home = Gadgets.Computer()
home.programs["main"] = Gadgets.Program(Programs.ShellCore("/","main"), 5)
home.programs["john"] = Gadgets.Program(Programs.InterConnector("/","john"), 5)
home.programs["killer"] = Gadgets.Program(Programs.InterSender("/","killer"), 5)
home.programs["nmap"] = Gadgets.Program(Programs.NetworkMapper("/","nmap"), 5)

google = Gadgets.Computer()
google.programs["main"] = Gadgets.Program(Programs.ShellCore("/","main"), 5)
google.programs["john"] = Gadgets.Program(Programs.InterConnector("/","john"), 5)
google.programs["ponger"] = Gadgets.Program(Programs.PingProgram("/","ponger"), 5)
google.programs["john"].execute(google, "1", "ponger")

modem.addSerialObject("192.168.1.2", home)
modem.addSerialObject("192.168.1.5", google)
home.setModem(modem)
google.setModem(modem)
while True:
    home.programs["main"].execute(home,"home")
    #google.programs["main"].execute(google,"google")
    home.parallelExecute()
    google.parallelExecute()
