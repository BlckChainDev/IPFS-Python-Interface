from datetime import datetime
import sqlite3

def updatedict(dbname):
    con = sqlite3.connect(dbname + '.db')
    cur = con.cursor()
    hashes = []
    names = []
    dicttion = {}
    for hash in cur.execute('SELECT hash FROM spacedb'):
        str(hash)
        hash = str(hash)
        hash = hash.strip("' (),")
        hashes.append(hash)
        hash = ""
    for name in cur.execute('SELECT name FROM spacedb'):
        str(name)
        name = str(name)
        name = name.strip("'(),")
        names.append(name)
        name = ""
    for x, y in zip(names, hashes):
        dicttion.update({x: y})
    con.close()
    return dicttion
    
def getHash(item, name, tf : bool):
    try:
        item = dict(item)
        return item['Hash']
    except KeyError:
        if tf:
            items = dict(item)
            print(items)
            name = str(name)
            return items[name]
        else:
            hashes = []
            items = dict(item)
            for i in items:
                hashes.append(items[i])
            return hashes
                

def addItem(dbname, name, hash, tablename):
    newhash = hash
    try:
        con = sqlite3.connect(dbname + '.db')
        cur = con.cursor()
        datenow = datetime.now()
        cur.execute("INSERT INTO " + tablename + " (name, hash, date) VALUES(?, ?, ?)", (name, newhash, datenow))
        con.commit()
        con.close()
    except:
        cur.execute('''CREATE TABLE ''' + tablename + ''' (name, hash, date)''')
        con.commit()
        print("Created Database")
        con.close()
        con = sqlite3.connect(dbname + '.db')
        cur = con.cursor()
        datenow = datetime.now()
        cur.execute("INSERT INTO " + tablename + " (name, hash, date) VALUES(?, ?, ?)", (name, newhash, datenow))
        con.commit()
        con.close()
        
def getanwser(text):
    newtext = str(text)
    text = newtext.strip("#!@#$%^*()")
    text = text.strip("'' }{|<>,./?`~")
    return text.lower()

def clear(num):
    for i in range(num):
        print('\n')
        
        
def ask(string):
    ask = input(string + '>>>')
    text = getanwser(ask)
    return text

Menu1 = "1:App Mode\n2:Console Mode\nCTRL+C: Quit\n\n"

ConsoleMenu = "1: New Item\n2: Review Items\n3: Download Items\n4: Credits\nCTRL + X: Quit"

Credits = "Code Dev: GOLD BEAR"

#import ipfshttpclient
#client = ipfshttpclient.connect()

#creating new item
# hashh = getHash(updatedict('doc'), 'hash', False)
#pprint(hashh)
#adding new item to database
#addItem('doc', 'Testt', '45764765467547654rvffgfhhfhh', 'spacedb')
#addItem('doc', 'yeet', '6546547kjhkjh787t7f#$W^645634', 'spacedb')
#addItem('doc', 'Testttt', '0x0454', 'spacedb')
#print(getHash(updatedict('doc'), 'yeet', True))
#pprint(updatedict('doc'))
#updating
