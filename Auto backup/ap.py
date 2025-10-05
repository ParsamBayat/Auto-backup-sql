# In the name of God
# project name: Auto Backup sql
# Developer: Parsa bayat (github.com/ParsamBayat)

import os
import subprocess
from datetime import datetime
import time
import sys

def backup_database():
    db_username = 'root'  # dont change this line 
    db_password = ''  # Password (اگر رمز ندارد تغییر ندهید)
    db_name = 'dashbash'  # اسم دیتابیس 
    xampp_path = r'C:\XAMPP'  # محل نصب xampp 
    backup_path = r'C:\Users\Administrator\Desktop\Sql_Backup'  # محل ذخیره بکاپ

    # ایجاد پوشه بکاپ اگر وجود ندارد
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    # زمان‌بندی برای نام فایل
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = os.path.join(backup_path, f'{db_name}_backup_{timestamp}.sql')

    # مسیر کامل به mysqldump
    mysqldump_path = os.path.join(xampp_path, 'mysql', 'bin', 'mysqldump.exe')
    
    if not os.path.exists(mysqldump_path):
        print(f"Error: mysqldump.exe not found at {mysqldump_path}")
        return False

    try:
        # ساخت دستور با استفاده از subprocess برای مدیریت بهتر
        command = [
            mysqldump_path,
            f'--user={db_username}',
            f'--databases',
            db_name
        ]
        
        # اگر پسورد وجود دارد اضافه کن
        if db_password:
            command.append(f'--password={db_password}')
        
        # اجرای دستور و ذخیره خروجی در فایل
        with open(backup_file, 'w') as output_file:
            result = subprocess.run(
                command, 
                stdout=output_file, 
                stderr=subprocess.PIPE,
                text=True,
                timeout=30  # تایم‌اوت 30 ثانیه
            )
        
        if result.returncode == 0:
            print(f'Backup completed successfully: {backup_file}')
            return True
        else:
            print(f'Backup failed with error: {result.stderr}')
            # حذف فایل بکاپ ناموفق
            if os.path.exists(backup_file):
                os.remove(backup_file)
            return False
            
    except subprocess.TimeoutExpired:
        print("Backup process timed out")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def main():
    print("Auto Backup SQL started...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            success = backup_database()
            if success:
                print("Waiting for next backup...")
            else:
                print("Backup failed, retrying in 1 minute...")
                time.sleep(60)  # یک دقیقه صبر کن اگر خطا داشت
                continue
                
            time.sleep(600)  # ۱۰ دقیقه منتظر بمان
    
    except KeyboardInterrupt:
        print("\nBackup service stopped by user")
    except Exception as e:
        print(f"Fatal error: {str(e)}")

if __name__ == "__main__":
    main()
