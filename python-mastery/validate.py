from decimal import Decimal

class Validator:
    @classmethod
    def check(cls, value):
        return value


class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError('Expected {}'.format(cls.expected_type))
        return super().check(value)    


class Integer(Typed):
    expected_type = int 

class Float(Typed):
    expected_type = float 

class String(Typed):
    expected_type = str 

class DecimalType(Typed):
    expected_type = Decimal


def customadd(x,y):
    Integer.check(x)
    Integer.check(y)
    return x + y

print(customadd(2,4))


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError("expected >= 0")
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError("Must be non-empty")
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass


if __name__ == "__main__":
    print(PositiveInteger.check((10)))
    print(NonEmptyString.check(("check_me_out")))