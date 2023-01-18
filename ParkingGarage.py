class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket 

    def takeTicket(self):
        del self.tickets[-1]
        del self.parkingSpaces[-1]
    
    def payForParking(self):
        self.payment = input("Please enter amount to pay now ")
        if self.payment != "":
            self.currentTicket["Paid"] = True
            return "Your ticket has been paid. You have 15 minutes to leave the garage."
        else:
            return ""

    def leaveGarage(self):
        if self.currentTicket["Paid"] == True:
            self.parkingSpaces.append(self.parkingSpaces[-1] + 1)
            self.tickets.append(self.tickets[-1] + 1)
            return "Thank You, have a nice day"

        else:
            self.payment = input("Please enter payment ")
            while self.payment == "":
                self.payment = input("Please enter payment ")
            self.parkingSpaces.append(self.parkingSpaces[-1] + 1)
            self.tickets.append(self.tickets[-1] + 1)
            return "Thank you, have a nice day!"
    
ticketsList = [1, 2, 3]
parkingSpacesList = [101, 202, 303]
ticketStatus = {"Paid": False}

newGarage = ParkingGarage(ticketsList, parkingSpacesList, ticketStatus)

def run():
    print("Ticket taken")

    newGarage.takeTicket()

    print("Ticket amount decreased:", newGarage.tickets)

    print("Parking spaces decreased:", newGarage.parkingSpaces)

    print("Paid status:", newGarage.currentTicket)

    pay = newGarage.payForParking()

    while pay == "":
        pay = newGarage.payForParking()
    
    print("New Paid Status:", newGarage.currentTicket)

    print(newGarage.leaveGarage())

    print("Ticket amount changed:", newGarage.tickets)

    print("Parking spaces changed:", newGarage.parkingSpaces)

run()