set -e

disk_index=42 #TODO
# get from blkid
luks_UUID="QQQQQQQ" #TODO
diskName="BVHBUP${disk_index}"
partition_boot="${diskName}BOOT"
partition_data="${diskName}DATA"


if [[ ! -f "/mnt/backup/gui.py" ]]; then
	cryptsetup open --type luks /dev/disk/by-uuid/${luks_UUID} luks-${partition_data}
	mount /dev/mapper/luks-${partition_data} /mnt/backup
fi


pushd /mnt/backup
python3 gui.py
popd


echo "Press enter to unmount encrypted partition"
umount /mnt/backup
echo "Press enter to release encrypted partition"
cryptsetup close luks-${partition_data}
echo "Press enter to exit"

