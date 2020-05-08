"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total   
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""
    #     if self.get_country_code:
    #         return self.country_code
    #     else:
    #         return None

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.tax = .08
    
    def get_total():
        super().get_total()
        return total
    
    def mark_shipped(self):
        super().mark_shipped()
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.country_code = country_code
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        super().get_total()
        return total
    
    def get_country_code(self):
        """Return the country code."""
       
        return self.country_code
    
    def mark_shipped(self):
        super().mark_shipped()
        
    


