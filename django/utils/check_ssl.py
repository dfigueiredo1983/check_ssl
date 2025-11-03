import ssl
from OpenSSL import crypto
from datetime import datetime, timezone

def verificar_certificado_ssl(url):
    hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
    port = 443

    try:
        cert_pem = ssl.get_server_certificate((hostname, port))
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)

        # Data de expiração (em bytes) → converter para datetime com timezone UTC
        data_exp_bytes = cert.get_notAfter()
        data_expiracao = datetime.strptime(data_exp_bytes.decode('ascii'), "%Y%m%d%H%M%SZ")
        data_expiracao = data_expiracao.replace(tzinfo=timezone.utc)

        data_atual = datetime.now(timezone.utc)

        if data_atual < data_expiracao:
            dias_expirar = (data_expiracao - data_atual).days
            # return f"[OK] - '{url}' é válido até {data_expiracao.strftime('%Y-%m-%d %H:%M:%S %Z')} - Dias para expirar: {dias_expirar}"
            return f"[OK] - '{url}' é válido até {data_expiracao.strftime('%Y-%m-%d')} - Dias para expirar: {dias_expirar}"
        else:
            # return f"[ERRO] - '{url}' expirou em {data_expiracao.strftime('%Y-%m-%d %H:%M:%S %Z')}."
            return f"[ERRO] - '{url}' expirou em {data_expiracao.strftime('%Y-%m-%d')}."
    except Exception as e:
        return f"[FALHA] Não foi possível verificar o certificado SSL de '{url}'. Erro: {e}"


if __name__ == "__main__":

    sites = [
        'euamocerrado.ibram.df.gov.br',
        'gaviao-api-homolog.ibram.df.gov.br',
        'gaviao-api.ibram.df.gov.br',
        'gaviao-homolog.ibram.df.gov.br',
        'gaviao.ibram.df.gov.br',
        'harpia-dev.ibram.df.gov.br',
        'harpia-hml.ibram.df.gov.br',
        'harpia.ibram.df.gov.br',
        'onda-homolog.ibram.df.gov.br'

        # 'https://www.google.com',
        # 'https://brasiliaambiental.df.gov.br/',
        # 'https://ibram.df.gov.br/',
        # 'https://onda.ibram.df.gov.br/portal/home/index.html',
        # 'https://ondalab.ibram.df.gov.br/portal/home/index.html',
        # 'https://www.ibram.df.gov.br/harpia/'
    ]

    for site in sites:
        resultado = verificar_certificado_ssl(site)
        print(resultado)


#  LISTAGEM DE URLS - IP 10.230.81.124

# euamocerrado.ibram.df.gov.br
# gaviao-api-homolog.ibram.df.gov.br
# gaviao-api.ibram.df.gov.br
# gaviao-homolog.ibram.df.gov.br
# gaviao.ibram.df.gov.br
# harpia-dev.ibram.df.gov.br
# harpia-hml.ibram.df.gov.br
# harpia.ibram.df.gov.br
# onda-homolog.ibram.df.gov.br


# LISTAGEM DE URLS - IP 10.230.81.125

# datastore.ibram.df.gov.br
# imageserver.ibram.df.gov.br
# intranet.ibram.df.gov.br
# onda.ibram.df.gov.br
# ondalab.ibram.df.gov.br
# portal.ibram.df.gov.br
# server.ibram.df.gov.br
