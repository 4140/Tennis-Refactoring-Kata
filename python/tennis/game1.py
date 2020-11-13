class TennisGame1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        temp_score = 0
        if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points >= 4 or self.p2points >= 4):
            minus_result = self.p1points-self.p2points
            if (minus_result == 1):
                result = "Advantage " + self.player_1_name
            elif (minus_result == -1):
                result = "Advantage " + self.player_2_name
            elif (minus_result >= 2):
                result = "Win for " + self.player_1_name
            else:
                result = "Win for " + self.player_2_name
        else:
            for i in range(1, 3):
                if (i == 1):
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
