__author__ = 'joede'
import paramiko
import time
# Perform common tasks for the whole pi farm
# TODO clean up the cut and paste code and wrap the client creation into a single proc

pilist = ['10.30.33.8', '10.30.33.9', '10.30.33.4','10.30.33.13', '10.30.32.245', '10.30.32.251',
          '10.30.32.249', '10.30.32.250', '10.30.32.254', '10.30.32.255']


def getBuffer(chan,expected):
    buff = ''
    while not buff.endswith(expected):
        resp = chan.recv(9999)
        buff += resp
        time.sleep(0.05)
    print buff


def update (destip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)
    print ("update list of "+ destip)
    chan.send('sudo apt-get update\n')
    time.sleep(2)
    getBuffer(chan,'$ ')
    time.sleep(2)

    print ("upgrade of " + destip)
    chan.send('sudo apt-get dist-upgrade -y\n')
    time.sleep(2)
    getBuffer(chan,'$ ')

def gitclone(destip, gitpass):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)
    print ("git clone "+ destip)
    remote = ""	
    chan.send('git clone' + remote +'\n')
    time.sleep(2)
    # BUG BUG - If we are already cloned this fails silently, need to check for "fatal"
    getBuffer(chan,".com': ")
    # Supply username
    username =""
    chan.send(username+'\n')
    time.sleep(2)
    getBuffer(chan,".com': ")

    # password
    chan.send(gitpass + '\n')
    time.sleep(2)
    getBuffer(chan,'$ ')

def gitPull(destip,gitpass):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)
    print ("git pull "+ destip)
    chan.send ('cd pymine\n')
    time.sleep(2)
    getBuffer(chan,'$ ')

    chan.send('git pull origin master\n')
    time.sleep(2)
    getBuffer(chan,".com': ")

    # Supply username
    username = "" + ' \n'
    chan.send(username)
    time.sleep(2)
    getBuffer(chan,".com': ")

    # password
    chan.send(gitpass + '\n')
    time.sleep(2)
    print "Waiting for git update to finish"
    getBuffer(chan,'$ ')


def reboot(ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)
    chan.send('sudo reboot\n')
    time.sleep(2)
    getBuffer(chan,'$ ')


def version(ip):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)
    chan.send('uname -a\n')
    time.sleep(2)
    getBuffer(chan,'$ ')


def poweroff(ip):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    chan = client.invoke_shell()
    output = chan.recv(1000)
    print output
    time.sleep(2)

    chan.send('sudo poweroff\n')
    time.sleep(2)
    getBuffer(chan,'$ ')


username = 'pi'
password = 'raspberry'

#gitpass = raw_input("Enter git password")
gitpass =""
for ip in pilist:
    # version(ip)
    gitPull(ip,gitpass)
    #update(ip)
    #reboot(ip)
    # poweroff(ip)
    #gitclone(ip,gitpass)
