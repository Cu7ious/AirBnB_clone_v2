#!/usr/bin/python3
"""
This program will use fabric to backup a directory into a tarball
"""


def do_pack():
    from fabric.operations import local, run
    from datetime import datetime
    import os
    from fabric.context_managers import lcd

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    with lcd("./versions"):
        local_name = local("pwd", capture=True)
        packin = local("tar -czvf {} ../web_static".format(name))
    for r, d, f in os.walk(local_name):
        for files in f:
            if files == name:
                path = os.path.join(r, files)
    if packin.succeeded:
        return path
    else:
        return None


if __name__ == "__main__":
    do_pack()
