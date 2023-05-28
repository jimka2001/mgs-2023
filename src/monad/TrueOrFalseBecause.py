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


def existsM(items, p):
    tf = next((p(i) for i in items), FalseBecause(""))
    if tf:
        return TrueBecause("example " + tf.because)
    else:
        return tf


def forallM(items, p):
    return existsM(items, lambda i:
        p(i).Not()).Not()


print(TrueBecause("xxx") or FalseBecause("yyy"))
print(FalseBecause("yyy") or TrueBecause("xxx"))
print(TrueBecause("xxx") and FalseBecause("yyy"))
print(FalseBecause("yyy") and TrueBecause("xxx"))

print(existsM([TrueBecause("xxx"), FalseBecause("yyy")],
              lambda i: i))
