#/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, json, codecs

BOOKMARK_FILE = 'bookmarks.json'

def goto(alias):
    """
    Go to bookmark with name `alias`.

    :alias: name for the exist bookmark
    """

    if not __exist(alias):
        raise StandardError

    bookmarks = __load_bookmarks()
    os.chdir(bookmarks[alias])

    return;

def add(alias):
    """
    Add new bookmark with name `alias`.

    :alias: name for the new bookmark
    """
    if __exist(alias):
       raise StandardError

    bookmarks = __load_bookmarks()
    bookmarks[alias] = os.getcwd()
    __dump_bookmarks(bookmarks)

    return;

def list():
    """
    List all bookmarks.
    """
    bookmarks = __load_bookmarks()
    print bookmarks
    return;

def __load_bookmarks():
    input_file = open(BOOKMARK_FILE, 'r')
    try:
        bookmarks = json.load(input_file)
        input_file.close()
    except ValueError:
        bookmarks = {}

    return bookmarks;

def __dump_bookmarks(bookmarks):
    output_file = open(BOOKMARK_FILE, 'w')
    json.dump(bookmarks, output_file)
    output_file.close()
    return True;

def __exist(dir_name):
    """
    Return if dirname already exist
    """
    bookmarks = __load_bookmarks()
    return dir_name in bookmarks;

print("file is load!")
