import json


def replace_coords(template, output, coords):
    with open(template, "r") as input:
        with open(coords) as coords:
            mrchem = json.load(input)
            mrchem["Molecule"]["coords"] = coords.read()
    with open(output, "w") as output:
        mrchem = json.dump(mrchem, output, indent=2)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('coords')
    args = parser.parse_args()

    replace_coords(args.input, args.output, args.coords)
