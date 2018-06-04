FROM swaggerapi/swagger-ui:v3.14.2

COPY docs/api/common.v1.yaml /usr/share/nginx/html/
COPY docs/api/search.v1.yaml /usr/share/nginx/html/
COPY docs/api/bitcoin.v1.yaml /usr/share/nginx/html/
COPY docs/api/ethereum.v1.yaml /usr/share/nginx/html/

ENV API_URLS='[                                              \
    {name:"Search API", url:"search.v1.yaml"},               \
    {name:"Ethereum API", url:"ethereum.v1.yaml"},            \
    {name:"Bitcoin API", url:"bitcoin.v1.yaml"}            \
]'

