# from django.views.generic import TemplateView

# class Certificate_SSL_View(TemplateView):
#     pass
    
#     # template_name = 'ssl.html'


from django.http import HttpResponse
from django.views.generic import TemplateView

from utils.check_ssl import verificar_certificado_ssl

def ssl_view(request):
    return HttpResponse('Até aqui deu certo.')


class ListSSLView(TemplateView):
    template_name = 'ssl_view/list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        sites = ['https://www.google.com',
                 'https://brasiliaambiental.df.gov.br/',
                 'https://ibram.df.gov.br/',
                 'https://onda.ibram.df.gov.br/portal/home/index.html',
                 'https://ondalab.ibram.df.gov.br/portal/home/index.html',
                 'https://www.ibram.df.gov.br/harpia/'
                ]
        
        list_of_certificates = []

        # for site in sites:
        #     list_of_certificates.append(verificar_certificado_ssl(site))

        for site in sites:
            item = verificar_certificado_ssl(site)

            try:
                print(item)
                partes = item.split(" - ")
                print(f'Partes: {partes}')
                status = partes[0].strip("[").strip("]")
                # print(f'Status: {status}')
                link = partes[1].split(' ')[0].strip("'")
                print(f'Link: {link}')
                validade = partes[1].split(' ')[4]
                print(f'Validade: {validade}')
                dias_expirar = partes[2].split(' ')[3]
                print(f'Dias para expirar: {dias_expirar}')

                list_of_certificates.append({
                    'status': status,
                    'link': link,
                    'validade': validade,
                    'dias_expirar': dias_expirar
                })


            except Exception as e:
                list_of_certificates.append({'erro': f'Erro ao processar o item {item}'})


        context['certificados'] = list_of_certificates
        return context





