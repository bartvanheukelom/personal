# This script file is not marked executable because of FAT restrictions.
# Start by running `bash welcome.sh`

set -e

# --- per disk config --- #
disk_index=42 #TODO
# get from blkid
luks_UUID="QQQQQQQ" #TODO

diskName="BVHBUP${disk_index}"
partition_boot="${diskName}BOOT"
partition_data="${diskName}DATA"


if [[ ! -f "/mnt/backup/gui.py" ]]; then
	echo "Opening LUKS volume ${luks_UUID}"
	cryptsetup open --type luks /dev/disk/by-uuid/${luks_UUID} luks-${partition_data}
	echo "Mounting in /mnt/backup"
	mount /dev/mapper/luks-${partition_data} /mnt/backup
fi
echo "$partition_data is now mounted at /mnt/backup"


pushd /mnt/backup
echo "Launching gui.py"
python3 gui.py
popd


echo "Press enter to unmount encrypted partition"
read
umount /mnt/backup

echo "Press enter to release encrypted partition"
read
cryptsetup close luks-${partition_data}

echo "Press enter to exit"
read

