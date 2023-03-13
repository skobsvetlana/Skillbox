from karma_classes import Life

KARMA = 500

buddist = Life()

while buddist.my_karma < KARMA:
    buddist.one_day()
    print('Day {}, karma = {}'.format(buddist.get_day_count(), buddist.my_karma))
