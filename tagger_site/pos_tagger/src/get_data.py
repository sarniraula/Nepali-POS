# -*- coding: utf-8 -*-

"""
Nepali corpora parser

@author: sandesh
"""

import xml.etree.ElementTree as ET
import os


def get_tags():
    tag_list = list()
    for rootdir, dirs, files in os.walk("/home/sandesh/Major/tagset/cs"):
        for name in files:
            filename = os.path.join(rootdir, name)

            tree = ET.parse(filename)
            root = tree.getroot()

            for sentence in root.iter('s'):
                tag_sentence = list()
                for word in sentence.findall('w'):
                    text = word.text
                    tag = word.get('ctag')
                    tag_list.append((text, tag))
                    # tag_sentence.append((text, tag))
                # tag_list.append(tag_sentence)
    return tag_list[0:100]

#resultingTree = ET.tostring(root, encoding='utf-16')
#print(resultingTree.decode('utf-16'))
