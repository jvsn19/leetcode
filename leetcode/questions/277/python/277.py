def knows(a: int, b: int):
    pass

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        # O(N)
        for person in range(1, n):
            # If the current candidate knows a person, it cannot be a celebrity
            # because it knows someone, but this person now can be a candidate.
            # Otherwise, the candidate don't know the person, so it still can be
            # a celebrity
            if knows(candidate, person):
                candidate = person

        # Now the candidate don't know anyone before them and we don't know if 
        # everyone know them. We need to test, for everyone else, if they know
        # the candidate and if the candidate know any of them
        # O(2*N) -> O(N)
        for person in range(n):
            if person != candidate and (knows(candidate, person) or not knows(person, candidate)):
                return -1

        return candidate