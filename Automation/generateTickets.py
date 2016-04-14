
#returns {name, email, tickets, hasPaid} taking in a line from tickets form
def splitLine(line):
    name = '';
    email = '';
    tickets = 0;
    hasPaid = '';

    # comma delimited, strip out extra space
    val = [token.strip() for token in line.split(',')]

    name = val[1]
    email = val[2]
    tickets = int (val[4])
    hasPaid = val[6].lower()

    return {
        'name':     val[1],
        'email':    val[2],
        'tickets':  int(val[4]),
        'hasPaid':  val[6].lower()
    }

#returns the email string + email_body
def generateEmail(ticket, currentCount):
    email_to = ticket['email'] + '\n'
    email_greeting = "Dear " + ticket['name'] + ",\n\n";
    email_thank_you = "Thank you for your purchase of tickets to Intandesh's Annual Culture Show! This email is just a confirmation of your purchase. When you get to the door, just tell them the ticket numbers you are redeeming and they will handle the rest. \n\n"
    email_tickets  = "According to our records, you have purchased " + str(ticket['tickets']) + " tickets. You have been assigned the following Ticket Numbers: "

    for i in range(0, ticket['tickets']):
        email_tickets += '#' + str(currentCount + i) + ' '

    email_tickets += "\n\n"

    email_paid = "In addition, you have "

    if "yes" not in ticket['hasPaid']:
        email_paid += "not paid. Please bring either cash or venmo @Nikita-Bhatnagar-1 with you or before the show"
    else:
        email_paid += "paid. "

    email_further = "If you have any further questions, please email aelahi@scu.edu or djhutty@scu.edu. \n\n"
    email_closing = "Peace and Enjoy the Show,\nSCU Intandesh \n \n"

    email = email_to + email_greeting + email_thank_you + email_tickets + email_paid + email_further + email_closing
    return email


tickets_csv = open('tickets.csv', 'r')
emails = open('emails.txt', 'w')

currentCount = 100000

for line in tickets_csv:
    currentTicket = splitLine(line)
    emails.write(generateEmail(currentTicket, currentCount))
    currentCount += currentTicket['tickets']
