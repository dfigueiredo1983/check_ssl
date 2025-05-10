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
        'https://www.google.com',
        'https://brasiliaambiental.df.gov.br/',
        'https://ibram.df.gov.br/',
        'https://onda.ibram.df.gov.br/portal/home/index.html',
        'https://ondalab.ibram.df.gov.br/portal/home/index.html',
        'https://www.ibram.df.gov.br/harpia/'
    ]

    for site in sites:
        resultado = verificar_certificado_ssl(site)
        print(resultado)
