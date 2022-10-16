from libqtile.config import Group, Match


class Groups(object):
    groups = [
        # first group that hold the terminals
        Group(
            # label='',
            init=True,
            exclusive=False,
            persist=True,
            matches=[Match(wm_class=['Alacritty', 'kitty'])],
            position=1,
            screen_affinity=1,
            name='1',
        ),
        Group(
            # label='',
            init=True,
            exclusive=False,
            persist=True,
            matches=[Match(wm_class=['Code'])],
            position=2,
            screen_affinity=1,
            name='2',
        ),
        Group(
            # label='',
            init=True,
            exclusive=False,
            persist=True,
            matches=[Match(wm_class=['Nemo'])],
            position=3,
            screen_affinity=1,
            name='3',
        ),
        Group(
            # label='',
            init=True,
            exclusive=False,
            persist=True,
            # matches=[Match(wm_class=['Nemo'])],
            position=4,
            screen_affinity=1,
            name='4',
        ),
        Group(
            # label='ﱘ',
            init=True,
            exclusive=False,
            persist=True,
            # matches=[Match(wm_class=['Nemo'])],
            position=5,
            screen_affinity=1,
            name='5',
        ),
        Group(
            # label='',
            init=True,
            persist=True,
            exclusive=False,
            matches=[Match(wm_class=['firefox'], role=['browser'])],
            position=6,
            screen_affinity=2,
            name='6',
        ),
        Group(
            # label='',
            init=True,
            persist=True,
            exclusive=False,
            #   matches=[Match(wm_class=['firefox'])],
            position=7,
            screen_affinity=2,
            name='7',
        ),
        Group(
            # label='調',
            init=True,
            persist=True,
            exclusive=False,
            matches=[Match(wm_class=['Steam'])],
            position=8,
            screen_affinity=2,
            name='8',
        ),
        Group(
            # label='',
            init=True,
            persist=True,
            exclusive=False,
            matches=[Match(wm_class=['discord'])],
            position=9,
            screen_affinity=2,
            name='9',
        ),
        Group(
            # label='',
            init=True,
            persist=True,
            exclusive=False,
            matches=[Match(wm_class=['PkgBrowser'])],
            position=10,
            screen_affinity=2,
            name='0',
        ),
    ]
