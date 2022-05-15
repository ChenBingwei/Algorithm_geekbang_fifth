from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        self.top_voted = []
        top_person = -1
        person_votes = {-1: -1}
        for person in self.persons:
            person_votes.setdefault(person, 0)
            person_votes[person] += 1
            if person_votes[person] >= person_votes[top_person]:
                top_person = person
            self.top_voted.append(top_person)

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.top_voted[right]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
