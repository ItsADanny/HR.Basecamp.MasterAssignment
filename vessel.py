class Vessel:

    def __init__(self, imo: int, mmsi: int, name: str, country: str, type: str, build: int, gross: int, netto: int, length: int, beam: int) -> None:
        self.imo = imo
        self.mmsi = mmsi
        self.name = name
        self.country = country
        self.type = type
        self.build = build
        self.gross = gross
        self.netto = netto
        self.length = length
        self.beam = beam

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))
