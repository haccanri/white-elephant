import random

class WhiteElephant(object):
    def __init__(self, num, max_steal_times=2):
        self.num = num
        self.max_steal_times = max_steal_times

    def compute(self):
        raise NotImplementedError

    def show(self):
        """show the optimal policy"""
        raise NotImplementedError

    def explain(self, env, target):
        """explain the options of target under current environment"""
        raise NotImplementedError

class SimpleWhiteElephant(WhiteElephant):
    def __init__(self, num, max_stolen_times=2):
        super(SimpleWhiteElephant, self).__init__(num, max_stolen_times)
        # selected gift for each candidate, -1 for not selected candidate
        self.gifts = [-1] * num
        # the stolen times for each gift
        self.gifts_stolen_times = [0] * num
        # the left gifts not selected
        self.left_gifts = set(range(num))

    def compute(self):
        for i in range(self.num):
            if self._no_gift_available(i):
                self._random_select(i)
            else:
                # steal one from others or random select one
                pass

    def _no_gift_available(self, i):
        assert i < self.num, 'index should be less than n'
        for i in range(i):
            if self.gifts[i] != -1 and \
                self.gifts_stolen_times[self.gifts[i]] < self.max_stolen_times:
                return False

        return True

    def _random_select(self, i):
        assert i < self.num, 'index should be less than n'
        lg = list(self.left_gifts)
        gift = random.choice(lg)
        self.gifts[i] = gift
        self.left_gifts.remove(gift)
