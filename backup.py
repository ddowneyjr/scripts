import tarfile
import datetime

backup_dir = ""
source_dir = ""
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_file = f"{backup_dir}/backup_{timestamp}.tar.gz"

with tarfile.open(backup_file, "w:gz") as tar:
    tar.add(source_dir, arcname="")

print(f"Backup created at {backup_file}")
