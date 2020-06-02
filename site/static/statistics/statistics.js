
const nodeUrl ='https://api.cyber.cybernode.ai';
const wsUrl= 'wss://api.cyber.cybernode.ai/websocket';

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
    const statusPromise = fetchAsync (`${nodeUrl}/status`);




      Promise.all([indexStatsPromise, statusPromise])
          .then(([indexStats, status]) => {
              const response = {
                 ...indexStats,
                 testnet: status.node_info.network,

              };
              const links = +response.linksCount
              const cids = +response.cidsCount
              const account = +response.accountsCount;

              const lastBlock = +response.height;

              const nameTestnet = response.testnet;

               document.getElementById('cyberlinks').innerHTML = formatNumber(links);
               document.getElementById('contentIds').innerHTML = formatNumber(cids);
               document.getElementById('accounts').innerHTML = formatNumber(account);

              //  document.getElementById('totalGCYB').innerHTML = formatNumber((totalCyb / 1000000000).toFixed(0));
              //  document.getElementById('stakedCYB').innerHTML = formatNumber(stakedCyb);
              //  document.getElementById('price').innerHTML = formatNumber(linkPrice);

              //  document.getElementById('validator').innerHTML = formatNumber(activeValidatorsCount);
              //  document.getElementById('transactions').innerHTML = formatNumber(txCount);
               document.getElementById('lastBlock').innerHTML = formatNumber(lastBlock);

               document.getElementById('testnet').innerHTML = nameTestnet;




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
