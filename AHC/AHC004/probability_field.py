import numpy as np


class ProbabilityField(object):

    def __init__(self, n=20, d=8, max_l=12):
        self.n = n
        self.d = d
        self.max_l = max_l
        self.probability = np.ones((n, n, d), dtype=np.float16) / d
        self.count = np.zeros((n, n, d), dtype=np.float16)
        self.extend_probability = np.ones((2 * n, 2 * n, d), dtype=np.float16) / d
        self.d_roll = np.zeros((n, n, 2, max_l, d))
        self.update_roll_tensor()

    def update_roll_tensor(self):
        self.extend_probability[:self.n, :self.n, :] = self.probability
        self.extend_probability[self.n:, :self.n, :] = self.probability
        self.extend_probability[:self.n, self.n:, :] = self.probability
        self.extend_probability[self.n:, self.n:, :] = self.probability

        for k in range(self.max_l):
            self.d_roll[:, :, 0, k, :] = self.extend_probability[:self.n, k:(self.n + k), :]
            self.d_roll[:, :, 1, k, :] = self.extend_probability[k:(self.n + k), :self.n, :]

    def random_accept(self, w_array, t):
        """
        :param w_array: input word, 0-1 array(float16) with shape (max_l, d, m)
        :param t: temperature
        :return:
        """
        assert w_array.shape[0] <= self.n
        assert w_array.shape[1] == self.d

        self.extend_probability *= 0

        res_d = np.tensordot(np.log(self.d_roll), w_array, axes=([3, 4], [0, 1]))
        distance = 0.0
        judge_d = np.exp(res_d / t)

        for p in range(w_array.shape[2]):

            q = np.random.choice(self.n * self.n * 2, p=judge_d[:, :, :, p].flatten() / judge_d[:, :, :, p].sum())
            d = q % 2
            q = q // 2
            j = q % self.n
            i = q // self.n
            if d == 0:
                self.extend_probability[i, j:(j + self.max_l), :] += w_array[:, :, p]
            else:
                self.extend_probability[i:(i + self.max_l), j, :] += w_array[:, :, p]

            distance += res_d[i, j, d, p]

        # print(-distance / w_array.shape[2])

        self.probability *= 0
        self.probability += self.extend_probability[:self.n, :self.n, :]
        self.probability += self.extend_probability[self.n:, :self.n, :]
        self.probability += self.extend_probability[:self.n, self.n:, :]
        self.probability += self.extend_probability[self.n:, self.n:, :]
        self.probability = np.maximum(self.probability, 0.05)
        self.probability /= self.probability.sum(axis=2, keepdims=True)

        # print(self.probability.max())

        self.update_roll_tensor()

        # print(self.probability)
        # print(self.evaluate(w_array))
        return None

    def strict_weighted_accept(self, w_array, c):
        """
        :param w_array: input word, 0-1 array(float16) with shape (max_l, d, m)
        :param t: temperature
        :return:
        """
        assert w_array.shape[0] <= self.n
        assert w_array.shape[1] == self.d

        self.extend_probability *= 0

        res_d = np.tensordot(np.log(self.d_roll), w_array, axes=([3, 4], [0, 1]))
        distance = 0.0

        for p in range(w_array.shape[2]):

            q = np.argmax(res_d[:, :, :, p].flatten())
            d = q % 2
            q = q // 2
            j = q % self.n
            i = q // self.n

            weight = max(c + res_d[i, j, d, p], 0)

            if d == 0:
                self.extend_probability[i, j:(j + self.max_l), :] += w_array[:, :, p] * weight
            else:
                self.extend_probability[i:(i + self.max_l), j, :] += w_array[:, :, p] * weight

            distance += res_d[i, j, d, p]

        # print(-distance / w_array.shape[2])

        self.probability *= 0
        self.probability += self.extend_probability[:self.n, :self.n, :]
        self.probability += self.extend_probability[self.n:, :self.n, :]
        self.probability += self.extend_probability[:self.n, self.n:, :]
        self.probability += self.extend_probability[self.n:, self.n:, :]
        self.probability = np.maximum(self.probability, 0.05)
        self.probability /= self.probability.sum(axis=2, keepdims=True)

        # print(self.probability.max())

        self.update_roll_tensor()

        # print(self.probability)
        # print(self.evaluate(w_array))
        return None

    def evaluate(self, w_array):

        d_roll_bool = (self.d_roll == self.d_roll.max(axis=4, keepdims=True)).astype(np.float16)
        d_roll_bool /= d_roll_bool.sum(axis=4, keepdims=True)
        # print(d_roll_bool)

        res_d_bool = np.tensordot(d_roll_bool, w_array, axes=([3, 4], [0, 1]))
        score = 0

        for p in range(w_array.shape[2]):

            q = np.argmax(res_d_bool[:, :, :, p])
            d = q % 2
            q = q // 2
            j = q % self.n
            i = q // self.n
            # print(res_d_bool[i, j, d, p])
            if res_d_bool[i, j, d, p] == 1:
                score += 1
        return score

    def return_array(self):
        res_list = []
        for i in range(self.n):
            res = ""
            for j in range(self.n):
                k = np.argmax(self.probability[i, j])
                res = res + "ABCDEFGH"[k]
            res_list.append(res)
        return res_list


def solve(n, m, s_list):

    # initialize
    d = 8
    max_len = max([len(s) for s in s_list])
    pf = ProbabilityField(max_l=max_len)
    w_array = np.zeros((max_len, d, m), dtype=np.float16)
    for i, s in enumerate(s_list):
        for j, c in enumerate(s):
            k = "ABCDEFGH".index(c)
            w_array[j, k, i] = 1
        w_array[:, :, i] /= len(s)
    # print(w_array)

    # update loop
    for _ in range(10):
        pf.random_accept(w_array=w_array, t=10.0)
    for _ in range(10):
        pf.random_accept(w_array=w_array, t=5.0)
    for _ in range(10):
        pf.random_accept(w_array=w_array, t=3.0)
    pf.random_accept(w_array=w_array, t=1.0)
    pf.random_accept(w_array=w_array, t=1.0)
    pf.random_accept(w_array=w_array, t=1.0)
    pf.random_accept(w_array=w_array, t=0.3)
    pf.random_accept(w_array=w_array, t=0.3)
    pf.random_accept(w_array=w_array, t=0.3)
    pf.random_accept(w_array=w_array, t=0.1)
    pf.random_accept(w_array=w_array, t=0.1)
    pf.random_accept(w_array=w_array, t=0.1)
    pf.random_accept(w_array=w_array, t=0.03)
    pf.random_accept(w_array=w_array, t=0.03)
    pf.random_accept(w_array=w_array, t=0.03)
    pf.random_accept(w_array=w_array, t=0.01)
    pf.random_accept(w_array=w_array, t=0.01)
    pf.random_accept(w_array=w_array, t=0.01)
    # print(pf.evaluate(w_array))
    res_list = pf.return_array()
    return res_list


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(m)]
    res_list = solve(n, m, s_list)
    for res in res_list:
        print(res)


if __name__ == "__main__":
    main()
