# gmail.com, yahoo.com, test.com
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible



def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email {value} is incorrect address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <{args[0].split("@")[1]}> not valid.')


def validate_unique_email(value):
    from students.models import Student
    if Student.objects.filter(email=value).exists():
        raise ValidationError(f'Email {value} is already use.')

def validate_phone_number(value):
    symbols_for_phone = '+0123456789'
    if len(value) != 13:
        raise ValidationError('Lenth of phone number must be 13 sybmols.')
    else:
        for i in value:
            if i not in symbols_for_phone:
                raise ValidationError('Phone number must be entered in the format: +380001111111.')

