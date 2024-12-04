import wmi

# List of known backup software signatures (can be expanded based on your environment)
backup_software_signatures = [
    # Enterprise Backup Solutions
    "Veeam",            # Veeam Backup & Replication
    "Druva",            # Druva InSync or Druva Phoenix
    "Acronis",          # Acronis Backup
    "Veritas",          # Veritas NetBackup
    "CommVault",        # CommVault Simpana
    "Carbonite",        # Carbonite Backup
    "BackupExec",       # Symantec Backup Exec
    "Arcserve",         # Arcserve UDP (Unified Data Protection)
    "Datto",            # Datto Backup (Business continuity)
    "Barracuda",        # Barracuda Backup
    "Zerto",            # Zerto Disaster Recovery and Backup
    "IBM Spectrum",     # IBM Spectrum Protect (formerly Tivoli Storage Manager)
    "Unitrends",        # Unitrends Backup and DR
    "Asigra",           # Asigra Cloud Backup
    "Unitrends",        # Unitrends Backup
    "FalconStor",       # FalconStor Backup Solutions

    # Cloud Backup Solutions
    "Backblaze",        # Backblaze Backup (Cloud)
    "CrashPlan",        # CrashPlan (Cloud backup)
    "IDrive",           # IDrive (Cloud and local backup)
    "Amazon S3",        # Amazon S3 Backup
    "Wasabi",           # Wasabi Cloud Storage
    "Dropbox",          # Dropbox Backup (Cloud storage)
    "Google Drive",     # Google Drive Backup
    "OneDrive",         # OneDrive Backup (Cloud storage)
    "Box",              # Box Backup (Cloud storage)
    "Microsoft Azure",  # Microsoft Azure Backup Service
    "Google Cloud",     # Google Cloud Backup
    "CloudBerry",       # CloudBerry Backup (MSP360)
    
    # Virtualization and Hypervisor Backup
    "Veeam",            # Veeam Backup & Replication (Hyper-V, VMware)
    "Altaro",           # Altaro VM Backup (for Hyper-V and VMware)
    "Trilead",          # Trilead VM Backup
    "Vembu",            # Vembu Backup
    "SolarWinds",       # SolarWinds Backup (Cloud and On-Premise)
    "Datto",            # Datto Backup for Virtualization (Backup & Disaster Recovery)

    # File/Folder Backup Solutions
    "Cobian",           # Cobian Backup (File Backup software)
    "SyncBack",         # SyncBack Backup (File backup software)
    "EaseUS",           # EaseUS Todo Backup
    "AOMEI",            # AOMEI Backupper
    "Macrium",          # Macrium Reflect (Disk Imaging and Backup)
    "RoboCopy",         # RoboCopy (Windows file copying tool)
    "FastCopy",         # FastCopy (Fast file copy and backup)
    
    # Backup Agents and Services
    "VeeamAgent",       # Veeam Agent for Windows and Linux
    "DruvaAgent",       # Druva InSync Agent
    "AcronisAgent",     # Acronis Backup Agent
    "CommVaultAgent",   # CommVault Backup Agent
    "CarboniteAgent",   # Carbonite Backup Agent
    "VeritasAgent",     # Veritas NetBackup Agent
    "ZertoAgent",       # Zerto Backup Agent

    # Other Backup Solutions and Tools
    "BackUp",           # Backup and Restore (Generic)
    "NovaStor",         # NovaStor Backup
    "StorageCraft",     # StorageCraft ShadowProtect
    "Bacula",           # Bacula (Open Source Backup)
    "R1Soft",           # R1Soft Continuous Data Protection (CDP)
    "Acronis",          # Acronis Backup (Various agents)
    "BackupPC",         # BackupPC (Open Source Backup)
    "Bareos",           # Bareos (Open Source Backup Software)
    "Tivoli",           # IBM Tivoli Storage Manager (TSM)
    "SUSE",             # SUSE Linux Enterprise Backup
    "OpenStack",        # OpenStack Backup
    "CommVaultSimpana", # CommVault Simpana
    "Ahsay",            # Ahsay Online Backup
    "Zmanda",           # Zmanda Backup Solutions
    "VBackup",          # VBackup (Backup tool for virtual machines)
    "SkyKick",          # SkyKick Cloud Backup
    "Kaseya",           # Kaseya VSA (Backup and monitoring)
    "Nexenta",          # Nexenta Backup Solution
    "Voxility",         # Voxility Backup
    "PHD Virtual",      # PHD Virtual Backup (for VMware)
    "V-Machine",        # V-Machine Backup
]


def check_installed_software():
    # Initialize WMI interface
    c = wmi.WMI()

    # Query for installed programs
    installed_programs = c.query("SELECT * FROM Win32_Product")

    print("Checking for installed backup software...\n")
    found_software = []

    for program in installed_programs:
        for signature in backup_software_signatures:
            if signature.lower() in program.Name.lower():
                found_software.append(program.Name)

    if found_software:
        print("Found the following backup software installed:")
        for software in found_software:
            print(f"  - {software}")
    else:
        print("No known backup software found in installed programs.")

def check_running_processes():
    # Initialize WMI interface
    c = wmi.WMI()

    # Query for running processes
    running_processes = c.query("SELECT * FROM Win32_Process")

    print("\nChecking for running backup software processes...\n")
    found_processes = []

    for process in running_processes:
        for signature in backup_software_signatures:
            if signature.lower() in process.Name.lower():
                found_processes.append(process.Name)

    if found_processes:
        print("Found the following backup software running:")
        for process in found_processes:
            print(f"  - {process.Name}")
    else:
        print("No known backup software processes found running.")

def check_backup_services():
    # Initialize WMI interface
    c = wmi.WMI()

    # Query for running services
    running_services = c.query("SELECT * FROM Win32_Service")

    print("\nChecking for running backup software services...\n")
    found_services = []

    for service in running_services:
        for signature in backup_software_signatures:
            if signature.lower() in service.Name.lower():
                found_services.append(service.Name)

    if found_services:
        print("Found the following backup software services running:")
        for service in found_services:
            print(f"  - {service.Name}")
    else:
        print("No known backup software services found running.")

# Function to check for shadow copies (backups/snapshots)
def check_shadow_copies():
    c = wmi.WMI()

    # Querying for shadow copies
    shadow_copies = c.query("SELECT * FROM Win32_ShadowCopy")

    print("\nChecking for shadow copies (backups/snapshots)...\n")
    if shadow_copies:
        for shadow in shadow_copies:
            print(f"Shadow Copy ID: {shadow.ID}")
            print(f"Description: {shadow.Description}")
            print(f"DeviceObject: {shadow.DeviceObject}")
            print(f"VolumeName: {shadow.VolumeName}")
            print(f"InstallDate: {shadow.InstallDate}")
            print(f"State: {shadow.State}")
            print("-" * 40)
    else:
        print("No shadow copies found on this system.")

def check_scheduled_tasks():
    # Initialize WMI interface
    c = wmi.WMI()

    # Query for scheduled tasks
    scheduled_tasks = c.query("SELECT * FROM Win32_ScheduledJob")

    print("\nChecking for backup-related scheduled tasks...\n")
    found_tasks = []

    for task in scheduled_tasks:
        for signature in backup_software_signatures:
            if signature.lower() in task.Name.lower():
                found_tasks.append(task.Name)

    if found_tasks:
        print("Found the following backup-related scheduled tasks:")
        for task in found_tasks:
            print(f"  - {task.Name}")
    else:
        print("No backup-related scheduled tasks found.")

def main():
    print("Starting to check for backup solutions on the system...\n")

    check_installed_software()
    check_running_processes()
    check_backup_services()
    check_shadow_copies()
    check_scheduled_tasks()

if __name__ == "__main__":
    main()
