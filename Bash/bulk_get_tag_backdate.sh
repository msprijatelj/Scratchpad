#!/usr/bin/bash

set -e
file=$1
remote=$2

cur_dir=$(dirname "$0")

echo "Start!"
while IFS=',' read -r commit version rest; do 
    echo $("${cur_dir}/git_tag_backdate.sh" $commit $version)
done <"${file}"
# git push --tags $remote