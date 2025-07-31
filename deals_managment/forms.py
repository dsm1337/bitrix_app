from django.forms import Form, CharField, DateField, FloatField, BooleanField, DateInput


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
    international_deal = BooleanField(label='Международная сделка')
