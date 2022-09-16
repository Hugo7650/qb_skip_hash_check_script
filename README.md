# Qbittorrent强制跳过校验python脚本

python版本：3+

依赖库：python-qbitorrent

参数：

| 参数  | 说明 |
| ------------- | ------------- |
| qb_url  | webui链接  |
| qb_username  | webui用户名(本地跳过验证则留空)  |
| qb_password  | webui密码  |
| qb_nackup_path  | qb备份的的种子文件夹路径  |

备份路径：
  
 - windows: `C:/Users/<user>/AppData/Local/qBittorrent/BT_backup/`
    
 - linux: `/home/<user>/.local/share/data/qBittorrent/BT_backup/`

运行：

 - `curl -O https://raw.githubusercontent.com/Hugo7650/qb_skip_hash_check_script/master/qb_skip.py` 下载脚本
 - `pip install python-qbittorrent` 安装依赖库
 - 修改py文件添加上对应的参数
 - 运行

请在本地环境/ssh后运行

仅在windows上测试过

原理：

 - 通过webapi获取到要检查的种子
 - 找到对应的种子文件
 - 复制到当前文件夹
 - 在qb上删除这个种子
 - 再添加进去并跳过校验
 - 最后删除当前文件夹下的副本
