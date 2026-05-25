import subprocess
import ToolChecker
import ArgumentSetter
import ToolParser
from TextFiler import outputAlltoText

print("====================================================")
print("                         FulScan           ")
print("       Made by Mohannad Saif, Ibrahim Al-Absi")
print("========================================================")
#region Variables
target = input("Enter Target IP/URL: ")

hasNmap = ToolChecker.checkNmap()
hasWhatweb = ToolChecker.checkWhatweb()
hasGobuster = ToolChecker.checkGobuster()
hasSSLscan = ToolChecker.checkSSLscan()
#endregion

#region Arguments
nmap_command = ArgumentSetter.prepareNmapArguments(target)
whatweb_command = ArgumentSetter.prepareWhatwebArguments(target)
gobuster_command = ArgumentSetter.prepareGobusterArguments(target)
ssl_command = ArgumentSetter.prepareSSLscanArguments(target)
#endregion





#region Run Commands

if hasNmap:
    print("Running Command: " + " ".join(nmap_command))
    nmap_result = subprocess.run(nmap_command, text=True, capture_output=True)
    nmap_ready_output = ToolParser.parseNmapOutput(nmap_result.stdout)


if hasWhatweb:
    print("Running whatweb: " + " ".join(whatweb_command))
    whatweb_result = subprocess.run(whatweb_command, text=True, capture_output=True)
    whatweb_ready_output = ToolParser.parseWhatwebOutput(whatweb_result.stdout)
    whatweb_ready_output2 = ToolParser.parseWhatwebOutput(whatweb_result.stderr)
    whatweb_ready_output = whatweb_ready_output + whatweb_ready_output



if hasGobuster:
    print("Running gobuster: " + " ".join(gobuster_command))
    gobuster_result = subprocess.run(gobuster_command, text=True, capture_output=True)
    gobuster_ready_output = ToolParser.parseGobusterOutput(gobuster_result.stdout)
    gobuster_ready_output2 = ToolParser.parseGobusterOutput(gobuster_result.stderr)
    gobuster_ready_output = gobuster_ready_output + gobuster_ready_output2



if hasSSLscan:
    print("Running SSLscan: " + " ".join(ssl_command))
    sslscan_result = subprocess.run(ssl_command, text=True, capture_output=True)
    print(sslscan_result.stdout)
    ssl_ready_output = ToolParser.parseSslscanOutput(sslscan_result.stdout)
    print(sslscan_result.stdout)

#endregion



outputAlltoText(nmap_ready_output,whatweb_ready_output,gobuster_ready_output,ssl_ready_output)


