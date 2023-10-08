#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive and deploys it to web servers.
"""

from fabric.decorators import task
from fabric.api import run, local, env, put
from datetime import datetime
import os

# Define the remote servers
env.hosts = ["100.25.37.123", "52.91.122.53"]


def do_deploy(archive_path):
    """Distribute an archive to web servers and deploy it."""
    try:
        if not os.path.exists(archive_path):
            return False

        # Extract information from the archive_path
        archive_filename = os.path.basename(archive_path)
        ext_splitted = os.path.splitext(archive_filename)[0]
        remote_path = "/data/web_static/releases/"

        # Upload the archive to the remote server's /tmp/ directory
        put(archive_path, "/tmp/")

        # Create a new directory and extract the archive
        run("mkdir -p {}{}".format(remote_path, ext_splitted))
        run("tar -xzf /tmp/{} -C {}{}".format(archive_filename, remote_path, ext_splitted))

        # Remove the uploaded archive from /tmp/
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of the extracted folder to the target directory
        run("mv {1}{0}/web_static/* {1}{0}/".format(ext_splitted, remote_path))

        # Remove the original web_static folder
        run("rm -rf {}{}/web_static".format(remote_path, ext_splitted))

        # Update the symbolic link to the current release
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(remote_path, ext_splitted))

        return True
    except Exception as e:
        return False


def do_pack():
    """Generate a .tgz archive from the web_static folder."""
    try:
        date_data = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date_data)
        local("mkdir -p versions")
        local("tar -czvf {} web_static/".format(file_name))
        return file_name
    except Exception as e:
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")
