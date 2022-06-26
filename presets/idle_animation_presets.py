from gui.utils import IndexCycler

DIE_IDLE = IndexCycler([[0, 1, 2, 3, 4, 5], [3, 4, 1, 2, 0, 5], [5, 2, 1, 3, 4, 0], [1, 2, 5, 3, 0, 4]], 0.05)

AARON_IDLE = IndexCycler([[1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 7, 6, 5, 0, 0, 0, 0],
                          [10, 11, 12, 12, 12, 12, 12, 12, 12, 11, 10, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

ARCA_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 3, 3, 2, 1, 0, 0, 0],
                         [0, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 0],
                         [0, 0, 0, 5, 6, 7, 7, 7, 6, 5, 0, 0, 8, 9, 10, 10, 10, 9, 8, 0, 0, 0],
                         [0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0]], 0.09)

BADUCK_IDLE = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                           [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                           [0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 0],
                           [0, 0, 0, 0, 0]], 0.06)

BAGGINS_IDLE = IndexCycler([[1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 5, 5, 6, 5, 5, 4, 4, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                            [7, 8, 7, 8, 7, 8, 8, 8, 9, 9, 9, 8, 9],
                            [10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

BURSA_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 0],
                          [0, 0, 0, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0],
                          [0, 0, 0, 0, 8, 8, 0, 0, 8, 0, 0, 0, 8, 0, 0, 0, 0],
                          [0, 0, 0, 9, 10, 9, 11, 9, 10, 9, 0, 0, 0]], 0.1)

CENA_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0],
                         [0, 0, 0, 5, 6, 7, 8, 7, 6, 7, 6, 5, 0, 0, 0],
                         [0, 0, 0, 9, 10, 11, 11, 11, 10, 9, 9, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

CONNOR_IDLE = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                           [6, 7, 8, 8, 9, 9, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                           [10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

DORITA_IDLE = IndexCycler([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                            15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                            37, 38, 39]], 0.015)

ELLIE_IDLE = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

KIRAN_IDLE = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

MIGAHEXX_IDLE = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                             [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], 0.001)

PLAYER_IDLE = IndexCycler([[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                           [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                           [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

RIA_IDLE = IndexCycler([[0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 2, 3, 4, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 5, 6, 6, 6, 5, 0, 0, 0, 0, 0, 7, 8, 9, 8, 7, 0, 0, 0],
                        [0, 0, 0, 10, 11, 10, 11, 10, 0, 0, 0]], 0.1)

SHOPKEEPER_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 0, 0, 0],
                               [0, 5, 6, 7, 6, 5, 0, 0, 0, 0, 0],
                               [0, 8, 9, 10, 9, 8, 0, 0, 0, 0, 0],
                               [0, 11, 11, 11, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 0.05)

SOSH_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0, 0, 0],
                         [0, 0, 0, 4, 5, 6, 6, 6, 6, 6, 5, 4, 4, 0, 0, 0],
                         [0, 0, 0, 0, 7, 8, 9, 8, 9, 8, 7, 7, 0, 0, 0, 0],
                         [0, 0, 0, 10, 0, 0, 10, 10, 0, 0, 0, 0, 0],
                         [0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0]], 0.09)

SQUARE_IDLE = IndexCycler([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                           [3, 4, 1, 2, 0, 5, 7, 1, 2, 3, 10, 11],
                           [5, 2, 1, 3, 4, 0, 7, 2, 6, 8, 8],
                           [1, 2, 5, 3, 0, 4, 1, 1, 2, 6, 2, 3]], 0.05)

WALLY_IDLE = IndexCycler([[0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 7, 8, 7, 4, 3, 2, 1, 0, 0, 0],
                          [0, 0, 9, 9, 0, 0, 10, 11, 12, 12, 16, 16, 16, 12, 12, 12, 16, 12, 11, 10, 0, 0],
                          [0, 0, 9, 9, 15, 9, 15, 9, 0, 0],
                          [0, 0, 17, 18, 19, 20, 21, 22, 23, 24, 17, 18, 19, 20, 21, 22, 23, 24, 0, 0],
                          [0, 0, 0, 0, 0]], 0.07)

WANDRE_IDLE = IndexCycler([[0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 0, 0],
                           [0, 0, 0, 5, 6, 7, 8, 8, 8, 9, 9, 8, 8, 7, 6, 5, 0, 0, 0],
                           [0, 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 10, 10, 0, 0, 0],
                           [0, 0, 0, 11, 0, 11, 0, 11, 0, 0, 0],
                           [4, 4, 4, 4, 4, 4]], 0.09)
