from matching import Matching
from collections import deque


class StableMarriageMatcher:
    def __init__(self, men, women):
        self.matching = Matching(men, women)

        pass

    def find_matching(self):
        self.gale_shapley()

    def gale_shapley(self):
        self.matching.unmatch_all()
        free_men = deque(self.matching.matches_men.keys())

        men_proposition_list = {}
        for key in self.matching.matches_men:
            men_proposition_list[key] = 0

        while free_men:
            m = free_men.popleft()
            w = self.matching.men_ranks[m][men_proposition_list[m]]
            men_proposition_list[m] += 1

            if self.matching.woman_is_free(w):
                self.matching.match_pair(m, w)
            elif self.matching.woman_prefers_new_match(w, m):
                old_man = self.matching.matches_women[w]
                self.matching.unmatch_pair(old_man, w)
                free_men.append(old_man)

                self.matching.match_pair(m, w)
            else:
                free_men.append(m)
