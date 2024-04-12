class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive

    def __str__(self) -> str:
        return f"({self.row}, {self.column}) - {'Alive' if self.is_alive else 'Destroyed'}"


class Ship:
    def __init__(
            self,
            start: tuple[int, int],
            end: tuple[int, int],
            is_drowned: bool = False
    ) -> None:
        self.is_drowned = is_drowned
        self.decks = []
        if start[1] != end[1]:
            for index in range(start[1], end[1] + 1):
                self.decks.append(Deck(start[0], index))
        elif start[0] != end[0]:
            for index in range(start[0], end[0] + 1):
                self.decks.append(Deck(index, end[1]))
        elif start[1] == end[1] and start[0] == end[0]:
            for index in range(start[0], end[0] + 1):
                self.decks.append(Deck(index, end[1]))

    def get_deck(self, row: int, column: int) -> Deck:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck

    def fire(self, row: int, column: int) -> None:
        self.get_deck(row, column).is_alive = False
        print([deck.is_alive for deck in self.decks])
        if all(deck.is_alive for deck in self.decks):
            self.is_drowned = True
        print(self.is_drowned)
        print()


class Battleship:
    def __init__(self, ships: tuple) -> None:
        self.field = {
            (deck.row, deck.column):
                Ship(start=ship[0], end=ship[1])
            for ship in ships
            for deck in Ship(start=ship[0], end=ship[1]).decks}
        self.ships = ships

    def fire(self, location: tuple) -> str:
        if location in self.field:
            ship = self.field[location]
            ship.fire(*location)
            if ship.is_drowned:
                return "Sunk!"
            return "Hit!"
        return "Miss!"


ships = [
    ((2, 0), (2, 3)),
    ((4, 5), (4, 6)),
    ((3, 8), (3, 9)),
    ((6, 0), (8, 0)),
    ((6, 4), (6, 6)),
    ((6, 8), (6, 9)),
    ((9, 9), (9, 9)),
    ((9, 5), (9, 5)),
    ((9, 3), (9, 3)),
    ((9, 7), (9, 7)),
]

# Створення об'єкту Battleship з заданими кораблями
battlefield = Battleship(ships)

coordinates = [
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),

]

for coord in coordinates:
    result = battlefield.fire(coord)
    print(result)
