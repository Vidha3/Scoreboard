"""
We completely understand that not everyone knows Python and Django,
there are many other great languages and frameworks out there.
For that reason, we have created a completely software agnostic challenge for you.
So, what should you do? Say that you have a “Scoreboard service”
which shows the high score of a game. If you’re a frontend developer kind of guy,
could you create a page that lists scores?
- The page must list the name of the player,
as well as the amount of “points” that was scored by the player.
- The list must be sortable by the score.
- At the end of the list, there should be a way for a user
to input more scores into the list.

If you’re more of a backend kind of person, then create the backend
for the frontend described above. If you want to go all out and show us
your crazy full-stack skills, then do both. How you tackle the problem is up to you,
there are no restrictions on the technology (any language + framework is allowed)
that you can use to finish the challenge. Please do not use much time for the problem,
we do not want you to stay up all night coding this. The only requirement is that all
the work should be done in a Git repository.

When you are done zip up the repo or create a git bundle, whichever you prefer.
"""


class Scoreboard:
    def __init__(self):
        self.scoreboard = [("tom", 343), ("rock", 421), ("storm", 122)]
        self.names = set([x[0] for x in self.scoreboard])
        self.ordering = 0

    def add_score(self, name, score):
        if name not in self.names:
            self.scoreboard.append((name, score))
            self.names.add(name)
            return True
        else:
            print("Cannot modify score")
            return False

    def display_scores(self, sort_by=False):
        if sort_by:
            display = sorted(self.scoreboard, key=lambda x: x[1])
        else:
            display = self.scoreboard
        print("Welcome to our Scoreboard")
        print("Name \t Score")
        for name, score in display:
            print(name + "\t\t" + str(score))


def main():
    sb = Scoreboard()
    sb.add_score("abc", 735)
    sb.add_score("rdj", 333)
    sb.display_scores(sort_by=True)


if __name__ == '__main__':
    main()
