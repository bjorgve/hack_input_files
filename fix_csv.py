
def fix_csv(input, output):
    with open(input, 'r') as input_file:
        with open(output, 'w') as output_file:
            for line in input_file:
                output_file.write(" ".join(line.split()) + "\n" )

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    fix_csv(args.input, args.output)
