# Welcome to Dogfooding for Pyrefly Configs

We're happy you're here. To get started, please run `./setup.sh`, and then
`source venv/bin/activate`.

This will install `Pyrefly` for you. We're going to walk through a few steps, which
should put you into a few different configuration situations.

As a reminder, you can find the [documentation here](https://pyrefly.org/en/docs/configuration/).

## Steps

1. Try to perform a type check with Pyrefly. Use the `--help` output to figure out what's going on.
    a. Try to just get output from `main.py`
    b. Try to get output from everything but `test` directories.
2. Try to add a configuration and use it to get this project to type check cleanly,
without actually fixing the type errors.
Don't forget that you have access to the
[documentation here](https://pyrefly.org/en/docs/configuration/). As you work through
this, think through the following questions:
    1. are there any configuration options that confuse you?
    2. are there any configuration options that do (almost) the same thing
    3. are there any configuration options that behave differently than what
       you'd expect, either due to their naming or description.
