from typing import Callable, Any


class TrueOrFalseBecause:
    def __init__(self, because):
        self.because = because

    def __eq__(self, other):
        return other.because == self.because

    def Not(self) -> 'TrueOrFalseBecause':
        raise NotImplemented

    def __add__(self, other) -> 'TrueOrFalseBecause':
        raise NotImplemented

    def map(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        raise NotImplemented

    def flatMap(self, f: Callable[[str], 'TrueOrFalseBecause']):
        return f(self.because)

    def ifFalse(self, f: Callable[[str], 'TrueOrFalseBecause']) -> 'TrueOrFalseBecause':
        return self

    def mapIfTrue(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return self

    def mapIfFalse(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return self

    def ifTrue(self, f: Callable[[str], 'TrueOrFalseBecause']) -> 'TrueOrFalseBecause':
        return self


class TrueBecause(TrueOrFalseBecause):
    def __eq__(self, other):
        return isinstance(other, TrueBecause) and super().__eq__(other)

    def __repr__(self):
        return f"True[{self.because}]"

    def __bool__(self):
        return True

    def Not(self):
        return FalseBecause(self.because)

    def __add__(self, because):
        return TrueBecause(self.because + " " + because)

    def map(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return TrueBecause(f(self.because))

    def ifTrue(self, f: Callable[[str], 'TrueOrFalseBecause']) -> 'TrueOrFalseBecause':
        return self.flatMap(f)

    def mapIfTrue(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return self.ifTrue(lambda str: FalseBecause(f(str)))

class FalseBecause(TrueOrFalseBecause):
    def __eq__(self, other):
        return isinstance(other, TrueBecause) and super().__eq__(other)

    def __repr__(self):
        return f"False[{self.because}]"

    def __bool__(self):
        return False

    def __add__(self, because) -> 'TrueOrFalseBecause':
        return FalseBecause(self.because + " " + because)

    def Not(self):
        return TrueBecause(self.because)

    def map(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return FalseBecause(f(self.because))

    def ifFalse(self, f: Callable[[str], 'TrueOrFalseBecause']) -> 'TrueOrFalseBecause':
        return self.flatMap(f)

    def mapIfFalse(self, f: Callable[[str], str]) -> 'TrueOrFalseBecause':
        return self.ifFalse(lambda str: FalseBecause(f(str)))


def existsM(items, p: Callable[[Any], TrueOrFalseBecause]) -> TrueOrFalseBecause:
    for i in items:
        r = p(i)
        if r:
            return TrueBecause(f"example {i} because {r.because}")

    return FalseBecause("")


def forallM(items, p: Callable[[Any], TrueOrFalseBecause]) -> TrueOrFalseBecause:
    return existsM(items, lambda i: p(i).Not()).Not()


print(TrueBecause("xxx") or FalseBecause("yyy"))
print(FalseBecause("yyy") or TrueBecause("xxx"))
print(TrueBecause("xxx") and FalseBecause("yyy"))
print(FalseBecause("yyy") and TrueBecause("xxx"))

print(existsM([TrueBecause("xxx"), FalseBecause("yyy")],
              lambda i: i))
