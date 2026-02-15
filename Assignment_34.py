import os
import sys
import time
import shutil
import hashlib
import zipfile
import smtplib
import schedule
from email.message import EmailMessage


DEFAULT_EXCLUDE = [".tmp", ".log", ".exe"]
LOG_FOLDER = "Logs"
HISTORY_FILE = "backup_history.txt"

def create_log():
    try:
        os.makedirs(LOG_FOLDER, exist_ok=True)
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        logfile = os.path.join(LOG_FOLDER, f"BackupLog_{timestamp}.log")
        return logfile
    except Exception:
        sys.exit()

def write_log(logfile, message):
    try:
        with open(logfile, "a") as f:
            f.write(f"{time.ctime()} : {message}\n")
    except Exception:
        pass

def calculate_hash(path):
    hobj = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hobj.update(data)
    return hobj.hexdigest()

def backup_files(source, destination, exclude_ext, logfile):
    copied_files = []

    os.makedirs(destination, exist_ok=True)

    for root, dirs, files in os.walk(source):
        for file in files:

            if any(file.endswith(ext) for ext in exclude_ext):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, source)
            dest_path = os.path.join(destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            try:
                if (not os.path.exists(dest_path)) or \
                   (calculate_hash(src_path) != calculate_hash(dest_path)):

                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative)

            except Exception as e:
                write_log(logfile, f"Error copying {file} : {str(e)}")

    return copied_files

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"{folder}_{timestamp}.zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                z.write(full_path, relative)

    return zip_name

def send_email(receiver, logfile, zipname):
    try:
        sender = "gauri18@gmail.com"
        password = "password"

        msg = EmailMessage()
        msg["Subject"] = "Backup Completed - Marvellous Data Shield"
        msg["From"] = sender
        msg["To"] = receiver

        msg.set_content(f"Backup Completed Successfully.\nZip File: {zipname}")

        with open(logfile, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(logfile)
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception:
        pass

def restore_backup(zipfile_name, destination):
    try:
        if not os.path.exists(zipfile_name):
            raise Exception("Zip file not found")

        os.makedirs(destination, exist_ok=True)

        with zipfile.ZipFile(zipfile_name, 'r') as z:
            z.extractall(destination)

    except Exception:
        logfile = create_log()
        write_log(logfile, "Restore failed")

def update_history(zipname, filecount):
    try:
        size = os.path.getsize(zipname) / (1024 * 1024)

        with open(HISTORY_FILE, "a") as f:
            f.write(f"{time.ctime()} | Files: {filecount} | "
                    f"Zip: {zipname} | Size: {size:.2f} MB\n")
    except Exception:
        pass

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("No backup history available.")
        return

    with open(HISTORY_FILE, "r") as f:
        print(f.read())

def read_config(file):
    config = {}
    with open(file, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
    return config


def start_backup(source, receiver=None, exclude_ext=None):

    logfile = create_log()
    write_log(logfile, "Backup Started")

    try:
        if not os.path.exists(source):
            raise Exception("Source directory does not exist")

        exclude_ext = exclude_ext if exclude_ext else DEFAULT_EXCLUDE
        backup_folder = "MarvellousBackup"

        copied = backup_files(source, backup_folder, exclude_ext, logfile)
        zipname = make_zip(backup_folder)

        write_log(logfile, f"Files Copied: {len(copied)}")
        write_log(logfile, f"Zip Created: {zipname}")

        update_history(zipname, len(copied))

        if receiver:
            send_email(receiver, logfile, zipname)

        write_log(logfile, "Backup Completed Successfully")

    except Exception as e:
        write_log(logfile, f"Error: {str(e)}")

def main():
    try:

        # Restore Mode
        if len(sys.argv) == 4 and sys.argv[1] == "--restore":
            restore_backup(sys.argv[2], sys.argv[3])
            return

        # History Mode
        if len(sys.argv) == 2 and sys.argv[1] == "--history":
            show_history()
            return

        # Config File Mode
        if len(sys.argv) == 2 and sys.argv[1].endswith(".txt"):
            config = read_config(sys.argv[1])

            source = config.get("Source")
            email = config.get("Email")
            exclude = config.get("Exclude")

            exclude_list = exclude.split(",") if exclude else DEFAULT_EXCLUDE

            start_backup(source, email, exclude_list)
            return

        # Scheduled Mode
        if len(sys.argv) == 3:
            interval = int(sys.argv[1])
            source = sys.argv[2]

            if interval <= 0:
                raise Exception("Interval must be positive")

            schedule.every(interval).minutes.do(start_backup, source)

            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            raise Exception("Invalid arguments")

    except Exception as e:
        logfile = create_log()
        write_log(logfile, f"Startup Error: {str(e)}")

if __name__ == "__main__":
    main()
