from django.contrib.admin import AdminSite as DjangoAdminSite


# admin.site.register(Enrollment_checklist)

class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'ESR21 Pharmacy'
    site_title = 'ESR21 Pharmacy'
    index_title = 'ESR21 Pharmacy'


esr21_pharmacy_admin = AdminSite(name='esr21_pharmacy_admin')
