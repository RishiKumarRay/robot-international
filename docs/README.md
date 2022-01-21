<p align="center">
  <a aria-label="Pico logo" href="https://intern.gnztmpz.eu.org">
    <img src="images/RobotIntern.png" />
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
    href="https://msft-prod.herokuapp.com/"
  >Leaderboards</a>
</p>

<p align="center">
  Robot International is a Discord Bot that hangs around in the Warung International and Wholesomeland Discord Servers.
</p>

<p align="center">
  <a href="https://msft-prod.herokuapp.com/">Robot International</a>
</p>

<hr>

[![build-frontend](https://github.com/wholesomeland/docs-new/actions/workflows/build.yml/badge.svg)](https://github.com/wholesomeland/docs-new/actions/workflows/build.yml) [![pages-build-deployment](https://github.com/wholesomeland/docs-new/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/wholesomeland/docs-new/actions/workflows/pages/pages-build-deployment)

## Development

### Requirements:

- Chocolatey/Homebrew
- Git
- [DocFX](https://dotnet.github.io/docfx/index.html)

### Setup

```bash
# Install DocFX with Chocolatey
choco install docfx -y

# OR, Use Homebrew (skip this if you already install with chocolatey)
brew install docfx

# Clone the Project
git clone https://github.com/wholesomeland/docs-new.git

# Open the Project Directory
cd /path/to/project

# Start the server
docfx docfx.json --serve
```

By default the development server will run on `http://localhost:8080`.