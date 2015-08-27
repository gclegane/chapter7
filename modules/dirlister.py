import os

def run(**args):
    
    print "[*] In dirlistiner module."
    files = os.listdir(".")
    
    return str(files)


    