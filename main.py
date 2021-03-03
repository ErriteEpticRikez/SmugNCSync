import paramiko
import json

running = True
dead = False
configData = None
setup = False

with open("config.json", "r") as configJson:
    configData = json.load(configJson)
    server = configData["server-ip"]
    username = configData["username"]
    password = configData["password"]
    smugdl_home = configData["smug-home"]
    setup = configData["setup"]

while running:
    ssh = paramiko.SSHClient()
    ssh.connect(server, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
    ssh.close()