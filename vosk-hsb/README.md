# Vosk HSB - Speech to Text

This is a containerized Speech to Text model which is used to transcribe Upper Sorbian (HSB) for the jitsi meet setup.

Browse on GitHub:
* https://github.com/fnbk/mudrowak/tree/fix/use-explicit-versions

Original source of the whisper model (HSB):
* https://huggingface.co/spaces/Korla/hsb_stt_demo (Jul 14, 2023)


# Getting Started

```
# checkout repository
git clone git@github.com:fnbk/mudrowak.git

# checkout specific branch
cd mudrowak/
git checkout fix/use-explicit-versions

# submodules
# * double check that 'git submodule update' command succeeds! 
# * takes about 5min
git --no-pager submodule status
git submodule update --init --recursive

# download git-lfs files
cd hsb_stt_demo
git lfs pull
cd ..
cd whisper-small
git lfs pull
cd ..


# build docker image
docker build -f docker_vosk/vosk_server_whisper/full-vosk-whisper-stack.Dockerfile -t fnbk/vosk-hsb:250508 .

```

