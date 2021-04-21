text = """
---
title: "{title}"
date: {date}
# weight: 1
# aliases: ["/"]
tags: ["{tag}"]
author: "l3gacy"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: ""
disableHLJS: false # to disable highlightjs
disableShare: false
hideSummary: false

ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowToc: true # table of contents
---
"""
fnames = []
import os
for root, dirs, files in os.walk("source/_posts", topdown=False):
   for name in files:
      fnames.append(os.path.join(root, name))

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

for file in fnames:
    with open(file, "r") as reader:
        inputtext = reader.readlines()

        title = remove_prefix(inputtext[1], "title: ").strip("\n")
        date = remove_prefix(inputtext[2], "date: ").strip("\n")
        tag = remove_prefix(inputtext[1], "tags: ").strip("\n")

        newheader = text.format(title=title, date=date, tag=tag)
        #print(newheader)

        newfile = inputtext.copy()
        newfile.pop(0)
        newfile.pop(0)
        newfile.pop(0)
        newfile.pop(0)
        newfile.pop(0)

        newheader = newheader.split("\n")

        newfile = newheader + newfile

        output = "\n".join(newfile)
        with open("content/" + remove_prefix(file, "source/_posts/"), "w") as writable:
            writable.write(output)




