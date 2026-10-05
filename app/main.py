class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
            self, start: tuple,
            end: tuple,
            is_drowned: bool = False
    ) -> None:

        self.start = start
        self.end = end
        self.is_drowned = is_drowned
        self.decks = []

        if self.start[0] == self.end[0]:
            for column in range(self.start[1], self.end[1] + 1):
                self.decks.append(Deck(self.start[0], column))

        else:
            for row in range(self.start[0], self.end[0] + 1):
                self.decks.append(Deck(row, self.end[1]))

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:

            if deck.row == row and deck.column == column:
                return deck

        return

    def fire(self, row: int, column: int) -> None:
        alive_deck = False

        for deck in self.decks:
            if deck.row == row and deck.column == column:
                deck.is_alive = False

            if deck.is_alive:
                alive_deck = True

        if alive_deck is False:
            self.is_drowned = True


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.ships = ships
        self.field = {}
        for ship in ships:
            start, end = ship
            ship = Ship(start, end)
            for decks in ship.decks:
                self.field[(decks.row, decks.column)] = ship

    def fire(self, location: tuple) -> str:
        if location in self.field:

            ship = self.field[location]

            row, column = location
            ship.fire(row, column)

            if ship.is_drowned is True:
                return "Sunk!"

            return "Hit!"
        return "Miss!"
