#!/usr/bin/bash

set -e
commit=$1
version=$2

echo "Commit: $commit";
echo "Version tag: $version";

GIT_COMMITTER_DATE="$(git show ${commit} --format=%aD | head -1)" \
git tag -a "${version}" -s "${commit}" -m "${version}"
