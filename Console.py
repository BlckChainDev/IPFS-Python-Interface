import sqlite3
import Helpers
import NewItem
import ipfshttpclient
client = ipfshttpclient.connect()
onetwo = {}
try:
    onetwo = Helpers.updatedict('doc')
except sqlite3.OperationalError:
    con = sqlite3.connect('doc' + '.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE ''' + 'spacedb' + ''' (name, hash, date)''')
    con.commit()
    print("Created Database")
    con.close()
if 'GENESIS' in onetwo:
    pass
else:
    Helpers.addItem('doc', 'GENESIS', '0000000000000000000000000000000000000000', 'spacedb')

quit = False

def console(username):
    global quit
    while quit != True:
        Helpers.clear(15)
        print(Helpers.ConsoleMenu)
        awn = Helpers.ask('Please Select Only One')
        if awn == '1':
            check = Helpers.updatedict('doc')
            filename = Helpers.ask('FileName')
            if filename in check:
                print("Already Exits")
            else:
                item = NewItem.NewItem(filename, client, username, True)
                hash = Helpers.getHash(item, username, True)
                Helpers.addItem('doc', filename, hash, 'spacedb')
                print("Done")
            input("Press Enter To Continue>>>")
        elif awn == '2':
            print(Helpers.updatedict('doc'))
            input("Press Enter To Continue>>>")
        elif awn == '3':
            try:
                hash = input("Hash For File(No Spaces)>>>")
                file = NewItem.GetFile(client, hash)
                savefile = Helpers.ask('Enter File To Save (No Spaces)>>>')
                save = open(savefile, 'w')
                save.write(file)
                save.close()
                print("saved")
                input("Press Enter To Continue>>>")
            except:
                print("There was an error")
        elif awn == '4':
            print(Helpers.Credits)
            input("Press Enter To Continue>>>")
        else:
            quit = True
            break


if __name__ == "__main__":
    console(Helpers.ask('Code Name'))