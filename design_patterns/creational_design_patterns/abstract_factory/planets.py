from abc import ABC, abstractmethod


# ==================================================
# 1. ABSTRACT PRODUCTS (Planet rules)
# ==================================================

class GravityCalculator(ABC):
    @abstractmethod
    def calculate_weight(self, earth_weight: float) -> float:
        pass


class TimeCalculator(ABC):
    @abstractmethod
    def calculate_age(self, earth_age: float) -> float:
        pass


# ==================================================
# 2. CONCRETE PRODUCTS — EARTH
# ==================================================

class EarthGravity(GravityCalculator):
    def calculate_weight(self, earth_weight: float) -> float:
        return earth_weight  # same as earth


class EarthTime(TimeCalculator):
    def calculate_age(self, earth_age: float) -> float:
        return earth_age


# ==================================================
# 3. CONCRETE PRODUCTS — MARS
# ==================================================

class MarsGravity(GravityCalculator):
    def calculate_weight(self, earth_weight: float) -> float:
        return earth_weight * 0.38


class MarsTime(TimeCalculator):
    def calculate_age(self, earth_age: float) -> float:
        return earth_age * 1.88


# ==================================================
# 4. CONCRETE PRODUCTS — JUPITER
# ==================================================

class JupiterGravity(GravityCalculator):
    def calculate_weight(self, earth_weight: float) -> float:
        return earth_weight * 2.34


class JupiterTime(TimeCalculator):
    def calculate_age(self, earth_age: float) -> float:
        return earth_age * 0.41


# ==================================================
# 5. ABSTRACT FACTORY (Planet)
# ==================================================

class PlanetFactory(ABC):
    """
    Abstract Factory: creates a family of related objects
    for a planet.
    """

    @abstractmethod
    def create_gravity_calculator(self) -> GravityCalculator:
        pass

    @abstractmethod
    def create_time_calculator(self) -> TimeCalculator:
        pass


# ==================================================
# 6. CONCRETE FACTORIES (Planets)
# ==================================================

class EarthFactory(PlanetFactory):
    def create_gravity_calculator(self) -> GravityCalculator:
        return EarthGravity()

    def create_time_calculator(self) -> TimeCalculator:
        return EarthTime()


class MarsFactory(PlanetFactory):
    def create_gravity_calculator(self) -> GravityCalculator:
        return MarsGravity()

    def create_time_calculator(self) -> TimeCalculator:
        return MarsTime()


class JupiterFactory(PlanetFactory):
    def create_gravity_calculator(self) -> GravityCalculator:
        return JupiterGravity()

    def create_time_calculator(self) -> TimeCalculator:
        return JupiterTime()


# ==================================================
# 7. CLIENT CODE (Planet-agnostic)
# ==================================================

class PlanetProfile:
    """
    Client code depends only on abstract factory.
    """

    def __init__(self, factory: PlanetFactory):
        self.gravity = factory.create_gravity_calculator()
        self.time = factory.create_time_calculator()

    def show_profile(self, earth_weight: float, earth_age: float):
        print(f"Weight on this planet: {self.gravity.calculate_weight(earth_weight):.2f} kg")
        print(f"Age on this planet: {self.time.calculate_age(earth_age):.2f} years")


# ==================================================
# 8. APPLICATION ENTRY POINT
# ==================================================

if __name__ == "__main__":

    earth_weight = 70  # kg
    earth_age = 25     # years

    print("---- EARTH ----")
    earth = PlanetProfile(EarthFactory())
    earth.show_profile(earth_weight, earth_age)

    print("\n---- MARS ----")
    mars = PlanetProfile(MarsFactory())
    mars.show_profile(earth_weight, earth_age)

    print("\n---- JUPITER ----")
    jupiter = PlanetProfile(JupiterFactory())
    jupiter.show_profile(earth_weight, earth_age)
