class Mailing:
    def __init__(self, from_address, to_address, track, cost):
        self.from_address = from_address
        self.to_address = to_address
        self.track = track
        self.cost = cost

    def __str__(self):
        return (f"""отправление {self.track} из {self.from_address.index},
        {self.from_address.city}, {self.from_address.street},
        {self.from_address.house}, {self.from_address.flat}
        в {self.to_address.index}, {self.to_address.city},
        {self.to_address.street}, {self.to_address.house},
        {self.to_address.flat}, стоимость: {self.cost} рублей""")
