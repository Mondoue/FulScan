import re

def parseNmapOutput(output):

    lines = output.splitlines()
    collecting = False
    os = "Unknown"
    mac = "Unknown"
    pretty_output = []

    try:
        for line in lines:

            # print("Current Line before strip and split")
            # print(line)
            line = line.strip()
            line = line.split()
            # print("Current Line after strip and split")
            # print(line)
            if not collecting:
                if len(line) >= 3:
                    if line[0] == "PORT" and line[1] == "STATE" and line[2] == "SERVICE":
                        print("Section Started")
                        pretty_output.append(line)
                        collecting = True
                        print(line)
                        continue

            if "Running:" in line[0]:
                os = " ".join(line[1:])
                continue
            if "MAC" in line[0]:
                mac = " ".join(line[1:])
                continue

            if collecting and "/tcp" in line[0] or "/udp" in line[0]:
                pretty_output.append(line)

                if not line:
                    print("section ended")
                    collecting = False
    except:
        pass

    # print("=======================")
    # print("PRETTY OUTPUT:")
    # print("Host: " + os)
    # print("Mac: " + mac)
    os = "Host: " + os
    mac = "Mac " + mac
    os = os.split()
    mac = mac.split()
    pretty_output.append(os)
    pretty_output.append(mac)
    # for line in pretty_output:
    #     print(" ".join(line))
    return pretty_output






def parseWhatwebOutput(output):
    lines = output.splitlines()
    pretty_output = []

    for line in lines:
        line = line.strip()
        line = line.split()
        pretty_output.append(line)
    return pretty_output

def parseGobusterOutput(output):
    lines = output.splitlines()
    pretty_output = []

    for line in lines:
        line = line.strip()
        line = line.split()
        pretty_output.append(line)
    return pretty_output


def parseSslscanOutput(output):
    lines = output.splitlines()
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    pretty_output = []

    collecting = False
    for line in lines:
        line = ansi_escape.sub('', line)
        line = line.strip()
        # line = line.split()
        if "Version" in line:
            pretty_output.append(line)
            continue
        if "OpenSSL" in line:
            pretty_output.append(line)
            continue
        print("WERE ABOUT TO START")
        print(repr(line))
        if line.endswith(":"):
            print("HEADER STARTED")
            collecting = True
            pretty_output.append(line)
            continue

        if collecting and line:
            pretty_output.append(line)
            continue
        if collecting and not line:
            collecting = False
            pretty_output.append(" ")
            print("Section ended")
    print("=====================================")
    print("\n".join(pretty_output))
    return pretty_output


