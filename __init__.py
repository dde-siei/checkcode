# coding=utf-8
__version__ = "1.0.0"

''' Copyright (c) 2025 Rolling Loayza

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''

import os
import hashlib
import requests
import json

def getsha(filepath):
    """
    Compute the SHA-256 hash of a file.

    Args:
        filepath (str): Complete file path

    Returns:
        str: SHA-256 hash of the file in hexadecimal format.
    """
    sha_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Read and update hash in chunks of 4KB
        for byte_block in iter(lambda: f.read(4096), b""):
            sha_hash.update(byte_block)
    return sha_hash.hexdigest()

def randomfile():
    """
    Create a randon file name as MD5

    Args:
        None

    Returns:
        str: MD5 hash
    """
    rbbytes = os.urandom(32)
    filename = hashlib.md5(rbbytes).hexdigest()
    #tmp_path = os.path.join(tempfile.gettempdir(), folder_name)
    #os.makedirs(tmp_path, exist_ok=True)
    return filename

def getfile2json(url):
    """
    Create a randon file name as MD5

    Args:
        url (str): A web page Address, like GitHub

    Returns:
        str: A Json File
    """
    response = requests.get(url)
    jsonfile = response.json()
    return jsonfile

def add2version(versions, packages, newkey, newvalue):
    """
    Help to assing a new version script

    Args:
        versions (dict): A dictionary estructured
        packages (str): Name of package to update version
        newkey (str): Nwe Version Number
        newvalue (str): Assign a New SHA-256
        
    Returns:
        dict: A Dictionary file
    """
    if package not in versions_dict:
        versions[packages] = {}
    versions[package][newkey] = newvalue
    return newversion

def dict2json(dic, savefile):
    """
    Create a Json file

    Args:
        dic (dict): A dictionary estructured
        savefile (str): A full File address to save
        
    Returns:
        none
    """
    jsonstr = json.dumps(dic)
    with open(savefile,'w')as f:
        f.write(jsonstr)
