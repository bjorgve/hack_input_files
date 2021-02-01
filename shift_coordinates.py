import csv

def shift_coordinates(inp, out, shift):
    with open(inp) as csv_file:
        file = list(csv.reader(csv_file, delimiter=" "))
        for row in file:
            if (row[0] == "p" or row[0] == "period"):
                continue
            for i in range(1, len(row)):
                row[i] = float(row[i])
                row[i] += shift
        with open(out, "w") as f:
            writer = csv.writer(f, delimiter=" ")
            writer.writerows(file)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('shift')
    args = parser.parse_args()

    shift_coordinates(args.input, args.output, float(args.shift))
