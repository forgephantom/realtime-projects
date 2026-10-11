#!/usr/bin/env python3
"""Molar Mass Calculator: Unit Converter.

A molecule's molar mass is the sum of its atoms' atomic weights, and it converts between grams weighed on a balance and moles used in equations. Parsing a chemical formula into element counts automates the bookkeeping.

Demo dataset idea: A seeded RNG draws formulas from a compound list with random masses and computes moles and required masses..
"""

import argparse
import random

SLUG = "molar-mass-calculator-unit_converter-beginner"
PARAMS = {'formula': 'chemical formula string such as H2SO4', 'mass_grams': 'sample mass in grams', 'target_moles': 'desired amount in moles'}


class UnitConverter:
    """Convert between units within a category using factor-to-base tables.

    Length, mass, volume, speed, and data sizes convert through a base unit
    with a single multiplication factor. Temperature is special-cased with
    to/from-Celsius functions because its scales have offsets, not just
    ratios.
    """

    CATEGORIES = {
        "length": {"base": "m", "units": {
            "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
            "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}},
        "mass": {"base": "kg", "units": {
            "mg": 1e-6, "g": 0.001, "kg": 1.0, "t": 1000.0,
            "oz": 0.028349523125, "lb": 0.45359237}},
        "volume": {"base": "L", "units": {
            "ml": 0.001, "L": 1.0, "floz": 0.0295735295625, "cup": 0.24,
            "pt": 0.473176473, "qt": 0.946352946, "gal": 3.785411784}},
        "speed": {"base": "m/s", "units": {
            "m/s": 1.0, "km/h": 1.0 / 3.6, "mph": 0.44704,
            "ft/s": 0.3048, "knot": 0.514444}},
        "data": {"base": "B", "units": {
            "B": 1, "KB": 1000, "MB": 1e6, "GB": 1e9,
            "KiB": 1024, "MiB": 1024 ** 2, "GiB": 1024 ** 3}},
    }
    TEMPERATURE_UNITS = ("c", "f", "k")

    @classmethod
    def _category_of(cls, unit: str):
        """(category_name, factor_or_None) for a unit; temperature -> ('temperature', None)."""
        if unit.lower() in cls.TEMPERATURE_UNITS:
            return ("temperature", None)
        for category, spec in cls.CATEGORIES.items():
            if unit in spec["units"]:
                return (category, spec["units"][unit])
        return (None, None)

    @staticmethod
    def _to_celsius(value: float, unit: str) -> float:
        unit = unit.lower()
        if unit == "c":
            return value
        if unit == "f":
            return (value - 32.0) * 5.0 / 9.0
        return value - 273.15  # k

    @staticmethod
    def _from_celsius(value: float, unit: str) -> float:
        unit = unit.lower()
        if unit == "c":
            return value
        if unit == "f":
            return value * 9.0 / 5.0 + 32.0
        return value + 273.15  # k

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert value from from_unit to to_unit; raises ValueError on misuse."""
        from_cat, from_factor = self._category_of(from_unit)
        to_cat, to_factor = self._category_of(to_unit)
        if from_cat is None:
            raise ValueError("unknown unit %r" % from_unit)
        if to_cat is None:
            raise ValueError("unknown unit %r" % to_unit)
        if from_cat != to_cat:
            raise ValueError("cannot convert %r (%s) to %r (%s)" % (
                from_unit, from_cat, to_unit, to_cat))
        if from_cat == "temperature":
            return self._from_celsius(self._to_celsius(value, from_unit), to_unit)
        return value * from_factor / to_factor

    def categories(self) -> list:
        """Category names, including temperature."""
        return sorted(list(self.CATEGORIES) + ["temperature"])

    def units(self, category: str) -> list:
        """Unit names for a category."""
        if category == "temperature":
            return list(self.TEMPERATURE_UNITS)
        return sorted(self.CATEGORIES[category]["units"])


def run_demo(seed: int) -> int:
    """Convert the seeded demo list and print a results table."""
    random.seed(seed)  # kept for the --seed contract; the table itself is fixed
    converter = UnitConverter()
    conversions = PARAMS.get("conversions", [["mi", "km", 5], ["c", "f", 100]])

    print("Molar Mass Calculator: Unit Converter  (topic: Molar Mass Calculator, seed=%d)" % seed)
    print("Supported categories: %s\n" % ", ".join(converter.categories()))
    print("%12s %-6s -> %-6s %s" % ("value", "from", "to", "result"))
    for from_unit, to_unit, value in conversions:
        result = converter.convert(value, from_unit, to_unit)
        print("%12g %-6s -> %-6s %g" % (value, from_unit, to_unit, result))
    print("\nConverted %d values across %d categories." % (
        len(conversions), len(converter.categories())))
    return 0


def run_single(value: float, from_unit: str, to_unit: str) -> int:
    """Convert one value supplied on the command line."""
    converter = UnitConverter()
    try:
        result = converter.convert(value, from_unit, to_unit)
    except ValueError as exc:
        print("error: %s" % exc)
        return 2
    print("%g %s = %g %s" % (value, from_unit, result, to_unit))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Molar Mass Calculator: Unit Converter: A molecule's molar mass is the sum of its atoms' atomic weights, and it converts between grams weighed on a balance and moles used in equations. Parsing a chemical formula into element counts automates the bookkeeping."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--value", type=float, default=None,
                        help="Single value to convert (needs --from and --to).")
    parser.add_argument("--from", dest="from_unit", type=str, default=None,
                        help="Source unit, e.g. mi.")
    parser.add_argument("--to", dest="to_unit", type=str, default=None,
                        help="Target unit, e.g. km.")
    return parser


def main(argv=None) -> int:
    """Entry point: demo table by default, single conversion with --value/--from/--to."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    if args.value is not None:
        if not args.from_unit or not args.to_unit:
            print("error: --value needs both --from and --to")
            return 2
        return run_single(args.value, args.from_unit, args.to_unit)
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
