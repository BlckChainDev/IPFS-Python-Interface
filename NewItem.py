import datetime
import Helpers

def NewItem(filename : str, client, sig : str, tf : bool):
    if tf:
        file = open(str(filename), 'a')
        sig = sig + '\n'
        writee = [str(datetime.datetime.now()), '\n', sig]
        file.writelines(writee)
        file.close()
    item = client.add(str(filename))
    Helpers.addItem('doc', str(filename), Helpers.getHash(item, 'None', False), 'spacedb')
    return item

def GetFile(client, item):
    if type(item) == str:
        getfile = client.cat(item)
        getfile = getfile.decode('utf-8')
        return getfile
    elif type(item) == dict:
        hash = item["Hash"]
        getfile = client.cat(str(hash))
        getfile = getfile.decode('utf-8')
        return getfile
    else:
        return False

#client = ipfshttpclient.connect()
#hash = NewItem('./yeet.txt', client, 'Bot', True)
#print(hash)
#hash = dict(hash)
#print(GetFile(client, hash))