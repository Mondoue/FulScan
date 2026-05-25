

def outputAlltoText(nmap,whatweb,gobuster,sslscan):

    with open("fulscan_result.txt","w") as f:
        f.write("FULSCAN REPORT\n")
        f.write("==================================\n")
        f.write("NMAP REPORT \n\n")

        for line in nmap:
            f.write(" ".join(line) + "\n")
        f.write("====================================\n")
        f.write("\n\n")
        f.write("GOBUSTER REPORT\n\n")

        for line in gobuster:
            f.write(" ".join(line) + "\n")
        f.write("====================================\n")
        f.write("\n\n")
        f.write("WHATWEB REPORT\n\n")
        for line in whatweb:
            f.write(" ".join(line) + "\n")

        f.write("====================================\n")
        f.write("\n\n")
        f.write("SSL REPORT\n\n")
        for line in sslscan:
            f.write("".join(line) + "\n")

        print("Output Saved")