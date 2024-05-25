"""
input a CDS query string, use the from_name function to get coordinates and 
return the Galactic Standard of Rest.
"""

import argparse

import astropy.coordinates as coord
import astropy.units as u

import rv_to_gsr as gsr

def query_to_coord(query, radial_velocity):
    return coord.SkyCoord(
        coord.SkyCoord.from_name(query),
        radial_velocity=radial_velocity * u.km / u.s,
        frame="icrs",
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', action='store', type=str, help='CDS name resolver query string.')
    parser.add_argument('--radial_velocity', action='store', type=float, default=-16.1, help='Radial velocity.')
    args = parser.parse_args()

    icrs = query_to_coord(args.query, args.radial_velocity)
    print(gsr.rv_to_gsr(icrs))

if __name__ == "__main__":
    main()
