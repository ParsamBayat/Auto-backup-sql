
#  In the name of God
# project name : Auto Backaup sql
# Developer : Parsa bayat (github.com/ParsamBayat)

#lib
import os
import shutil
from datetime import datetime
import time

#code
def backup_database():
    db_username = 'root' #dont change this line 
    db_password = '' # Passowrd (Agar ramz nadarad taghir nadahid)
    db_name = 'dashbash' #esm database 
    xampp_path = r'C:\XAMPP' # mahal nasb xampp 
    backup_path = r'C:\Users\Administrator\Desktop\Sql_Backup' #mahl save backup

    shutil.rmtree(backup_path, ignore_errors=True)
    os.makedirs(backup_path)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = f'{db_name}_backup_{timestamp}.sql'

    backup_command = (
        f'{xampp_path}\\mysql\\bin\\mysqldump.exe '
        f'--user={db_username} --password={db_password} --databases {db_name} > {backup_path}\\{backup_file}'
    )

    os.system(backup_command)

    print(f'Backup completed successfully: {backup_path}\\{backup_file}')

while True:
    backup_database()
    time.sleep(600)  # Be tor default baraye 600 sanie (dah daghighe tanzim shode ast)

    #END 
    #Parsa Bayat @MR_Morphines
