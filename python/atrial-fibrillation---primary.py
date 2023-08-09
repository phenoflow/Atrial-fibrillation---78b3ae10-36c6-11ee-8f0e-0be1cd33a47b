# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"212R.00","system":"readv2"},{"code":"3272.00","system":"readv2"},{"code":"6A9..00","system":"readv2"},{"code":"9hF..00","system":"readv2"},{"code":"9hF1.00","system":"readv2"},{"code":"G573200","system":"readv2"},{"code":"G573300","system":"readv2"},{"code":"G573400","system":"readv2"},{"code":"G573500","system":"readv2"},{"code":"1268","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atrial-fibrillation-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atrial-fibrillation---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atrial-fibrillation---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atrial-fibrillation---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
