import socket
import sys
import time

server = "irc.freenode.net"
channel = "#upbgecoders"
botnick = "upbgebuildbot"

class IrcClient():
	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Connecting to: " + server)

		self.irc.connect((server, 6667)) #connects to the server
		self.send("USER " + botnick + " " + botnick + " " + botnick + " : \n") #user authentication
		self.send("NICK " + botnick + "\n") #sets nick
		self.send("PRIVMSG nickserv :iNOOPE\r\n") #auth
		self.send("JOIN " + channel + "\n") #join the chan

		endtime = time.time() + 10.0
		while endtime > time.time(): # puts it in a loop
			data = self.irc.recv(2040) # receive the text
			text = data.decode("utf-8")
			#print(text)
			if text.find("NOTICE upbgebuildbot :") != -1: #check if 'PING' is found
				self.send("PONG " + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
				print("=" * 10, "PONG", "=" * 10)
				break

	def send(self, msg):
		self.irc.send(str.encode(msg))

	def sendMsg(self, msg):
		self.send("PRIVMSG " + channel + " :" + msg + "\n")

	def sendError(self, msg):
		self.sendMsg("4" + msg + "")

if __name__ == "__main__":
	client = IrcClient()
	client.send("message from buildbot")
