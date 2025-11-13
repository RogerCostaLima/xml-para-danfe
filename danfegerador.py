import io
from brazilfiscalreport.danfe import Danfe 


class DanfeGerador:

    
    def __init__(self, xml_content:str | bytes):
            if isinstance(xml_content, str):
                self.xml_bytes = xml_content.encode('utf-8')
            else:
                self.xml_bytes = xml_content


    def create_danfe(self) -> bytes | None:
    """Gera o DANFE em formato PDF e retorna seu conteúdo como um objeto de bytes."""
    try:
        buffer = io.BytesIO()

        danfe = Danfe(self.xml_bytes)

        # 🔹 Define texto personalizado de homologação:
        danfe.test_text = "NFe EMITIDA EM HOMOLOGAÇÃO\nSEM VALOR FISCAL"

        # 🔹 Gera o PDF no buffer
        danfe.output(buffer)

        pdf_bytes = buffer.getvalue()
        buffer.close()

        print("DANFE gerado em memória com sucesso.")
        return pdf_bytes

    except Exception as e:
        print(f"Erro ao gerar DANFE em memória: {e}")
        return None
