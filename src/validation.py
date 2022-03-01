from .variables import M, N


def isvalid(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True
