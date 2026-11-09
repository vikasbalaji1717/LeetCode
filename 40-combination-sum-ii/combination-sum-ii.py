
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()

        result = []
        path = []

        def backtrack(start, remaining):

            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if number is too large
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # i + 1 ensures each candidate is used only once
                backtrack(i + 1, remaining - candidates[i])

                path.pop()

        backtrack(0, target)

        return result
