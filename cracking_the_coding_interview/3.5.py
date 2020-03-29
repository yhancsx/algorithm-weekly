'''
다시보기
'''
class AnimalShelter:
    def __init__(self):
        self.index = 0
        self.cats = collectons.deque()
        self.dogs = collections.deque()

    def enqueue(self, animalKey, type):
        if type == 'cat':
            self.cats.append((animalKey, self.index))
        else:
            self.dogs.append((animalKey, self.index))
        self.index += 1

    def dequeueAny(self):
        key1, index1 = self.dogs.popleft()
        key2, index2 = self.cats.popleft()
        if index1 < index2:
            self.cats.appendleft((key2, index2))
        else:
            self.dogs.appendleft((key1, index1))

    def dequeueDog(self):
        key, _ = self.dogs.popleft()
        return key

    def dequeueCat(self):
        key, _ = self.cats.popleft()
        return key