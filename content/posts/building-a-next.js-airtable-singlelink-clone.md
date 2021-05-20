+++
ShowBreadCrumbs = true
ShowPostNavLinks = false
ShowReadingTime = true
TocOpen = false
author = "l3gacy"
comments = false
date = 2021-05-20T13:27:58Z
description = ""
disableHLJS = false
disableShare = false
draft = true
hideSummary = false
hidemeta = true
showToc = true
tags = ["singlelink", "airtable", "nextjs"]
title = "Building a Next.js + Airtable singlelink clone."

+++
## Backstory

Recently, something fun happened! I got my first real commission of a website, and it just so happened that I had basically written it earlier that day. I had been building a site for a hackathon I might run at some point, and I wanted to be able to have it not be hard-coded and be more user-friendly than mdx.

I had recently learned about [Airtable](https://airtable.com) thanks to [Hackclub](https://hackclub.com), so I thought why not use this? And in about an hour I had a working demo. I then thought I was done and I was going to move on from that project, but the universe had other plans! Specifically, my good friend asked me to make a website for them. I was a bit worried at first that it would be something I can't do, but they just wanted a singlelink-like thing for their TikTok (If I get permission from them, I'll link it here). 

So I just took the code I had written earlier and adapted it into [Multilink](https://github.com/l3gacyb3ta/multilink)! Obviously, it's FOSS, so it's on GitHub!

## Main Challenges:

* Because this is a real person I'm building a website for, I had to include some security features, which meant I had to figure out .env files for Next.js.
* I also wanted to implement analytics, which meant I had to find a modern _and_ open-source analytics system.

## Analytics: