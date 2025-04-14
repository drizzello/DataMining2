import datetime
import os
import glob
import pandas as pd


def backup_dataframe(df, backup_dir="backups", base_filename="df_backup"):
   # Create backup directory if it doesn't exist
   os.makedirs(backup_dir, exist_ok=True)
    
   # Generate timestamped filename
   timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
   filename = f"{base_filename}_{timestamp}.csv"
   filepath = os.path.join(backup_dir, filename)
    
   # Save DataFrame to CSV
   df.to_csv(filepath, index=False)
   print(f"✅ Backup saved to {filepath}")

def load_latest_backup(backup_dir="backups", base_filename="df_backup"):
    pattern = os.path.join(backup_dir, f"{base_filename}_*.csv")
    backup_files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

    if not backup_files:
        raise FileNotFoundError("❌ No backup files found.")

    latest_file = backup_files[0]
    print(f"📂 Loading latest backup: {latest_file}")
    return pd.read_csv(latest_file)
