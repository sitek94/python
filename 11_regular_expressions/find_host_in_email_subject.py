import re

email_subject = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

found_hosts = re.findall('@([^ ]+)', email_subject)
host = found_hosts[0]

print('Host:', host)
