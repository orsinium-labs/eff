import pytest
import eff


def test_init():
    e = eff.Effects(print=print)
    assert e.print is print


def test_short_alias():
    assert eff.ects is eff.Effects
    e = eff.ects(print=print)
    assert e.print is print


def test_no_attr():
    e = eff.Effects()
    with pytest.raises(AttributeError):
        e.print


def test_context():
    with eff.Effects(print=print) as e:
        assert e.print is print


def test_context_class_access():
    with eff.Effects(print=print):
        assert eff.Effects.print is print


def test_context_no_suppress():
    with pytest.raises(ZeroDivisionError):
        with eff.Effects(print=print):
            raise ZeroDivisionError


def test_deep_context():
    sent1 = object()
    sent2 = object()
    with eff.Effects(sent=sent1) as e1:
        assert e1.sent is sent1
        assert eff.Effects.sent is sent1

        with eff.Effects(sent=sent2) as e2:
            assert e1.sent is sent1
            assert e2.sent is sent2
            assert eff.Effects.sent is sent2

        assert e1.sent is sent1
        assert eff.Effects.sent is sent1


def test_two_contexts():
    class E1(eff.Effects):
        pass

    class E2(eff.Effects):
        pass

    sent1 = object()
    sent2 = object()
    with E1(sent=sent1) as e1, E2(sent=sent2) as e2:
        assert isinstance(e1, E1)
        assert isinstance(e2, E2)

        assert e1.sent is sent1
        assert e2.sent is sent2

        assert E1.sent is sent1
        assert E2.sent is sent2
