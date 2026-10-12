"""
CONCEPT DEFINITIONS:
1. Getter: A method decorated with `@property` that allows you to access a method 
   as if it were a regular attribute, while executing custom logic behind the scenes.
2. Setter: A method decorated with `@property_name.setter` that intercepts value 
   assignments to attributes, allowing validation or data transformation.
3. Encapsulation: Hiding internal object representation and exposing a clean 
   interface through properties.
"""

class Employee:
    """Class demonstrating encapsulation using Getters and Setters in Python."""
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    # --------------------------------------------------------------------------
    # 1. GETTER METHOD (Using @property)
    # --------------------------------------------------------------------------
    @property
    def email(self):
        """Returns the email address derived dynamically from first and last name."""
        return f"{self.first_name}.{self.last_name}@company.com"

    # --------------------------------------------------------------------------
    # 2. SETTER METHOD (Using @property_name.setter)
    # --------------------------------------------------------------------------
    @email.setter
    def email(self, new_email: str):
        """Allows updating first and last name dynamically by assigning to .email"""
        print(f"Setting new email to: {new_email}")
        
        # Split incoming email string into parts
        name_part = new_email.split("@")[0]
        self.first_name, self.last_name = name_part.split(".")

    # --------------------------------------------------------------------------
    # 3. DELETER METHOD (Optional: @property_name.deleter)
    # --------------------------------------------------------------------------
    @email.deleter
    def email(self):
        """Resets name properties when email attribute is deleted."""
        print("Deleting email details...")
        self.first_name = None
        self.last_name = None


# DEMONSTRATION IN VS CODE

if __name__ == "__main__":
    # Create an employee instance
    emp = Employee("Harry", "Python")

    # Accessing the getter (Notice we call it like an attribute, NOT a method: emp.email)
    print(f"Initial Email (Getter): {emp.email}")

    # Using the setter by assigning a value directly to emp.email
    emp.email = "coder.harry@company.com"

    # Verify updated attributes
    print(f"Updated First Name: {emp.first_name}")
    print(f"Updated Last Name: {emp.last_name}")
    print(f"New Email (Getter): {emp.email}")

    # Using the deleter
    del emp.email
    print(f"After Deletion - First Name: {emp.first_name}")