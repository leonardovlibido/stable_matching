from stable_marriage_matcher import StableMarriageMatcher


def test():
    men_ranks = {'abe' : ['ada', 'bea', 'cee'],
                 'ben' : ['bea', 'ada', 'cee'],
                 'che' : ['bea', 'cee', 'ada']}

    women_ranks = {'ada' : ['che', 'ben', 'abe'],
                   'bea' : ['ben', 'abe', 'che'],
                   'cee' : ['che', 'ben', 'abe']
                   }

    matcher = StableMarriageMatcher(men_ranks, women_ranks)
    matches = matcher.match()
    print(matches)

