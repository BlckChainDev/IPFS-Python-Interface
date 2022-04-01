setup = False
importtrue = False
verbose = True

try:
    import ipfshttpclient
    import sqlite3
    print("Import Successful")
    importtrue = True
except:
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable,
                            "-m", 
                            "pip", 
                            "install", 
                            "ipfshttpclient"])
        subprocess.check_call([sys.executable,
                            "-m", 
                            "pip", 
                            "install",
                            "sqlite3"])
        import ipfshttpclient
        import sqlite3
        importtrue = True
        if verbose:
            print("Import Successful!")
    except:
        print("You Have Not Installed Python Correct, \n",
            "Some Standerd Librarys Are Missing. Or If",
            "\nThis Error Keeps Ocurring Please Run\nWith",
            " Administrator Access.")


try:
    client = ipfshttpclient.connect()
    setup = True
except:
    print("Error")
    
def start():
    if setup and importtrue:
        if verbose:
            print("Successful and ready to start")
        return True
    return False