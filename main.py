# separa os blocos de legenda (enumeração + tempo + falas)
# em sublistas
def converteBlocosDeLegendaEmSublistas(listaDoArquivo):
    listaAux = []
    novaLista = []

    for elemento in listaDoArquivo:
        if elemento != '\n':
            listaAux.append(elemento)
        else:
            novaLista.append(listaAux)
            listaAux = []

    return novaLista



def estruturaDados(caminhoDaLegenda):
    arquivo = open(caminhoDaLegenda, 'r')

    listaDoArquivo = arquivo.readlines()
    novaListaEstruturada = converteBlocosDeLegendaEmSublistas(listaDoArquivo)

    arquivo.close()

    return novaListaEstruturada



def novaLegendaComTranscricao(listaIngles, listaPortugues):
    novaLegenda = []
    listaAuxiliar = []

    for blocoDeLegenda1, blocoDeLegenda2 in zip(listaIngles, listaPortugues):
        if len(blocoDeLegenda1) > 2:
            for elemento1, elemento2 in zip(blocoDeLegenda1, blocoDeLegenda2):
                listaAuxiliar.append(elemento1)
                listaAuxiliar.append(elemento2)
            
            # remove numeração e tempo repetido
            del listaAuxiliar[1]
            del listaAuxiliar[2]
            

            novaLegenda.append(listaAuxiliar)

            listaAuxiliar = []
        else:
            novaLegenda.append(blocoDeLegenda1)

    return novaLegenda



def escreveNovoArquivoDeLegenda(novaLegenda, saida):
    arquivo = open(saida, 'w')

    for sublista in novaLegenda:
        for elemento in sublista:
            arquivo.write(elemento)
        arquivo.write('\n')

    arquivo.close()



if __name__ == '__main__':
    arquivo1 = './material/lecture0.srt'
    arquivo2 = './material/week-zero-scratch-portugues.srt'
    saidaDoNovoArquivo = './output/legenda-com-transcricao.srt'

    try:
        listaIngles = estruturaDados(arquivo1)
        listaPortugues = estruturaDados(arquivo2)
        novaLegenda = novaLegendaComTranscricao(listaIngles, listaPortugues)
    except:
        print("Não foi possível abrir os arquivos.")
    
    try:
        escreveNovoArquivoDeLegenda(novaLegenda, saidaDoNovoArquivo)
    except:
        print("Não foi possível gerar o arquivo de transcrição.")
