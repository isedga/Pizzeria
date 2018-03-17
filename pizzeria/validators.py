from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class LowerAndUpperValidator(object):

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        lower = re.compile(r'[a-z]')
        upper = re.compile(r'[A-Z]')
        has_lower = lower.search(password)
        if has_lower is None:
            raise ValidationError(
                'The password must include at least one lowercase letter',
                code='password_no_lower'
            )
        has_upper = upper.search(password)
        if has_upper is None:
            raise ValidationError(
                'The password must include at least one uppercase letter',
                code='password_no_upper'
            )        
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d digit.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d letter.') % {'min_length': self.min_length})


    def get_help_text(self):
        return ""

