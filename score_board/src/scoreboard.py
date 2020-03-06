class Scoreboard:
    def __init__(self):
        # scoreboard: list of tuples with some built-in entries
        self.scoreboard = [("tom", 343), ("rock", 421), ("storm", 122)]
        self.names = set([x[0] for x in self.scoreboard])  # names set, to avoid duplicates
        self.ordering = 0  # ordering flag, 0=original, 1=ascending, 2=descending

    def add_score(self, name, score):
        """adds name, score tuple to scoreboard; checks for duplicated name"""
        if name not in self.names:
            self.scoreboard.append((name, score))
            self.names.add(name)
            return True
        else:
            return False

    def display_scores(self, sort_by=False):
        """displays score depending on sort_by flag, for debugging purposes"""
        if sort_by:
            display = sorted(self.scoreboard, key=lambda x: x[1])
        else:
            display = self.scoreboard
        print("Welcome to our Scoreboard")
        print("Name \t Score")
        for name, score in display:
            print(name + "\t\t" + str(score))


def main():
    """simple main for testing"""
    sb = Scoreboard()
    sb.add_score("abc", 735)
    sb.add_score("rdj", 333)
    sb.display_scores(sort_by=True)
