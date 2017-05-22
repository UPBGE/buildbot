from print import *
from sh import ErrorReturnCode, scp, Command

ip = "upbge.org"
port = "22"

password = "gerbille73"

def sendFile(file, dest):
	msgcmd("Sending file {} to upbge.org".format(file))
	try:
		cmd = Command("sshpass")
		#sshpass("-p", password, "scp", "-P", port, file, "git@" + ip + ":" + dest, _out=debugSh)
		scp("-P", port, file, "git@" + ip + ":" + dest, _out=debugSh)
	except ErrorReturnCode as e:
		msgerr("Failed send file {} to upbge.org".format(file))
		print(e.stderr)
		return False
	else:
		msgstat("Success send file {} to upbge.org".format(file))
		return True

def sendCommands(command):
	msgcmd("Send commands to upbge.org")
	try:
		cmd = Command("ssh -p " + port  + " git@" + ip + "\"" + command + "\"")
		cmd.run()
	except ErrorReturnCode:
		msgerr("Failed send commands to upbge.org")
		return False
	else:
		msgstat("Success send commands to upbge.org")
		return True
