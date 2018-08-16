#!/usr/bin/python3
"""
    Deploys an archive to web servers
"""
from fabric.operations import env, local, put, run
from datetime import datetime
import os
from fabric.context_managers import lcd


env.hosts = ["35.185.90.17", "35.196.3.9"]
env.user = "ubuntu"


def do_pack():
    """
        Tarballs content in web_static folder
    """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    packin = local("tar -czvf {} web_static".format(name))
    if packin.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """
        Deploys packed content to servers
    """
    if os.path.exists(archive_path) is not True:
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False

    filename = archive_path[9:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename

    if run("mkdir -p {}".format(foldername)).failed:
        return False
    if run("tar -zxf {} -C {}". format(filename, foldername)).failed:
        return False
    if run("rm {}".format(filename)).failed:
        return False
    if run('mv {}/web_static/* {}'.format(foldername, foldername)).failed:
        return False
    if run("rm -rf {}/web_static".format(foldername)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {} /data/web_static/current".format(foldername)).failed:
        return False

    return True


def deploy():
    """
        Deploy function for pack and do_deploy
    """
    path = do_pack()

    if path is False:
        return False

    return do_deploy(path)


if __name__ == "__main__":
    do_pack()