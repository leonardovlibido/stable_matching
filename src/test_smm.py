from stable_marriage_matcher import StableMarriageMatcher
from matching import Matching


def test():
    test_is_stable()


def test_is_stable():
    men_ranks = {'abe': ['ada', 'bea', 'cee'],
                 'ben': ['bea', 'ada', 'cee'],
                 'che': ['bea', 'cee', 'ada']}

    women_ranks = {'ada': ['che', 'ben', 'abe'],
                   'bea': ['ben', 'abe', 'che'],
                   'cee': ['che', 'ben', 'abe']
                   }

    # matcher = StableMarriageMatcher(men_ranks, women_ranks)
    # matches = matcher.match()

    matches = Matching(men_ranks, women_ranks)
    matches.match_pair('abe', 'ada')
    matches.match_pair('ben', 'bea')
    matches.match_pair('che', 'cee')
    assert(matches.is_stable() is True)

    matches = Matching(men_ranks, women_ranks)
    matches.match_pair('abe', 'bea')
    matches.match_pair('ben', 'ada')
    matches.match_pair('che', 'cee')
    assert(matches.is_stable() is False)

    print("OK!")



