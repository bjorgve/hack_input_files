import csv

def scale_coordinates(inp, out, scaling_factor):
    with open(inp) as csv_file:
        file = list(csv.reader(csv_file, delimiter=" "))
        for row in file:
            for i in range(1, len(row)):
                row[i] = float(row[i])
                row[i] *= scale
    with open(out, "w") as f:
        writer = csv.writer(f)
        writer.writerows(file)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('scale')
    args = parser.parse_args()

    scale_coordinates(args.input, args.output, float(args.scale))
