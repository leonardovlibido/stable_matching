
class Matching:
    def __init__(self, matches=None):
        pass

    def __str__(self):
        pass

    def add_match(self, match):
        pass

    def delete_match(self, match):
        pass

    def is_stable(self, a_ranks, b_ranks):
        pass


class StableMarriageMatcher:
    def __init__(self, men, women):
        pass

    def match(self):
        pass


def main():
    men_ranks = {'abe' : ['ada', 'bea', 'cee'],
                 'ben' : ['bea', 'ada', 'cee'],
                 'che' : ['bea', 'cee', 'ada']}

    women_ranks = {'ada' : ['che', 'ben', 'abe'],
                   'bea' : ['ben', 'abe', 'che'],
                   'cee' : ['che', 'ben', 'abe']
                   }

    matcher = StableMarriageMatcher(men_ranks, women_ranks)
    matches = matcher.match()


if __name__ == "__main__":
    main()
