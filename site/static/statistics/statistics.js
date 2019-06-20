
var nodeUrl ='http://88.198.36.117:26657'
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
  console.log(getStatistics());
  
getStatistics();

// async function fetchAsync (url) {
//     let response = await fetch(url);
//     let data = await response.json();
//     console.log(data);
//     return data;
//   }