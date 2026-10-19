"""
CONCEPT DEFINITIONS:
1. Method Overriding: An object-oriented feature where a child class redefines a 
   method that is already present in its parent class to tailor its behavior.
2. super() in Overriding: Allows the child class method to invoke the parent class's 
   original method implementation before or after adding custom logic.

"""

class Shape:
    """Parent Class representing a general 2D shape."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def calculate_area(self):
        """Base method to calculate area (default behavior)."""
        return self.x * self.y


class Circle(Shape):
    """Child Class representing a Circle, inheriting from Shape."""
    def __init__(self, radius: float):
        # We pass radius as both x and y to the parent constructor
        super().__init__(radius, radius)
        self.radius = radius

    # Method Overriding: Redefining calculate_area specifically for a Circle
    def calculate_area(self):
        """Overrides the parent's rectangular area formula with the circle area formula."""
        pi = 3.14159
        # We can either compute directly or call super().calculate_area() if applicable
        return pi * (self.radius ** 2)


# ==============================================================================
# DEMONSTRATION IN VS CODE
# ==============================================================================

if __name__ == "__main__":
    # Test Parent Class (Rectangle-like shape)
    rect = Shape(4, 5)
    print(f"Rectangle/Shape Area: {rect.calculate_area()}")  # Output: 20

    # Test Child Class with Overridden Method
    circ = Circle(3)
    print(f"Circle Area (Overridden Method): {circ.calculate_area()}")  # Output: ~28.27431