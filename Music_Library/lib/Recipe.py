class Recipe:
    def __init__(self, id, names, average_cooking_time, rating_one_to_five):
        self.id = id
        self.names = names
        self.average_cooking_time = average_cooking_time
        self.rating_one_to_five = rating_one_to_five

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Recipe({self.id}, {self.names}, {self.average_cooking_time}, {self.rating_one_to_five})"