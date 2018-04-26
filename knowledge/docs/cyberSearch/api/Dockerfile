FROM swaggerapi/swagger-ui:v3.12.1

COPY docs/common.v1.yaml /usr/share/nginx/html/
COPY docs/search.v1.yaml /usr/share/nginx/html/
COPY docs/bitcoin.v1.yaml /usr/share/nginx/html/
COPY docs/ethereum.v1.yaml /usr/share/nginx/html/

ENV API_URLS='[                                              \
    {name:"Search API", url:"search.v1.yaml"},               \
    {name:"Ethereum API", url:"ethereum.v1.yaml"},            \
    {name:"Bitcoin API", url:"bitcoin.v1.yaml"}            \
]'

