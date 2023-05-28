class TrueOrFalseBecause:
    def __init__(self, because):
        self.because = because

    def __eq__(self, other):
        return other.because == self.because

    def Not(self):
        raise NotImplemented

    def __add__(self, other):
        raise NotImplemented

    def __add__(self, because):
        return FalseBecause(self.because + " " + because)


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


class FalseBecause(TrueOrFalseBecause):
    def __eq__(self, other):
        return isinstance(other, TrueBecause) and super().__eq__(other)

    def __repr__(self):
        return f"False[{self.because}]"

    def __bool__(self):
        return False

    def Not(self):
        return TrueBecause(self.because)


def forallM(items, p):
    for i in items:
        acc = p(i)
        print(f"i={i}  p->{p(i)}")
        if not acc:
            return acc + f"example {i}"
    return TrueBecause("")

print(
  all(i for i in [TrueBecause("xxx"), FalseBecause("yyy")])
)

def existsM(items, p):
    q = lambda x: p(x).Not()
    return forallM(items, q).Not()

print(TrueBecause("xxx"))
print(FalseBecause("yyy"))

print(existsM([TrueBecause("xxx"), FalseBecause("yyy")],
              lambda i: i))
