
class Boss:
    def __init__(self, name):
        self.name = name
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            worker.boss = self
            self.workers.append(worker)
        else:
            raise ValueError("Can only add instances of Worker class to Boss's workers list")


class Worker:
    def __init__(self, name, boss=None):
        self.name = name
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if new_boss is None or isinstance(new_boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            if new_boss:
                new_boss.add_worker(self)
            self._boss = new_boss
        else:
            raise ValueError("Worker's boss must be an instance of Boss class or None")

