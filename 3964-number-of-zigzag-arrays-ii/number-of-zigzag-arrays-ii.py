
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Transition matrix
        A = [[0] * m for _ in range(m)]

        for x in range(m):
            for z in range(m):
                if z > m - 1 - x:
                    A[x][z] = 1

        # Initial DP for arrays of length 2
        dp = list(range(m))

        def mat_vec(mat, vec):
            size = len(vec)
            res = [0] * size

            for i in range(size):
                res[i] = sum(mat[i][j] * vec[j] for j in range(size)) % MOD

            return res

        def mat_mul(a, b):
            size = len(a)
            res = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if a[i][k]:
                        val = a[i][k]
                        for j in range(size):
                            if b[k][j]:
                                res[i][j] += val * b[k][j]

                for j in range(size):
                    res[i][j] %= MOD

            return res

        # Apply A^(n-2) to dp using binary exponentiation
        power = n - 2

        while power > 0:
            if power & 1:
                dp = mat_vec(A, dp)

            power >>= 1

            if power:
                A = mat_mul(A, A)

        # up and down counts are symmetric
        return (2 * sum(dp)) % MOD
