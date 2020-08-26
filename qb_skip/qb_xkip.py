import os, shutil
from qbittorrent import Client

qb_url = ''
qb_username = ''
qb_password = ''
qb_backup_path = ''
tmp_path = os.getcwd() + '/'

qb = Client(qb_url)
qb.login(qb_username, qb_password)
torrents = qb.torrents()
l=[]
for i in torrents:
     if i['state'] == 'checkingUP':
         l.append(i)
print('Get', len(l), 'torrents.')
for i in l:
    filename = i['hash']+'.torrent'
    shutil.copy(qb_backup_path+filename, tmp_path)
    qb.delete(i['hash'])
    with open(tmp_path+filename,'rb') as f:
        qb.download_from_file(f,save_path=i['save_path'],category=i['category'],skip_checking=True)
    os.remove(tmp_path+filename)
    print('Force skip '+i['name'])
print('Finished.')
