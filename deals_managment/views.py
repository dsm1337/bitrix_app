from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from .forms import DealForm

def delete_all(bx_token, deals):
    for deal in deals:
        bx_token.call_api_method("crm.deal.delete", params={"id": deal['ID']})

@main_auth(on_cookies=True)
def list_deals(request):
    but = request.bitrix_user_token
    fields = ['ID', 'TITLE', 'BEGINDATE', 'CLOSEDATE', 'OPPORTUNITY', 'UF_CRM_PENALTY', 'UF_CRM_INTERNATIONAL_DEAL']
    deals = but.call_api_method(
        'crm.deal.list', params={
            'select': fields
        }
    )
    all_fields = but.call_list_method('crm.deal.fields')
    field_names = []
    for name in fields:
        if 'listLabel' in all_fields[name]:
            field_names.append(all_fields[name]['listLabel'])
        else:
            field_names.append(all_fields[name]['title'])
    for deal in deals['result']:
        print(deal)
    # delete_all(but, deals)
    return render(request, 'deals_list.html', context={'deals': deals['result'], 'names': field_names})

@main_auth(on_cookies=True)
def add_deal(request):
    but = request.bitrix_user_token
    print(request.GET)
    form = DealForm(request.GET or None)
    if form.is_valid():
        data = form.cleaned_data
        fields = {
            'TITLE': data['title'],
            'BEGINDATE': data['begin_date'].strftime('%Y-%m-%d'),
            'CLOSEDATE': data['close_date'].strftime('%Y-%m-%d'),
            'OPPORTUNITY': data['opportunity'],
            'UF_CRM_PENALTY': data['penalty'],
            'UF_CRM_INTERNATIONAL_DEAL': 'Y' if data['international_deal']  else 'N',
        }
        res = but.call_api_method('crm.deal.add', params={'fields':fields})
        print(f'Данные: {fields}. Результат : {res}')
    else:
        print('1232')
    return render(request, 'add_deal.html', locals())