from .models import VendorImage, CompanyLogo, SiteContent

def get_vendor_company_logo(request):
  return {
    'vendors': VendorImage.objects.all(),
    'company_logo': CompanyLogo.objects.first(),
    'site_content': SiteContent.objects.first(),
    }

