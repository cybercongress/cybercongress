
Current wiki is built on top of [mkdocs.org](http://mkdocs.org) engine with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) extensions pack.


## Required Installations

* https://hub.docker.com/r/squidfunk/mkdocs-material/


## Commands Cheat Sheet

* `docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material`
* `docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build`
* `docker run --rm -it -v ~/.ssh:/root/.ssh -v ${PWD}:/docs squidfunk/mkdocs-material gh-deploy`

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
