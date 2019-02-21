import sys


class Matching:
    def __init__(self, men_ranks, women_ranks):
        self.men_ranks = men_ranks
        self.women_ranks = women_ranks

        self.matches_men = {}
        self.matches_women = {}

        for key in self.men_ranks:
            self.matches_men[key] = None
        for key in self.women_ranks:
            self.matches_women[key] = None

    def unmatch_all(self):
        for key in self.men_ranks:
            self.matches_men[key] = None
        for key in self.women_ranks:
            self.matches_women[key] = None

    def str_matches_men(self):
        return "\n".join([str(el) + " : " + str(self.matches_men[el]) for el in self.matches_men])

    def str_matches_women(self):
        return "\n".join([str(el) + " : " + str(self.matches_women[el]) for el in self.matches_women])

    def __str__(self):
        return self.str_matches_men() + "\n\n" + self.str_matches_women()

    def match_pair(self, man, woman):
        if man in self.matches_men and woman in self.matches_women:
            self.matches_men[man] = woman
            self.matches_women[woman] = man
        else:
            sys.exit("Given name is not in the matching")

    def unmatch_pair(self, man, woman):
        if man not in self.matches_men or woman not in self.matches_women:
            sys.exit("Given name is not in the matching")
        if self.matches_men[man] != woman or self.matches_women[woman] != man:
            sys.exit("Given pair is not matched")

        self.matches_men[man] = None
        self.matches_women[woman] = None

    def man_rank_of_match(self, man):
        if self.matches_men[man] is not None:
            return self.men_ranks[man].index(self.matches_men[man])
        else:
            return -1

    def man_rank_of_woman(self, man, woman):
        return self.men_ranks[man].index(woman)

    def woman_rank_of_man(self, woman, man):
        return self.women_ranks[woman].index(man)

    def woman_rank_of_match(self, woman):
        if self.matches_women[woman] is not None:
            return self.women_ranks[woman].index(self.matches_women[woman])
        else:
            return -1

    def is_complete(self):
        return None not in self.matches_men.values()

    def is_stable(self):
        if not self.is_complete():
            return False

        for man in self.matches_men:
            match_rank = self.man_rank_of_match(man)
            man_ranks = self.men_ranks[man][:match_rank]
            for woman in man_ranks:
                if self.woman_rank_of_match(woman) > self.woman_rank_of_man(woman, man):
                    return False
        return True
