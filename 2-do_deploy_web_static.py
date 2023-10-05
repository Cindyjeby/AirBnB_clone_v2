#!/usr/bin/python3
"""sets up your web servers for deployment"""
from os.path import exists
from fabric.api import *

#set the host ip address
env.hosts = ['100.26.160.94', '54.85.48.49']
env.user = "ubuntu"

def do_deploy(archive_path):
    """distributes an achiveto webservers"""

    if not exists(archive_path):
        return False

    try:
        # upload thearchive to the tmp directory of the webserver
        put(archive_path, "/tmp/")

        #uncompress the archive to the folder
        archive_filename = archive_path.split("/")[-1]
        release_folder = "/data/web_static/release/{}".format(
                archive_filename.split(".")[0])

        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        #delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        #remove the existing symbolic link
        current_link = "/data/web_static/current"
        run("rm -f {}".format(current_link))

        #create a new link
        run("ln -s {} {}".format(release_folder, current_link))

        return True
    except Exception:
        return False
