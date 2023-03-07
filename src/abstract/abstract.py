num_tests = 1000


def is_closed(gen, member, op):
    return all(member(op(gen(), gen()))
               for _ in range(num_tests))


def is_identity(gen, identity, op):
    return all(x == op(x, identity)
               for _ in range(num_tests)
               for x in [gen()]
               )


def is_associative(gen, op):
    for _ in range(num_tests):
        a = gen()
        b = gen()
        c = gen()
        if op(a, op(b, c)) != op(op(a, b), c):
            return False
    return True


def is_monoid(gen, member, identity, op):
    return is_closed(gen, member, op) \
        and is_identity(gen, identity, op) \
        and is_associative(gen, op)


def is_abelian(gen, member, identity, op, invert):
    pass


def is_group(gen, member, op):
    pass


def is_ring(gen, member, zero, one, plus, times):
    pass


def is_field(gen, member, zero, one, plus, times):
    pass
