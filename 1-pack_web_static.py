#!/usr/bin/python3
""" function that creates a .tgzarchive from web_static"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """create a tar gzipped archive"""
    #obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    #construct path where archive willbe saved
    archive_path = f"versions/web_static_{now}.tgz"
    local("mkdir -p versions")

    #use the tar command to create a compressed archive
    command = f"tar -czvf {archive_path} web_static"
    result = local(command, capture=True)

    #check result and return the aechive path if successful
    if result.return_code == 0:
        return archive_path
    else:
        return None
