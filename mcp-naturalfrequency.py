from mcp.server.fastmcp import FastMCP
from math import inf
from naturalfrequency import general_beam_natural_frequency

mcp = FastMCP("beam_frequency")

@mcp.tool()
async def simple_beam_frquency(beamtype: str,rhoA: float,EI: 
                         float,length: float,) -> float:
    """Calcuate the natural angular frequency of a beam.

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

@mcp.tool() 
async def beam_frquency(rhoA: float,EI: float,length: float, 
                         linearsprings: tuple[float | str, float | str],
                         torsionalsprings: tuple[float | str, float | str]) -> float:
    """Calcuate the natural angular frequency of a beam,
    with linear and torsional springs at the beginning and end of the beam.

    Args:
        rhoA (float): Mass per unit length.
        EI (float): Bending stiffness.
        length (float): Length of beam.
        linearsprings (tuple[float,float]): Linear springs at the beginning and end of the beam.
            - 0 for no spring
            - inf for fixed end
        Torsionalsprings (tuple[float,float]): Torsional springs at the beginning and end of the beam.
            - 0 for no spring
            - inf for fixed end
    """
    K1, K2 = linearsprings
    C1, C2 = torsionalsprings

    if isinstance(K1, str) and 'inf' in K1.lower():
        K1=inf
    if isinstance(K2, str) and 'inf' in K2.lower():
        K2=inf
    if isinstance(C1, str) and 'inf' in C1.lower():
        C1=inf
    if isinstance(C2, str) and 'inf' in C2.lower():
        C2=inf

    k1 = K1*length**3/EI
    k2 = K2*length**3/EI
    c1 = C1*length/EI
    c2 = C2*length/EI

    
    if k1 < 0.:
        raise ValueError("Invalid value for linear spring at the beginning. Choose from 0, inf or positive values.")
    elif k1 < 1.:
        k_1 = (k1, 1.)
    else:
        k_1 = (1., 1/k1)
    #
    if k2 < 0.:
        raise ValueError("Invalid value for linear spring at the end. Choose from 0, inf or positive values.")
    elif k2 < 1.:
        k_2 = (k2, 1.)
    else:
        k_2 = (1., 1/k2)
    #
    if c1 < 0.:
        raise ValueError("Invalid value for torsional spring at the beginning. Choose from 0, inf or positive values.")
    elif c1 < 1.:
        c_1 = (c1, 1.)
    else:
        c_1 = (1., 1/c1)
    #
    if c2 < 0.:
        raise ValueError("Invalid value for torsional spring at the end. Choose from 0, inf or positive values.")
    elif c2 < 1.:
        c_2 = (c2, 1.)
    else:
        c_2 = (1., 1/c2)
    
    eps = general_beam_natural_frequency(k_1,k_2,c_1,c_2)

    return eps**2/length**2 * (EI/rhoA)**0.5

    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")