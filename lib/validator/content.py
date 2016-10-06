from ..exceptions import ValidationError

class ContentValidator:
    def __init__(self):
        pass

    def validate(self, content=None):
        if content is None:
            raise ValidationError("Content cannot be empty!")
        if not content:
            raise ValidationError("Content cannot be empty!")
        return True