from ..exceptions import ValidationError

class PublishedDateValidator:
    def __init__(self):
        pass

    def validate(self, published_date=None):
        if published_date is None:
            raise ValidationError("Published Date cannot be empty!")
        if not published_date:
            raise ValidationError("Published Date cannot be empty!")
        return True