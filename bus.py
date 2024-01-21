class Bus:
    def __init__(self, route_number, destination) -> None:
        self.route_number = route_number
        self.destination = destination
        self.passengers = list()

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)
    
    def empty_bus(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.clear()