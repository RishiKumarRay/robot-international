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