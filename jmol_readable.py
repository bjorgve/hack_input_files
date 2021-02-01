import csv


def jmol_readable(input, output, period):
    with open(input) as file:
        new_lines = []
        for i in range(0, 3):
            tmp_list = ["lattice_vector", 0.0, 0.0, 0.0]
            tmp_list[i+1] = period
            new_lines.append(tmp_list)

        for line in file:
            tmp_line = line.split()
            new_lines.append(["atom"] + tmp_line[1:] + [tmp_line[0]])
        with open(output, "w") as geo_file:
            writer = csv.writer(geo_file, delimiter=" ")
            writer.writerows(new_lines)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('period')
    args = parser.parse_args()

    jmol_readable(args.input, args.output, args.period)
