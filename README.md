# Beam Frequency MCP Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction)  server that provides tools for calculating the natural angular frequencies of beams with various boundary conditions and spring supports.

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
2. Create enviroment and install dependencies:
3. Adding the Server to the `config.json` file:
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

<!--  
## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
-->
## Support

For issues or questions, please [add contact information or issue tracker link]