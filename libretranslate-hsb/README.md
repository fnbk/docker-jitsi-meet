# Libretranslate HSB

This is a containerized upper sorbian translation model that is used to translate DE -> HSB in the jitsi meet setup.

Browse on GitHub:
* https://github.com/fnbk/modele/tree/fix/use-explicit-versions

Original source:
* https://github.com/WitajSotra/modele/

# Getting Started

```
# checkout repository
git clone git@github.com:fnbk/modele.git

# checkout specific branch
cd modele/
git checkout fix/use-explicit-versions

# download git-lfs files
git lfs pull

# build docker image
docker build -f ctranslate-ol/Dockerfile -t fnbk/libretranslate-hsb:250508 ctranslate-ol/

```



