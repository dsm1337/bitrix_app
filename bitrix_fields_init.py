from integration_utils.bitrix24.models.bitrix_user_token import BitrixUserToken  # функция для получения BitrixUserToken
import os
import django

def create_deal_custom_fields(bitrix_token):
    bitrix_token.call_api_method('crm.deal.userfield.add', {
        'fields': {
            'FIELD_NAME': 'UF_PENALTY',
            'EDIT_FORM_LABEL': {'ru': 'Неустойка'},
            'LIST_COLUMN_LABEL': {'ru': 'Неустойка'},
            'LIST_FILTER_LABEL': {'ru': 'Неустойка'},
            'USER_TYPE_ID': 'double',
            'MULTIPLE': 'N',
            'MANDATORY': 'N',
            'SHOW_IN_LIST': 'Y',
            'EDIT_IN_LIST': 'Y',
            'IS_SEARCHABLE': 'N',
        }
    })
    bitrix_token.call_api_method('crm.deal.userfield.add', {
        'fields': {
            'FIELD_NAME': 'UF_INTERNATIONAL_DEAL',
            'EDIT_FORM_LABEL': {'ru': 'Международная сделка'},
            'LIST_COLUMN_LABEL': {'ru': 'Международная сделка'},
            'LIST_FILTER_LABEL': {'ru': 'Международная сделка'},
            'USER_TYPE_ID': 'char',
            'MULTIPLE': 'N',
            'MANDATORY': 'N',
            'SHOW_IN_LIST': 'Y',
            'EDIT_IN_LIST': 'Y',
            'IS_SEARCHABLE': 'N',
        }
    })

if __name__ == '__main__':
    but = BitrixUserToken.objects.filter(user__is_admin=True, is_active=True).first()
    create_deal_custom_fields(but)