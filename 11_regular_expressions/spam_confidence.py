import re

file = open('../materials/mail_box_short.txt')
values = list()

for line in file:
    line = line.rstrip()
    found_values = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(found_values) == 1:
        value = float(found_values[0])
        values.append(value)

print('Spam Confidence:')
print('Max:', max(values))
print('Avg:', sum(values) / len(values))
