import shutil
import subprocess

def checkNmap():
    if (shutil.which("nmap")):
        print("Nmap Installed")
        return True
    else:
        prompt = input("[X] Nmap not Installed. Would you like ot install Nmap? (y/n)")
        if prompt == "y":
            downloadNmap()
            return True
        else:
            print("Nmap will not be downloaded")
            return False

def checkWhatweb():
    if (shutil.which("whatweb")):
        print("WhatWeb Installed")
        return True
    else:
        prompt = input("[X]WhatWeb not Installed. Would you like to install Whatweb? (y/n)")
        if prompt =="y":
            downloadWhatweb()
            return True
        else:
            print("WhatWeb will not be downloaded")
            return False

def checkGobuster():
    if (shutil.which("gobuster")):
        print("GoBuster Installed")
        return True
    else:
        prompt = input("[X]GoBuster not Installed. Would you like to install Gobuster? (y/n)")
        if prompt == "y":
            downloadGobuster()
            return True
        else:
            print("Gobuster will not be downloaded")
            return False


def checkSSLscan():
    if (shutil.which("sslscan")):
        print("sslscan Installed")
        return True
    else:
        prompt = input("[X]sslscan not Installed. Would you like to install SSLscan? (y/n)")
        if prompt == "y":
            downloadsslscan()
            return True
        else:
            print("SSLscan will not be downloaded")
            return False


# Test function to download missing tools, might cause problems with admin privileges

def downloadNmap():
    subprocess.run(["sudo","apt","install","nmap"])

def downloadWhatweb():
    subprocess.run(["sudo","apt","install","whatweb"])

def downloadGobuster():
    subprocess.run(["sudo","apt","install","gobuster"])

def downloadsslscan():
    subprocess.run(["sudo","apt","install","sslscan"])
