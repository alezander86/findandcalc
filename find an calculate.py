import csv
import pandas as pd

my_file_name = "11.csv" 
my_file_name2 = "22.csv" 
cleaned_file = "out1.csv" #файл вывода
cleaned_file2 = "out2.csv" #файл вывода
remove_words = ['Отклонен', 'Договор №']

f = open(cleaned_file, "w")
with open(my_file_name, "r", newline="") as file:
    for row in file:
        a = row.split(';')
        f.write(a[0] + ';' + a[5] + '\n')
f.close()
f = open(cleaned_file, "a")
with open(my_file_name2, "r", newline="") as file:
    for row in file:
        a = row.split(';')
        f.write(a[1] + ';' + a[3] + '\n')
f.close()
with open(cleaned_file, 'r', newline='') as infile, \
     open(cleaned_file2, 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=';')
    for line in csv.reader(infile, delimiter=';'):
        if not any(remove_word in line for remove_word in remove_words):
            writer.writerow(line)

file = pd.read_csv('out2.csv', encoding="windows-1251", delimiter=';')
print(file.groupby(file['Номер договора'].str[:4])['Фамилия И.О.'].nunique())
