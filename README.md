# HeartSync - an anonymous chat service on Discord

![Facebook avatar image](https://scontent.fhan2-2.fna.fbcdn.net/v/t1.6435-9/206655953_403676684598926_2393075570746251864_n.png?_nc_cat=111&ccb=1-5&_nc_sid=973b4a&_nc_ohc=C17rj_188OkAX_9ItAa&_nc_ht=scontent.fhan2-2.fna&oh=3099dd882bdaa7e89723a094538ec313&oe=614A3ACC)

*Hiện tại chưa có bản hướng dẫn tiếng Việt.*

# TOC
- [What is HeartSync?](#what-is-heartsync)
- [How does it works?](#how-does-it-work)
- [Usage](#usage)
- [Installation](#installation)
- [Currently available features](#currently-available-features)
- [How is it different from Messenger version?](#how-is-it-different-from-messenger-version)
- [Technology](#technology)
- [Support and feedback](#support-and-feedback)
## What is HeartSync?
A discord anonymous chat service bot. It offers private chat sessions with another user. A ready-to-use version has been deployed on [Facebook's messenger](https://www.facebook.com/adaptHeartSync) platform.

## How does it work?
It acts as a protocol in a peer-to-peer network - taking messages of a user and send it to another, without storing it anywhere.

## Usage
At the moment, there's no bot yet. But here're the steps that it should take to use the bot in future.
1. Create your private Discord server (or use a public server, if you don't mind someone else reading your chat)
2. Invite the bot to your server
3. Start a chat session using the command
```bash
\chat start
```
4. End a chat session using the command:
```bash
\chat end
```

## Installation
At the release stage, you can also download the source (or binary) and create your own bot, manage your own private chat network. Instructions'll come in a documentation after release stage.

## Currently available features
None... Hope this field can be filled soon.

## How is it different from Messenger version?
It's completely open source, therefore, it provide more anonymity. I can't make the Messenger version open source, since I'm not its original author.
I'm still finding a way to implement more features, and here are some that I'm dealing with:
- It'll support anonymous group chat
- It'll have some text-based games that can be played in the middle of a chat session
- Each user'll have a "profile" in the network. Database'll be stored as hashed values to ensure anonymity.

## Technology
The bot use discord.py, and binaries for non-tech users will be released after testing stage.

## Support and feedback
If you have any problem, please create an issue in [issues](https://github.com/git-akihakune/HeartSync-discord/issues) tab, I'll try to fix it as soon as possible.
If you want to contact, make a request, send comments or feedback, you can directly send a message via [the Facebook page](https://www.facebook.com/adaptHeartSync), or through ```/feedback``` function that's going to be implemented later.
If you want to contribute to the project, you can [open a pull request](https://github.com/git-akihakune/HeartSync-discord/pulls) and I'll reply as fast as I can.
If you want to support the project, you can help extending the user base, frequently send user's experience feedback, or just simply send a "Thank you" through the [Facebook page](https://www.facebook.com/adaptHeartSync), I'll be very appreciated!