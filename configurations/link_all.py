#!/user/bin/env python
import os
import subprocess

file_maps = {
    './bash/bash_profile.bash': '~/.bash_profile'
}

for source in file_maps:
    subprocess.call('ln -fs $PWD/{} {}'.format(source, file_maps[source]), shell=True)
