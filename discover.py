#!/usr/bin/env python
import os

def discoverFiles(startpath):
    extensions = [
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape',
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', 

        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx',
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 
        'yml', 'yaml', 'json', 'xml', 'csv', 
        'db', 'sql', 'dbf', 'mdb', 'iso', 

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', 
        'java', 'class', 'jar',
        'ps', 'bat', 'vb',
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', 
        'go', 'py', 'pyc', 'bf', 'coffee',

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', 

        'wasted', 
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == "__main__":
    x = discoverFiles('/')
    for i in x:
        print(i)
