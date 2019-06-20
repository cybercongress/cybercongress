
var nodeUrl ='http://88.198.36.117:26657';
const wsUrl= 'ws://88.198.36.117:26657/websocket';



async function fetchAsync (url) {
    let response = await fetch(url);
    let data = await response.json();
    return data.result;
  }
  const formatNumber = (number, toFixed) => {
    let formatted = +number;

    if (toFixed) {
        formatted = +formatted.toFixed(toFixed);
    }

    return formatted
        .toLocaleString('en')
        .replace(/,/g, ' ');
};

  getStatistics = () => new Promise((resolve) => {
    
    const indexStatsPromise = fetchAsync (`${nodeUrl}/index_stats`);
    const stakingPromise = fetchAsync (`${nodeUrl}/staking/pool`);
    const bandwidthPricePromise = fetchAsync (`${nodeUrl}/current_bandwidth_price`);
    const latestBlockPromise = fetchAsync (`${nodeUrl}/block`);
    const validatorsPromise = fetchAsync (`${nodeUrl}/staking/validators`);



      Promise.all([indexStatsPromise, stakingPromise, bandwidthPricePromise, latestBlockPromise, validatorsPromise])
          .then(([indexStats, staking, bandwidthPrice, latestBlock, validators]) => {
              const response = {
                 ...indexStats,
                 notBondedTokens: staking.not_bonded_tokens,
                 bondedTokens: staking.bonded_tokens,
                 price: bandwidthPrice.price,
                 txCount: latestBlock.block_meta.header.total_txs,
                 validatorsActive: validators,

              };
              const links = +response.linksCount
              const cids = +response.cidsCount
              const account = +response.accsCount;

              const bondedTokens = +response.bondedTokens;
              const notBondedTokens = +response.notBondedTokens;
      
              const totalCyb = bondedTokens + notBondedTokens;
              const stakedCyb = (bondedTokens / totalCyb * 100).toFixed(0);
              const linkPrice = (400 * +response.price).toFixed(0);
            
              const activeValidatorsCount = validators
              .filter(validator => !validator.jailed)
              .length;
              const txCount = +response.txCount;
              const lastBlock = +response.height;

               document.getElementById('cyberlinks').innerHTML = formatNumber(links);
               document.getElementById('contentIds').innerHTML = formatNumber(cids);
               document.getElementById('accounts').innerHTML = formatNumber(account);

               document.getElementById('totalGCYB').innerHTML = formatNumber((totalCyb / 1000000000).toFixed(0));
               document.getElementById('stakedCYB').innerHTML = formatNumber(stakedCyb);
               document.getElementById('price').innerHTML = formatNumber(linkPrice);

               document.getElementById('validator').innerHTML = formatNumber(activeValidatorsCount);
               document.getElementById('transactions').innerHTML = formatNumber(txCount);
               document.getElementById('lastBlock').innerHTML = formatNumber(lastBlock);


              resolve(response);
            
          });
  });
  
getStatistics();

let websocket;
const listenNewBlock = (cb) => {
    websocket = new WebSocket(wsUrl);
    websocket.onopen = () => {
      console.log('WebSocket is connected.');
        websocket.send(JSON.stringify({
            "method": "subscribe",
            "params": ["tm.event='NewBlockHeader'"],
            "id": "1",
            "jsonrpc": "2.0",
        }));
    };

    websocket.onmessage = (event) => {
        // cb(event);
        // var message = event;
        // console.log(message);
        getStatistics();
    };
};

onNewBlock = (cb) => {
    if (websocket) {
        websocket.onclose = () => {
            listenNewBlock(cb);
            getStatistics();
        };

        websocket.close();
    } else {
        listenNewBlock(cb);
    }
};

unsubscribeNewBlock = () => {
    if (websocket) {
        websocket.close();
        websocket = null;
    }
};

onNewBlock();

// async function fetchAsync (url) {
//     let response = await fetch(url);
//     let data = await response.json();
//     console.log(data);
//     return data;
//   }