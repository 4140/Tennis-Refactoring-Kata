"""Tennis kata Version 1."""
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
    """Tennis game kata."""

    def __init__(self, player_1_name: str, player_2_name: str) -> None:
        self.player_1 = Player(name=player_1_name)
        self.player_2 = Player(name=player_2_name)

    def won_point(self, player_name: str) -> None:
        """Score point for `player_name`."""
        if player_name == self.player_1.name:
            self.player_1.score += 1
        else:
            self.player_2.score += 1

    def score(self):
        """Get current score."""
        score_counter = ScoreCounter(self.player_1, self.player_2)
        result = score_counter.get_score()
        return result


class Player(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0

    @property
    def verbose_score(self) -> str:
        return SCORE_MAP[self.score]


class ScoreCounter(object):
    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def get_score(self) -> str:
        """Get current score."""
        return self._compare_scores()

    def _compare_scores(self) -> str:
        return self._check_tie()

    def _check_tie(self) -> str:
        if (self.player_1.score == self.player_2.score):
            return TIE_MAP.get(self.player_1.score, "Deuce")

        return self._check_lead()

    def _check_lead(self) -> str:
        leader = max(self.player_1, self.player_2, key=attrgetter('score'))
        other = min(self.player_1, self.player_2, key=attrgetter('score'))

        if (leader.score >= 4):
            diff = leader.score - other.score
            if (diff == 1):
                return f"Advantage {leader.name}"
            elif (diff >= 2):
                return f"Win for {leader.name}"

        return self._default()

    def _default(self) -> str:
        return f"{self.player_1.verbose_score}-{self.player_2.verbose_score}"
