# Welcome to Dogfooding for Pyrefly Configs

We're happy you're here. To get started, please run `source setup.sh`.

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
    2. are there any configuration options that do (almost) the same thing. If so,
       does that make things difficult for you?
    3. are there any configuration options that behave differently than what
       you'd expect, either due to their naming or description.
    4. does the documentation's structure make sense?
    5. are there any big questions about how Pyrefly works you have that are unanswered
       by the docs?
