class TicketList:
    def __init__(self, code, destination, no_of_ticket):
        self.code = code
        self.name = ""
        self.destination = destination
        self.no_of_ticket = no_of_ticket
        self.price = 0
        self.calc_price = 0

    def get_price(self):
        return self.price

    def set_price(self, amnt):
        self.price = amnt

    def set_no_of_ticket(self):
        return self.no_of_ticket

    def set_destination(self):
        return self.destination

    def code_list(self):
        if self.code == "TR69420":
            self.name = "KAI Jakarta"

        elif self.code == "JY43987":
            self.name = "KAI Jakarta"

        elif self.code == "KR19832":
            self.name = "KAI Jakarta"

    def price_list(self):
        if self.destination == "Bandung":
            self.set_price(35)
        elif self.destination == "Cirebon":
            self.set_price(15)
        elif self.destination == "Malang":
            self.set_price(15)
        elif self.destination == "Semarang":
            self.set_price(13)
        elif self.destination == "Surabaya":
            self.set_price(16)
        elif self.destination == "Yogyakarta":
            self.set_price(22)

    def tick_cost(self):
        self.price_list()
        self.code_list()
        self.calc_price = self.price * self.no_of_ticket
        return self.calc_price


def show_dest():
    destinations = ["Bandung", "Cirebon", "Malang", "Semarang", "Surabaya", "Yogyakarta"]
    print("List of destinations:")
    for dest in destinations:
        print(f"- {dest}")

def show_code():
    train_codes = ["TR69420", "JY43987", "KR19832"]
    print("List of train codes:")
    for code in train_codes:
        print(f"- {code}")

def ticket_cart():
    tickets_ordered = int(input("How many tickets will you order today? "))
    while tickets_ordered < 1:
        print("Number of items must be at least 1 ticket.")
        tickets_ordered = int(input("How many tickets will you order today? "))
    list_of_orders = []
    for i in range(tickets_ordered):
        print(f"Ticket #{i+1}-")
        show_code()
        name_of_train = input("What is your train code? : ")
        show_dest()
        dest = input("Where would you like to go? : ")
        tick_amnt = int(input("How many of these tickets do you want to buy? : "))
        ticket = TicketList(name_of_train, dest, tick_amnt)
        print("")
        list_of_orders.append(ticket)
    return list_of_orders


def ticket_display(list_of_orders):
    print("Here's a summary of the tickets purchased:")
    print("Train Code\t\tTrain Name\t\tTickets ordered\t\tDestination\t\t\tPrice/ticket\t\tPrice/order")
    print("--------------------------------------------------------------------------------------")
    for i in range(len(list_of_orders)):
        list_of_orders[i].tick_cost()
        print(f"{list_of_orders[i].code}\t\t\t{list_of_orders[i].name}\t\t{list_of_orders[i].no_of_ticket}\t\t\t\t\t{list_of_orders[i].destination}\t\t\t${list_of_orders[i].get_price():.2f}\t\t\t\t${list_of_orders[i].tick_cost():.2f}")


def total_cost_calc(list_of_orders):
    total_cost = 0
    for i in range(len(list_of_orders)):
        total_cost += list_of_orders[i].tick_cost()
    return total_cost


def mainTickets():
    full_list = ticket_cart()
    ticket_display(full_list)
    print(f"Total cost: ${total_cost_calc(full_list):.2f}")

mainTickets()
