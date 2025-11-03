# from django.views.generic import TemplateView

# class Certificate_SSL_View(TemplateView):
#     pass
    
#     # template_name = 'ssl.html'


from django.http import HttpResponse
from django.views.generic import TemplateView

from utils.check_ssl import verificar_certificado_ssl
from utils.list_sites import list_sites_124, list_sites_125

class ListSSLView(TemplateView):
    template_name = 'ssl_view/list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
    
        list_of_certificates_124 = []
        list_of_certificates_125 = []

        # for site in sites:
        #     list_of_certificates.append(verificar_certificado_ssl(site))

        for site_124 in list_sites_124:
            item = verificar_certificado_ssl(site_124)

            try:
                partes = item.split(" - ")
                status = partes[0].strip("[").strip("]")
                link = partes[1].split(' ')[0].strip("'")
                validade = partes[1].split(' ')[4]
                dias_expirar = partes[2].split(' ')[3]

                list_of_certificates_124.append({
                    'status': status,
                    'link': link,
                    'validade': validade,
                    'dias_expirar': dias_expirar
                })

            except Exception as e:
                list_of_certificates_124.append({'erro': f'Erro ao processar o item {item}'})


        for site_125 in list_sites_125:
            item = verificar_certificado_ssl(site_125)

            try:
                partes = item.split(" - ")
                status = partes[0].strip("[").strip("]")
                link = partes[1].split(' ')[0].strip("'")
                validade = partes[1].split(' ')[4]
                dias_expirar = partes[2].split(' ')[3]

                list_of_certificates_125.append({
                    'status': status,
                    'link': link,
                    'validade': validade,
                    'dias_expirar': dias_expirar
                })

            except Exception as e:
                list_of_certificates_124.append({'erro': f'Erro ao processar o item {item}'})


        context['certificados_124'] = list_of_certificates_124
        context['certificados_125'] = list_of_certificates_125
        return context





