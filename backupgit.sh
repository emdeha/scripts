#!/bin/bash
# Shell script which creates a backup of a git repo every N seconds
# $1 - the directory in which the repo resides.
# $2 - interval for creating a backup.

function backupgit {
    # We don't want to make a backup if we haven't modified the files recently
    local backup_interval="$2"
    if ( [ -n "$(find . -mtime -$backup_interval | head -n 1)" ] ) then
        local backup_file="$1"
        if ( [[ -f "$backup_file" ]] ) then
            cp $backup_file $backup_file.back
            rm $backup_file
        fi


        if ( git bundle create $backup_file --all && [[ -f "$backup_file.back" ]] ) then
            rm $backup_file.back
        fi
    fi
}

while sleep $2
do
    backupgit $1/repo.bundle $2
done
