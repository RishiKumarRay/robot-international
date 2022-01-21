<p align="center">
  <a aria-label="Pico logo" href="https://intern.gnztmpz.eu.org">
    <img src="frontend/static/landing/img/meeseeks.png" />
  </a>
</p>

<p align="center">
  <em>Warung International and Wholesomeland Discord Server Bots</em>
</p>

<p align="center">
  <a
    href="https://intern.gnztmpz.eu.org"
  >Wiki</a>
  |
  <a
    href="https://bot.gnztmpz.eu.org/"
  >Website</a>
</p>

<p align="center">
  Robot International is a Discord Bot that have all tools you need from managing a server, engage with server members, and more...
</p>

<p align="center">
  <a href="https://bot.gnztmpz.eu.org/">Robot International</a>
</p>

<hr>

[![Warung International](https://img.shields.io/discord/922523614828433419.svg?logo=discord)](https://discord.gg/warung-international) ![Wholesomeland](https://img.shields.io/discord/806949608349106197.svg?logo=discord) [![Build Production](https://github.com/wholesomeland/robot-international/actions/workflows/build-prod.yml/badge.svg)](https://github.com/wholesomeland/robot-international/actions/workflows/build-prod.yml) [![Build Documentations](https://github.com/wholesomeland/robot-international/actions/workflows/build-docs.yml/badge.svg)](https://github.com/wholesomeland/robot-international/actions/workflows/build-docs.yml) [![Lint](https://github.com/wholesomeland/robot-international/actions/workflows/lint.yml/badge.svg)](https://github.com/wholesomeland/robot-international/actions/workflows/lint.yml) [![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Robot International Discord Server Bots
This monorepo contains the web services, bot services, and documentation for Robot International

> This is a merging bots of Wholesomeland Discord Server Bots and Warung International Discord Server Bots, written in Nextcord

## Overview

- `docs/` Wiki documentation for Robot International in [DocFX](https://dotnet.github.io/docfx) (Markdown) format.
- `frontend/` [Flask](https://flask.palletsprojects.com/) app for the https://bot.gnztmpz.eu.org site.
- `bot/` *The heart of this Project.* The bot itself, written in [Nextcord](https://nextcord.readthedocs.io)

## Frontend Development

To work on the frontend, you mostly only need to focus on the `frontend/` directory. Run `pip` commands in there such as `pip install -r requirements.txt`. See the readme file in there for more details.

## Bot Development

When working on the bot, you mostly only need to focus on the `bot/` directory. The server application will assume it's being run from the root, _not_ from within `bot/`. See the readme file in there for more details.

## Documentations

We're using [DocFX](https://dotnet.github.io/docfx) for Documenting things. See the readme file in there for more details.