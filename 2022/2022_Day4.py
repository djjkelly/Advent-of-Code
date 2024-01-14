import csv
import codecs

with codecs.open("2022/2022_Day4Raw.csv",'r',encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    count = 0
    for row in csv_reader:
            split_list = row[0].split(",")
            partner1 = split_list[0]
            partner2 = split_list[1]
            partner1_range = partner1.split("-")
            partner2_range = partner2.split("-")
            partner1_sections = set(range(int(partner1_range[0]),int(partner1_range[1])+1))
            partner2_sections = set(range(int(partner2_range[0]),int(partner2_range[1])+1))
            if partner1_sections.issubset(partner2_sections) or partner2_sections.issubset(partner1_sections):
                  count +=1
    print(count)
