from make_db_file import localDbase
db = localDbase()
for key in db:
    print key, '=>\n ', db[key]
print db['sue']['name']
