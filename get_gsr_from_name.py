"""
Input a star, use the from name function to get coordinates and return the Galactic Standard of Rest.

Uses the example from:
https://docs.astropy.org/en/latest/generated/examples/coordinates/rv-to-gsr.html#convert-a-radial-velocity-to-the-galactic-standard-of-rest-gsr
"""

import argparse
import astropy.coordinates as coord
import astropy.units as u

coord.galactocentric_frame_defaults.set("latest")

def rv_to_gsr(c, v_sun=None):
    """Transform a barycentric radial velocity to the Galactic Standard of Rest
    (GSR).

    The input radial velocity must be passed in as a

    Parameters
    ----------
    c : `~astropy.coordinates.BaseCoordinateFrame` subclass instance
        The radial velocity, associated with a sky coordinates, to be
        transformed.
    v_sun : `~astropy.units.Quantity`, optional
        The 3D velocity of the solar system barycenter in the GSR frame.
        Defaults to the same solar motion as in the
        `~astropy.coordinates.Galactocentric` frame.

    Returns
    -------
    v_gsr : `~astropy.units.Quantity`
        The input radial velocity transformed to a GSR frame.

    """
    if v_sun is None:
        v_sun = coord.Galactocentric().galcen_v_sun.to_cartesian()

    gal = c.transform_to(coord.Galactic)
    cart_data = gal.data.to_cartesian()
    unit_vector = cart_data / cart_data.norm()

    v_proj = v_sun.dot(unit_vector)

    return c.radial_velocity + v_proj

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', action='store', type=str, help='CDS name resolver query string.')
    args = parser.parse_args()

    icrs = coord.SkyCoord(
        coord.SkyCoord.from_name(args.name),
        radial_velocity=-16.1 * u.km / u.s,
        frame="icrs",
    )

    rv_gsr = rv_to_gsr(icrs)
    print(rv_gsr)

if __name__ == "__main__":
    main()
