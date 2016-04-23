import os
import json

from . import file_sys

def delete_file(fp):
    """
    :type fp: str
    """
    fp = os.path.expanduser(fp)
    try:
        if file_sys.file_exists(fp):
            os.remove(fp)
    except Exception as e:
        return 'Error occured while deleting {}\n{}'.format(fp, e.args)

def json_from_file(fp):
    """
    :type fp: str
    """
    fp = os.path.expanduser(fp)
    try:
        if file_sys.file_exists(fp):
            with open(fp, 'r') as f:
                return json.load(f)
        return dict()
    except Exception as e:
        return 'Error occured while reading {} as json\n{}'.format(fp, e.args)

def json_to_file(fp, content):
    """
    :type fp: str
    :type content: json encodable obj
    """
    fp = os.path.expanduser(fp)
    try:
        with open(fp, 'w') as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        return 'Error occured while writing json to {}\n{}'.format(fp, e.args)

def set_from_file(fp):
    """
    :type fp: str
    :returns: contents of file at file_path where each line is an element in returned set
    """
    fp = os.path.expanduser(fp)
    try:
        if file_sys.file_exists(fp):
            with open(fp, 'r') as f:
                return set([line.strip() for line in f.readlines()])
        return set()
    except Exception as e:
        return 'Error occured while reading {} as set\n{}'.format(fp, e.args)

def str_from_file(fp):
    """
    :type fp: str
    :returns: contents of file at file_path as string
    """
    fp = os.path.expanduser(fp)
    try:
        if file_sys.file_exists(fp):
            with open(fp, 'r') as f:
                return f.read()
        return str()
    except Exception as e:
        return 'Error occured while reading {} as string\n{}'.format(fp, e.args)

def str_to_file(fp, content):
    """
    :type fp: str
    :type content: str
    """
    fp = os.path.expanduser(fp)
    try:
        with open(fp, 'w') as f:
            f.write(content)
    except Exception as e:
        return 'Error occured while reading {} as set\n{}'.format(fp, e.args)