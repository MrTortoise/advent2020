class Validator:

    @staticmethod
    def get_total_valid(passwords):
        total = sum(1 for p in passwords if p.is_valid())
        return total
