#!/bin/bash
set -e
id=$(basename $(pwd))

mkdir -p meta

if [[ ! -f meta/description.txt ]]; then
	echo "Enter description (end with Ctrl-D)"
	cat > meta/desc.txt
	mv meta/desc.txt meta/description.txt
fi

if [[ -d "data" ]]; then
	echo ${id} > meta/id-${id}.txt
	(
		cd data
		find       > ../meta/find.txt
		tree -fias > ../meta/tree.txt
		tree -ah   > ../meta/tree_readable.txt
	)
	7z a wip.7z data -p${BLOB_PASS}
	mv wip.7z ${id}-data.enc.7z
	mv data data_done
fi

echo "Basic info"
date >> meta/info.txt
ls -l ${id}-data.enc.7z >> meta/info.txt
echo "Calc SHA256"
sha256sum ${id}-data.enc.7z > meta/sha256sum.txt

7z a ${id}-meta.7z meta
cat meta/info.txt
cat meta/sha256sum.txt

if [[ "$1" != "dry" ]]; then
	aws s3 cp ${id}-meta.7z s3://bvhbackups/meta/${id}-meta.7z
	aws s3 cp ${id}-data.enc.7z s3://bvhbackups/data/${id}-data.enc.7z #--storage-class ONEZONE_IA
fi

