import xmltodict

def nome_moedas():
    with open("moedas.xml", "rb") as arquivos_moedas:
        dic_moedas = xmltodict.parse(arquivos_moedas)

    moedas = dic_moedas["xml"]
    return moedas

def conver_disp():
    with open("available.xml", "rb") as arquivos_conver:
        dic_conver = xmltodict.parse(arquivos_conver)

    conver = dic_conver["xml"]
    dic_conver_disp = {}
    for par_conver in conver:
        moeda_origem, moeda_destino = par_conver.split("-")
        if moeda_origem in dic_conver_disp:
            dic_conver_disp[moeda_origem].append(moeda_destino)
        else:
            dic_conver_disp[moeda_origem] = [moeda_destino]
    return dic_conver_disp