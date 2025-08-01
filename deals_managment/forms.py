from django.forms import Form, CharField, DateField, FloatField, BooleanField, DateInput, ValidationError


class DealForm(Form):
    title = CharField(max_length=128, label='Название')
    begin_date = DateField(
        label='Дата начала',  widget=DateInput(attrs={'type': 'date'})
    )
    close_date = DateField(
        label='Дата завершения',  widget=DateInput(attrs={'type': 'date'})
    )
    opportunity = FloatField(label='Сумма')
    penalty = FloatField(label='Неустойка при нарушении договора')
    international_deal = BooleanField(label='Международная сделка', required=False)


    def clean(self):
        cleaned_data = super().clean()
        begin_date = cleaned_data.get('begin_date')
        close_date = cleaned_data.get('close_date')
        if begin_date and close_date and close_date < begin_date:
            raise ValidationError('Конец сделки не может быть раньше начала!')
