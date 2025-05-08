from mcp.server.fastmcp import FastMCP
from math import pi
from pydantic import Field

mcp = FastMCP("civil_test")

@mcp.tool()
async def eigenfrequency(beamtype: str,rhoA: float,EI: 
                         float,length: float,) -> float:
    """Calcuate the eigenfrequency of a system.

    Args:
        beamtype (str): Type of beams: 
            - "cantilever" for cantilever beam
            - "simply_supported" for simply supported beam
            - "popped_cantilever" for popped cantilever beam
            - "fixed" for fixed beam
        rhoA (float): Mass per unit length.
        EI (float): Bending stiffness.
        length (float): Length of beam.
    """
    omega_0 = 1/length**2 * (EI/rhoA)**0.5
    if beamtype == "cantilever":
        return 3.516 * omega_0
    elif beamtype == "simply_supported":
        return 9.870 * omega_0
    elif beamtype == "popped_cantilever":
        return 15.418 * omega_0
    elif beamtype == "fixed":
        return 22.373 * omega_0
    else:
        raise ValueError("Invalid type. Choose from 'cantilever', " \
        "'simply_supported', 'popped cantilever', or 'fixed'.")
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")