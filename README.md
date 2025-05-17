# Beam Frequency MCP Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction)  server that provides tools for calculating the natural angular frequencies of beams with various boundary conditions and spring supports.

This is a little project to learn how to use MCP-Server

## Overview

This server provides two main tools for structural dynamics calculations:
1. Simple beam configurations (cantilever, simply supported, etc.)
2. General beam configurations with arbitrary linear and torsional spring supports

## Installation

### Prerequisites
- Python 3.7+
- `mcp` library
- `naturalfrequency` library

### Setup
1. Clone this repository
2. Create enviroment and install dependencies with `uv` ([fast Python package and project manager](https://docs.astral.sh/uv/)):
````
uv sync
````
3. Adding the Server to the `config.json` of the used MCP-Client file:
  - for MacOS
````json
{
  "mcpServers": {
    "naturalfrequency": {
        "command": "/Users/USERNAME/.local/bin/uv",
        "args": [
            "--directory",
            "/PATH/TO/MCP/SERVER/mcp-naturalfrequency",
            "--project",
            "/PATH/TO/MCP/SERVER/mcp-naturalfrequency/.venv",
            "run",
            "mcp-naturalfrequency.py"
        ]
    }
  }
}
````
  - for Windows:
````json
{
  "mcpServers": {
    "naturalfrequency": {
        "command": "uv",
        "args": [
            "--directory",
            "C:\\PATH\\TO\\MCP\\SERVER\\mcp-naturalfrequency",
            "run",
            "mcp-naturalfrequency.py"
        ]
    }
  }
}
````


## Available Tools

### 1. Simple Beam Frequency (`simple_beam_frquency`)

Calculates the natural angular frequency for standard beam configurations.

- cantilever beam
- simply supported beam
- popped cantilever beam
- fixed beam

### 2. General Beam Frequency (`beam_frquency`)

Calculates the natural angular frequency for beams with arbitrary linear and torsional spring supports at the ends.

## Mathematical Background

The calculations are based on the Euler-Bernoulli beam theory. The natural frequency is determined by solving the characteristic equation for the given boundary conditions.

For simple beams, the frequency is calculated as:

$$
ω = \frac{λ^2}{L^2}  \sqrt{\frac{EI}{ρA}}
$$

Where $\lambda$ is a coefficient specific to each boundary condition:
- Cantilever: $\lambda$ = 3.516
- Simply supported: $\lambda$ = 9.870
- Popped cantilever: $\lambda$ = 15.418
- Fixed-fixed: $\lambda$ = 22.373

For general beams with spring supports, the calculation involves solving a more complex characteristic equation using the `general_beam_natural_frequency` function.

## Error Handling

The server includes input validation and will raise appropriate errors for:
- Invalid beam types
- Negative spring values
- Invalid parameter types

## Integration with MCP

This server uses the FastMCP framework and communicates via stdio transport. It can be integrated with any MCP-compatible client application.

## Tested

The server has been tested with [Claude 3.7 Sonnet](https://www.anthropic.com/claude/sonnet) on [Claude Desktop](https://claude.ai/download) on a Macbook with an Apple M2 and 24GB mamory. This setup works very well.

Also the server was tested with [Ollama](https://ollama.com/) and the terminal programm [oterm](https://github.com/ggozad/oterm). As model [Qwen3:4b](https://qwenlm.github.io/blog/qwen3/) was used. The system was a laptop with Windows 11, an Intel Core i7 3.40GHz and a NVIDIA GeForce GTX 1650. The setup worked but the local model where slow (because of the Hardware) and not as powerfull as Claude but for a local model with only laptop hardware it is very good.