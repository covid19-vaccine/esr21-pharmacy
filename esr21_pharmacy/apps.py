from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'esr21_pharmacy'
    verbose_name = 'ESR21 Pharmacy Forms'
    admin_site_name = 'esr21_pharmacy_admin'
