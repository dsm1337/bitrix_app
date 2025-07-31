from django.apps import AppConfig


class DealsManagmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deals_managment'

    def ready(self):
        from integration_utils.bitrix24.models.bitrix_user_token import BitrixUserToken
        bitrix_token = BitrixUserToken.objects.filter(user__is_admin=True, is_active=True).first()
        if not bitrix_token:
            print('shit')
            return
        fields = bitrix_token.call_api_method('crm.deal.userfield.list')
        existing_field_names = {f['FIELD_NAME'] for f in fields.get('result', [])}

        if 'UF_CRM_PENALTY' not in existing_field_names:
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
            print('added UF_PENALTY')

        if 'UF_CRM_INTERNATIONAL_DEAL' not in existing_field_names:
            bitrix_token.call_api_method('crm.deal.userfield.add', {
                'fields': {
                    'FIELD_NAME': 'UF_INTERNATIONAL_DEAL',
                    'EDIT_FORM_LABEL': {'ru': 'Международная сделка'},
                    'LIST_COLUMN_LABEL': {'ru': 'Международная сделка'},
                    'LIST_FILTER_LABEL': {'ru': 'Международная сделка'},
                    'USER_TYPE_ID': 'boolean',
                    'MULTIPLE': 'N',
                    'MANDATORY': 'N',
                    'SHOW_IN_LIST': 'Y',
                    'EDIT_IN_LIST': 'Y',
                    'IS_SEARCHABLE': 'N',
                }
            })
            print('added UF_INTERNATIONAL_DEAL')