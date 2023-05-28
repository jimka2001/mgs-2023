from TrueOrFalseBecause import TrueBecause, FalseBecause, forallM, existsM


class Magma:

    def gen(self):
        raise NotImplemented

    def op(self,a,b):
        raise NotImplemented

    def member(self,a):
        raise NotImplemented

    def equiv(self, a, b):
        if (a==b):
            return TrueBecause(f"{a} == {b}")
        else:
            return FalseBecause(f"{a} != {b}")

    def isClosed(self):
        return forallM(self.gen(), lambda a:
            forallM(self.gen, lambda b:
                self.member(self.op(a,b).member())))

    def isAssociative(self):
        return forallM(self.gen(), lambda a:
                       forallM(self.gen(), lambda b:
                               forallM(self.gen(), lambda c:
                                       self.equiv(self.op(self.op(a,b),c),
                                                  self.op(a,self.op(b,c))) + f"not associative: {a}, {b}, {c} ")))

    def isAbelian(self):
        return forallM(self.gen(), lambda a:
                       forallM(self.gen(), lambda b:
                               self.equiv(self.op(a,b),
                                          self.op(b,a)))) + f"not Abelian, e.g., {a},{b}"