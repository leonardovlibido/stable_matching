from stable_marriage_matcher import StableMarriageMatcher
from matching import Matching


def test():
    test_is_stable()
    test_gale_shapley()


def init_preferences():
    men_ranks = {'abe': ['ada', 'bea', 'cee'],
                 'ben': ['bea', 'ada', 'cee'],
                 'che': ['bea', 'cee', 'ada']}

    women_ranks = {'ada': ['che', 'ben', 'abe'],
                   'bea': ['ben', 'abe', 'che'],
                   'cee': ['che', 'ben', 'abe']
                   }
    return men_ranks, women_ranks


def test_gale_shapley():
    men_ranks, women_ranks = init_preferences()

    matcher = StableMarriageMatcher(men_ranks, women_ranks)
    assert(matcher.matching.is_stable() is False)
    matcher.find_matching()
    assert(matcher.matching.is_stable() is True)

    print("gale_shapley: OK!")


def test_is_stable():
    men_ranks, women_ranks = init_preferences()

    matches = Matching(men_ranks, women_ranks)
    assert(matches.is_stable() is False)

    matches.match_pair('abe', 'ada')
    matches.match_pair('ben', 'bea')
    matches.match_pair('che', 'cee')
    assert(matches.is_stable() is True)

    matches = Matching(men_ranks, women_ranks)
    matches.match_pair('abe', 'bea')
    matches.match_pair('ben', 'ada')
    matches.match_pair('che', 'cee')
    assert(matches.is_stable() is False)

    print("is_stable: OK!")



