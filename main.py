import paramiko
import json
import os
import subprocess

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

print("Runniung check conditions")
passedChecks = False
if os.path.exists(smugdl_home):
    print("Smugmug DL Home exists")
    if os.path.exists(os.path.join(smugdl_home, "config.toml")):
        print("Smugmug Downloader config present")
        if os.path.exists(os.path.join(smugdl_home, "/cmd/smugmug-backup/main")):
            print("Main go file for SmugMug downloader is present.")
            passedChecks = True


if passedChecks:
    if setup:
        while running:
            subprocess.run(smugdl_home + "/cmd/smugmug-backup/main")
            ssh = paramiko.SSHClient()
            ssh.connect(server, username=username, password=password)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("Wall it worked")
            ssh.close()
    else:
        print("Your configuration has been ")