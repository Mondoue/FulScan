

def prepareNmapArguments(target):
    nmap_arguments_raw = input("Enter arguments for nmap: ")
    print(nmap_arguments_raw)
    nmap_arguments = nmap_arguments_raw.split()

    nmap_command = ["nmap"]
    if nmap_arguments:

        for argument in nmap_arguments:
            nmap_command.append(argument)
    else:
        print("No arguments provided")

    nmap_command.append(target)
    return nmap_command

def prepareWhatwebArguments(target):
    whatweb_arguments_raw = input("Enter arguments for whatweb: ")
    whatweb_arguments = whatweb_arguments_raw.split()

    whatweb_command = ["whatweb"]
    if whatweb_arguments:
        for argument in whatweb_arguments:
            whatweb_command.append(argument)
    else:
        print("No arguments provided")
    whatweb_command.append(target)
    return whatweb_command

def prepareGobusterArguments(target):
    gobuster_arguments_raw = input("Enter arguments for gobuster: ")
    gobuster_wordlist = input("Enter wordlist location for Gobuster: ")
    gobuster_arguments = gobuster_arguments_raw.split()

    gobuster_command = ["gobuster"]
    gobuster_command.append("dir")
    gobuster_command.append("-u")
    gobuster_command.append(target)
    if gobuster_arguments:
        for argument in gobuster_arguments:
            gobuster_command.append(argument)
    else:
        print("No arguments provided")

    gobuster_command.append("-w")
    if not gobuster_wordlist:
        print("no wordlist provided, assuming /usr/share/wordlists/dirb/common.txt as default ")
        gobuster_command.append("/usr/share/wordlists/dirb/common.txt")
    else:
        gobuster_command.append(gobuster_wordlist)
    return gobuster_command

def prepareSSLscanArguments(target):
    ssl_arguments_raw = input("Enter arguments for sslscan: ")
    ssl_arguments = ssl_arguments_raw.split()
    ssl_command = ["sslscan"]
    if ssl_arguments:
        for argument in ssl_arguments:
            ssl_command.append(argument)
    else:
        print("No arguments provided")
    ssl_command.append(target)
    return ssl_command