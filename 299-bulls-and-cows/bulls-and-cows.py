
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        count = [0] * 10

        for s, g in zip(secret, guess):

            # Same digit at the same position
            if s == g:
                bulls += 1
            else:
                # Check whether this secret digit
                # was previously present in the guess
                if count[int(s)] < 0:
                    cows += 1

                # Check whether this guess digit
                # was previously present in the secret
                if count[int(g)] > 0:
                    cows += 1

                count[int(s)] += 1
                count[int(g)] -= 1

        return str(bulls) + "A" + str(cows) + "B"
