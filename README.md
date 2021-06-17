# Reddit CLI (v1.0)
## Introduction
### Why Reddit CLI?

<blockquote>
<p>Coworker who sees me looking at something in a browser:
&quot;Glad you're not busy; I need you to do this, this, this...&quot;
Coworker who sees me staring intently at a command prompt: Backs away, slowly...</p>
</blockquote>
Built on top of [PRAW](https://praw.readthedocs.io/en/latest/) 
and [Click](https://click.palletsprojects.com/en/8.0.x/)


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

## Usage
Guide:
Type your password like below and it is all set
<img src="https://media.giphy.com/media/6qJpCqv5ewzQXHuVpL/giphy.gif">


For more information please use my help menu
```
--help
```

## Contribution
Pull requests are accepted! Please open an issue if you find any bugs, or have any idea for a feature. Feedbacks are welcomed, especially about UI-design!

## Licensed
Apache License 2.0
