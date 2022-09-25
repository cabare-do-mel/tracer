# Troy the Tracer

## O que é?

<p>
Uma ferramenta usada para traçar a rota feita pelos pacotes que trafegam na internet. Ultilizada para diagnosticar problemas em uma rede.
</p>

## Como funciona?

<p>
O tracer funciona enviando pacotes ICMP, UDP, Echo Request para um destino conhecido com um valor TTL (Time To Live) especifico.
</p>
<p>
Cada vez que o pacote chega a um gateway (porta entre redes) a porta checa se o TTL é maior que um, caso seja, o programa diminui em 1 o TTL e tarnsmite para a proxima localização. Caso não seja, o gateway descarta o pacote, enviando uma mensage de error Time Oute (limite de tempo excedido) para o emisor do pacote.
</p>
<p>
Essas mensagens de erro são ultilizadas pelo cliente para determinar locais de falha na rede
</p>
