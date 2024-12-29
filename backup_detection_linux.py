import os
import subprocess

# List of known backup software signatures
backup_software_signatures = [
    "Veeam",            # Veeam Backup & Replication
    "Druva",            # Druva InSync or Druva Phoenix
    "Acronis",          # Acronis Backup
    "Bacula",           # Bacula Backup Software
    "rsync",            # rsync (File-based backup utility)
    "tar",              # tar (Backup via compression)
    "Amanda",           # Amanda Network Backup
    "Clonezilla",       # Clonezilla (Disk cloning tool)
    "Timeshift",        # Timeshift (System restore and snapshot tool)
    "UrBackup",         # UrBackup (Client-server backup solution)
    "Duplicity",        # Duplicity (Backup solution using encryption)
    "BorgBackup",       # BorgBackup (Deduplicating backup software)
    "Restic",           # Restic (Backup tool)
    "rclone",           # rclone (Cloud and remote storage backup)
    "Duplicity",        # Duplicity (Encrypted backups)
    "S3QL",             # S3QL (Cloud storage for backups)
]

# Function to check for installed backup software
def check_installed_software():
    print("Checking for installed backup software...\n")
    found_software = []
    
    # Check installed packages
    try:
        result = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        installed_packages = result.stdout.splitlines()
        
        for package in installed_packages:
            for signature in backup_software_signatures:
                if signature.lower() in package.lower():
                    found_software.append(package)
        
    except Exception as e:
        print(f"Error checking installed software: {e}")
    
    if found_software:
        print("Found the following backup software installed:")
        for software in found_software:
            print(f"  - {software}")
    else:
        print("No known backup software found in installed packages.")

# Function to check running backup processes
def check_running_processes():
    print("\nChecking for running backup processes...\n")
    found_processes = []
    
    try:
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        running_processes = result.stdout.splitlines()
        
        for process in running_processes:
            for signature in backup_software_signatures:
                if signature.lower() in process.lower():
                    found_processes.append(process)
        
    except Exception as e:
        print(f"Error checking running processes: {e}")
    
    if found_processes:
        print("Found the following backup software processes running:")
        for process in found_processes:
            print(f"  - {process}")
    else:
        print("No known backup software processes found running.")

# Function to check backup services (systemd)
def check_backup_services():
    print("\nChecking for running backup software services...\n")
    found_services = []
    
    try:
        result = subprocess.run(['systemctl', 'list-units', '--type=service'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        services = result.stdout.splitlines()
        
        for service in services:
            for signature in backup_software_signatures:
                if signature.lower() in service.lower():
                    found_services.append(service)
        
    except Exception as e:
        print(f"Error checking running services: {e}")
    
    if found_services:
        print("Found the following backup software services running:")
        for service in found_services:
            print(f"  - {service}")
    else:
        print("No known backup software services found running.")

# Function to check for LVM snapshots (Linux backups)
def check_lvm_snapshots():
    print("\nChecking for LVM snapshots...\n")
    found_snapshots = []
    
    try:
        result = subprocess.run(['lvs', '--noheadings', '-o', 'lv_name,lv_size,origin'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        lvs_output = result.stdout.splitlines()
        
        for line in lvs_output:
            if "snapshot" in line:
                found_snapshots.append(line)
        
    except Exception as e:
        print(f"Error checking for LVM snapshots: {e}")
    
    if found_snapshots:
        print("Found the following LVM snapshots (backup volumes):")
        for snapshot in found_snapshots:
            print(f"  - {snapshot}")
    else:
        print("No LVM snapshots found on this system.")

# Function to check for backup-related cron jobs
def check_scheduled_tasks():
    print("\nChecking for backup-related cron jobs...\n")
    found_cron_jobs = []
    
    try:
        result = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        cron_jobs = result.stdout.splitlines()
        
        for job in cron_jobs:
            for signature in backup_software_signatures:
                if signature.lower() in job.lower():
                    found_cron_jobs.append(job)
        
    except subprocess.CalledProcessError:
        print("No cron jobs found for the current user.")
    except Exception as e:
        print(f"Error checking for scheduled cron jobs: {e}")
    
    if found_cron_jobs:
        print("Found the following backup-related cron jobs:")
        for job in found_cron_jobs:
            print(f"  - {job}")
    else:
        print("No backup-related cron jobs found.")



def main():
    print("Starting to check for backup solutions and backup-related tasks on the system...\n")
    
    check_installed_software()
    check_running_processes()
    check_backup_services()
    check_lvm_snapshots()  # Check for LVM snapshots (backup volumes)
    check_scheduled_tasks()  # Check for backup-related cron jobs



if __name__ == "__main__":
    main()
