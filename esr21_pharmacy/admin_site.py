from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


# admin.site.register(Enrollment_checklist)

class AdminSite(DjangoAdminSite):
    site_url = '/administration'
    enable_nav_sidebar = False
    site_header = "Esr21 Site"

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        label = f'Esr21 {get_current_site(request).name.title()}: Pharmacy'
        context.update(
            site_title=label,
            site_header=label,
            index_title=label,
        )
        return context


esr21_pharmacy_admin = AdminSite(name='esr21_pharmacy_admin')
