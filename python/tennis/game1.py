from operator import attrgetter

SCORE_MAP = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
TIE_MAP = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}


class TennisGame1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1 = Player(name=player_1_name)
        self.player_2 = Player(name=player_2_name)

    def won_point(self, player_name):
        if player_name == self.player_1.name:
            self.player_1.score += 1
        else:
            self.player_2.score += 1

    def score(self):
        score_counter = ScoreCounter(self.player_1, self.player_2)
        result = score_counter.get_score()
        return result


class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    @property
    def verbose_score(self):
        return SCORE_MAP.get(self.score)


class ScoreCounter(object):
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def get_score(self):
        return self._compare_scores()

    def _compare_scores(self):
        return self._check_tie()

    def _check_tie(self):
        if (self.player_1.score == self.player_2.score):
            return TIE_MAP.get(self.player_1.score, "Deuce")

        return self._check_lead()

    def _check_lead(self):
        leader = max(self.player_1, self.player_2, key=attrgetter('score'))
        other = min(self.player_1, self.player_2, key=attrgetter('score'))

        if (leader.score >= 4):
            diff = leader.score - other.score
            if (diff == 1):
                return f"Advantage {leader.name}"
            elif (diff >= 2):
                return f"Win for {leader.name}"

        return self._default()

    def _default(self):
        return f"{self.player_1.verbose_score}-{self.player_2.verbose_score}"
