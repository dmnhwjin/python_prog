dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'w')
    for key in db:
        dbfile.write(key + '\n')
        for (name, value) in db[key].items():
            dbfile.write(name+RECSEP+repr(value) + '\n')
        dbfile.write(ENDDB + '\n')
    dbfile.close()


def localDbase(dbfilename=dbfilename):
    """Parse structual , rebuild database"""
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
