# Assuming that email has title that looks like this:
# "From steve.griffin@family.guy.com Sat Jan 10 12:15:32 2008"

def get_email_host_from_email_title(email):
    at_pos = email.find('@')

    # Start looking for " " from "@" sign position
    space_pos = email.find(' ', at_pos)

    host = email[at_pos + 1:space_pos]

    print(host)


get_email_host_from_email_title('From steve.griffin@family.guy.com Sat Jan 10 12:15:32 2008')
