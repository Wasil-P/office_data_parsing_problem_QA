import csv


def write_to_csv(file_path, offices):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Country", "CompanyName", "FullAddress"])
        for office in offices:
            writer.writerow([office.get("Country", ""),
                             office.get("CompanyName", ""),
                             office.get("FullAddress", "")])