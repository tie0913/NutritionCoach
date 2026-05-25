class NutriCoachException(Exception):

    def __init__(self, code=400, message="Business exception"):
        self.code = code
        self.message = message
        super().__init__(self.message)