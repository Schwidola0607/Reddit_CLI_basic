# Reddit CLI 
## Introduction
### Why Reddit CLI?
> Coworker who sees me looking at something in a browser: "Glad you're not busy; I need you to do this, this, this..."
> Coworker who sees me staring intently at a command prompt: Backs away, slowly...

A nice little CLI whose UI I designed from scratch.

Built on top of [&lt;PRAW&gt;](https://praw.readthedocs.io/en/latest/) 
and [&lt;Click&gt;](https://click.palletsprojects.com/en/8.0.x/)


## Setup
Create a requirement.txt and fill it with this
```
praw
click
textwrap
colorama
python-dotenv
```

Once you have done that, run the following to install those files

```console
$ pip install -r requirements.txt
```

Get your reddit client_id and client_secret by creating an app here
https://www.reddit.com/prefs/apps

Next, create a .env file like the following

```
CLIENT_ID=<your client id>
CLIENT_SECRET=<your client secret>
REDDIT_USERNAME=<your reddit username>
```
