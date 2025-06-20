# Serviço de Agendamento Automático

Este projeto é um script Python que realiza agendamentos automáticos de serviços para veículos, utilizando integração com APIs RESTful. O sistema permite configurar horários para agendamentos e notifica por meio de webhooks. 

## Recursos

- **Carregamento de dados JSON**: Importa dados de veículos para identificar veículos de suporte.
- **Integração com API**: Obtém informações detalhadas sobre o serviço e locatário.
- **Envio de Webhook**: Notifica um endpoint externo quando um serviço é agendado.
- **Agendamento Programado**: Utiliza a biblioteca `schedule` para executar tarefas em horários específicos.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - `schedule`
  - `requests`
  - `json`
  - `datetime`
  - [Custom tokenaut](https://github.com/seu-repo/tokenaut)

## Configuração

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu-repo/servico-agendamento.git
   cd servico-agendamento
   ```

2. **Instalar dependências**:
   Use o gerenciador de pacotes `pip` para instalar as bibliotecas:
   ```bash
   pip install -r requirements.txt
   ```

3. **Arquivo JSON**:
   Crie um arquivo `idcarros.json` com o seguinte formato:
   ```json
   [
       {
           "veiculo_suporte_id": "ID_DO_CARRO",
           "placa_veiculo_suporte": "PLACA",
           "filial_origem_veiculo": "FILIAL"
       }
   ]
   ```

4. **Configuração do Token**:
   Certifique-se de que a biblioteca `tokenaut` está configurada corretamente conforme as credenciais de sua instituição 

## Uso

1. **Execução do script**:
   Execute o script principal:
   ```bash
   python main.py
   ```

2. **Entrada de dados**:
   - Forneça o ID do serviço ao ser solicitado.
   - O script buscará informações sobre o serviço e o locatário na API.
   - Insira o ID do carro associado ao serviço.
   - Defina o horário para o agendamento no formato `HH:MM`.

3. **Processo de agendamento**:
   - O script configurará as tarefas programadas e aguardará a execução no horário especificado.
   - Notificações serão enviadas via webhook.

4. **Finalização**:
   Quando todos os agendamentos forem concluídos, o script encerrará automaticamente.

## Estrutura do Código

- **`carregar_dados_json`**: Carrega dados do arquivo JSON contendo informações sobre veículos.
- **`buscar_carro_por_id`**: Localiza informações de um carro com base no ID.
- **`enviar_webhook`**: Envia uma notificação para o webhook configurado.
- **`dadosends`**: Consulta a API para buscar informações sobre um serviço.
- **`agendamento`**: Programa um serviço para um veículo em um horário específico.

## Contribuições

Contribuições são bem-vindas. Abra uma issue ou envie um pull request no repositório.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se tiver dúvidas, entre em contato com [odevpablo@gmail.com](mailto:odevpablo@gmail.com).
