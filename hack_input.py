import csv

def hack_input(hack):
    with open(hack) as csv_file:
        file = list(csv.reader(csv_file, delimiter=" "))
        top = 0.0
        for row in file:
            if row[0] == "period":
                top = float(row[1])/2.0
                continue
            for i in range(1, len(row)):
                row[i] = float(row[i])
                row[i] += top
    with open("out_lif_corner.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerows(file)


if __name__ == '__main__':
    hack_input("lif_orig.in")
