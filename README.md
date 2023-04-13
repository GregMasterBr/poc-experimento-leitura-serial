# Projeto para demonstrar viabilidade do uso 5G em projetos IOTs utilizando o protocolo MQTT

Transferência de dados utilizando uma Raspberry Pi 4B, adquirindo dados via as portas USBs de diferentes sensores, e transmitindo para um broker online via MQTT e uma dashboard (streamlit) buscando esses dados para exibição.

## Estrura das pasta do projeto
* Client - Código instalado no raspberry pi, no qual faz a leitura dos sensores e envia para o broker via MQTT
* Sensores - Códigos de diferentes tipos de sensores que enviam seus dados via serial
* Dashboard - Painel de visualização das transmissão dos dados em tempo real. O Painel faz a leitura direto do broker. 

## Configuração do ambiente

```shell
python -m pip install --upgrade pip
python -m venv .venv
```

* Ativar o ambiente virtual  
    - Windows
    ```shell
    .venv/Scripts/activate
    ```

    - Linux
    ```shell
    source .\.venv\bin\activate
    ```

* Instalar as dependências do projeto
```shell
pip install -r .\requirements.txt
```

## Para rodar a aplicação:
* Para executar a Dashboard
Navegue até a pasta ***dashboard*** e execute o comando:  

```shell
streamlit run .\main.py
```  
* Para executar o Client (raspberrypi) 
Navegue até a pasta ***client*** e execute o comando:    

```shell
python .\app.py
```
