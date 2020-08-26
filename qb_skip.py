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
check_torrents=[]
for torrent in torrents:
     if torrent['state'] == 'checkingUP':
         check_torrents.append(torrent)
print('Get', len(check_torrents), 'torrents.')
for torrent in check_torrents:
    filename = torrent['hash']+'.torrent'
    shutil.copy(qb_backup_path+filename, tmp_path)
    qb.delete(torrent['hash'])
    with open(tmp_path+filename,'rb') as f:
        qb.download_from_file(f,save_path=torrent['save_path'],category=torrent['category'],skip_checking=True)
    os.remove(tmp_path+filename)
    print('Force skip '+torrent['name'])
print('Finished.')
