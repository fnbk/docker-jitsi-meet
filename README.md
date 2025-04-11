# Jitsi Meet on Docker

![](resources/jitsi-docker.png)

[Jitsi](https://jitsi.org/) is a set of Open Source projects that allows you to easily build and deploy secure videoconferencing solutions.

[Jitsi Meet](https://jitsi.org/jitsi-meet/) is a fully encrypted, 100% Open Source video conferencing solution that you can use all day, every day, for free — with no account needed.

This repository contains the necessary tools to run a Jitsi Meet stack on [Docker](https://www.docker.com) using [Docker Compose](https://docs.docker.com/compose/).

All our images are published on [DockerHub](https://hub.docker.com/u/jitsi/).

## Supported architectures

Starting with `stable-7439` the published images are available for `amd64` and `arm64`.

## Tags

These are the currently published tags for all our images:

Tag | Description
-- | --
`stable` | Points to the latest stable release
`stable-NNNN-X` | A stable release
`unstable` | Points to the latest unstable release
`unstable-YYYY-MM-DD` | Daily unstable release
`latest` | Deprecated, no longer updated (will be removed)

## Installation

The installation manual is available [here](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker).

### Kubernetes

If you plan to install the jitsi-meet stack on a Kubernetes cluster you can find tools and tutorials in the project [Jitsi on Kubernetes](https://github.com/jitsi-contrib/jitsi-kubernetes).

## TODO

* Builtin TURN server.


# Florian

```
#
# setup
#

# prepare
sudo rm -fr .jitsi-meet-cfg
mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config,jicofo,jvb,jibri,libretranslate/local,libretranslate/keys}
sudo chown -R 1032:1032 ~/.jitsi-meet-cfg/libretranslate

# start
docker compose -f docker-compose.yml -f transcriber.yml -f vosk.yml -f libretranslate.yml up

# check if libretranslate is properly running:
# * it takes about 5 min to download the language packs (de, en)
# * call API endpoint to see if service is available
curl -X POST http://0.0.0.0:5000/translate -H "Content-Type: application/json" -d '{"q": "Wie gehts?", "source": "de", "target": "en"}'

# visit localhost and accept opening without valid SSL Certificate
https://localhost:8443


#
# demonstrate translation DE -> EN
#

# set conference language to German
Menü: (...) -> Einstellungen -> Mehr -> Sprache: Deutsch

# set subtitles to English
Menü: (...) -> Untertitel einschalten -> English

```