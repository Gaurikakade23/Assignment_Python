import psutil
import sys
import os
import time
import smtplib
import schedule
from datetime import datetime
from email.message import EmailMessage

def validate_inputs():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Invalid number of arguments")

        folder = sys.argv[1]
        email = sys.argv[2]
        interval = int(sys.argv[3])

        if interval <= 0:
            raise ValueError("Interval must be positive")

        return folder, email, interval

    except Exception as e:
        write_error_log(str(e))
        sys.exit()


def create_log_folder(folder):
    try:
        if not os.path.exists(folder):
            os.mkdir(folder)
        elif not os.path.isdir(folder):
            raise Exception("Invalid folder path")
    except Exception as e:
        write_error_log(str(e))
        sys.exit()


def get_log_file(folder):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(folder, f"PlatformSurveillance_{timestamp}.log")


def write_error_log(message):
    with open("Error.log", "a") as f:
        f.write(f"{datetime.now()} : {message}\n")


def collect_process_data():
    process_data = []

    for proc in psutil.process_iter():
        try:
            pid = proc.pid
            name = proc.name()
            cpu = proc.cpu_percent(interval=0.1)
            mem_info = proc.memory_info()
            rss = mem_info.rss
            vms = mem_info.vms
            mem_percent = proc.memory_percent()
            threads = proc.num_threads()

            try:
                open_files = len(proc.open_files())
            except:
                open_files = "Access Denied"

            process_data.append({
                "Name": name,
                "PID": pid,
                "CPU": cpu,
                "RSS": rss,
                "VMS": vms,
                "MemoryPercent": mem_percent,
                "Threads": threads,
                "OpenFiles": open_files
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return process_data


def write_process_log(logfile, process_data):
    border = "-" * 80

    with open(logfile, "w") as f:
        f.write(border + "\n")
        f.write("Platform Surveillance System Report\n")
        f.write("Timestamp : " + str(datetime.now()) + "\n")
        f.write(border + "\n\n")

        total_processes = len(process_data)
        f.write(f"Total Processes : {total_processes}\n\n")

        for proc in process_data:
            f.write(f"Process Name : {proc['Name']}\n")
            f.write(f"PID : {proc['PID']}\n")
            f.write(f"CPU % : {proc['CPU']}\n")
            f.write(f"Memory RSS : {proc['RSS']}\n")
            f.write(f"Memory VMS : {proc['VMS']}\n")
            f.write(f"Memory % : {proc['MemoryPercent']}\n")
            f.write(f"Threads Count : {proc['Threads']}\n")
            f.write(f"Open Files Count : {proc['OpenFiles']}\n")
            f.write("Timestamp : " + str(datetime.now()) + "\n")
            f.write(border + "\n")

        # Top 10 Memory Processes
        f.write("\nTop 10 Memory Consuming Processes\n")
        top_mem = sorted(process_data, key=lambda x: x["MemoryPercent"], reverse=True)[:10]
        for proc in top_mem:
            f.write(f"{proc['Name']} (PID {proc['PID']}) - {proc['MemoryPercent']}%\n")

        # Top CPU
        f.write("\nTop CPU Consuming Processes\n")
        top_cpu = sorted(process_data, key=lambda x: x["CPU"], reverse=True)[:5]
        for proc in top_cpu:
            f.write(f"{proc['Name']} (PID {proc['PID']}) - {proc['CPU']}%\n")

        # Top Threads
        f.write("\nTop Thread Count Processes\n")
        top_threads = sorted(process_data, key=lambda x: x["Threads"], reverse=True)[:5]
        for proc in top_threads:
            f.write(f"{proc['Name']} (PID {proc['PID']}) - {proc['Threads']} threads\n")

        # Top Open Files
        f.write("\nTop Open File Processes\n")
        valid_files = [p for p in process_data if isinstance(p["OpenFiles"], int)]
        top_files = sorted(valid_files, key=lambda x: x["OpenFiles"], reverse=True)[:5]
        for proc in top_files:
            f.write(f"{proc['Name']} (PID {proc['PID']}) - {proc['OpenFiles']} files\n")


def send_email(logfile, receiver):
    try:
        sender = "gauri18@gmail.com"
        password = "password"

        msg = EmailMessage()
        msg["Subject"] = "Platform Surveillance System Report"
        msg["From"] = sender
        msg["To"] = receiver
        msg.set_content("Attached is the latest system monitoring report.")

        with open(logfile, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(logfile)

        msg.add_attachment(file_data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception as e:
        write_error_log(str(e))


def surveillance_task(folder, receiver):
    try:
        logfile = get_log_file(folder)
        process_data = collect_process_data()
        write_process_log(logfile, process_data)
        send_email(logfile, receiver)
    except Exception as e:
        write_error_log(str(e))


def main():
    folder, receiver, interval = validate_inputs()
    create_log_folder(folder)

    schedule.every(interval).minutes.do(surveillance_task, folder, receiver)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
