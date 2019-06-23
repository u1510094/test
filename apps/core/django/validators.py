from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'^\+?\d{7,15}$', 'Only numbers and sign + allowed')
date_validator = RegexValidator(r'^(\d{4}-\d{2}-\d{2})|(present)$', 'Input is not date, or `present`')
size_expression_validator = RegexValidator(r'(^\<?\>?\=?\d{1,10}$)|(^\d{1,10}\<?\>?\=?$)',
                                           'Input may include characters such as >,<,= and numbers')
