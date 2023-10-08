#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
import os
import tarfile
from datetime import datetime


def do_pack():
    """
    Representation of the class do-pack
    """
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + timestamp + ".tgz"
        archive_path = os.path.join("versions", archive_name)
        os.makedirs("versions", exist_ok=True)

        with tarfile.open(archive_path, "w:gz") as archive:
            archive.add("web_static", arcname=os.path.basename("web_static"))

        return archive_path
    except Exception as e:
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")
