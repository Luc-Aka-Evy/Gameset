"""Define a tour/round model"""


class Tour:
    """Tour
    A tour:
     -has a match list to record all the match of the round
     -a name(ex: Round 1)
     -the date/time of the beginning and the end
    """

    def __init__(self, match_list, name, beginning_time="", ending_time=""):
        """Tour model"""
        self.match_list = match_list
        self.name = name
        self.beginning_time = beginning_time
        self.ending_time = ending_time

    def __repr__(self):
        """Use in print"""
        return f"{self.name}" \
               f" Matchs:{self.match_list}" \
               f" Début:{self.beginning_time}" \
               f" Fin:{self.ending_time}"

    def serialized_tour(self):
        return {
            "name": self.name,
            "match list": str(self.match_list),
            "start": self.beginning_time,
            "end": self.ending_time,
        }

    def show_match(self):
        return self.match_list
