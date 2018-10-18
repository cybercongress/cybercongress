# DApp guidelines

@asadovka

## What is App?

App in Cyb is a one or multi page application. It can be a simple html file as a frontend and may include smart contract logic as a backend. Apps should be available through IPFS hash.

## App structure

Cyb CLI can automatically generate structure for your App. All you need to do is just type some commands, come up with a name and develop!

## App requirements

We set limitations of computation resources usage for each app.

- less then 5% of CPU usage
- less then 10% of RAM usage

## App development

Here we describe how to generate initial app structure.

1. Install the latest version of CYB package
npm install -g cyb

2. Select the path where you want to store your app. For example /Desktop/My_apps
cd username/Desktop/My_apps

3. Enter the name and generate the structure of the app. A folder with all necessary components will be created
cyb init appname

4. Go to the app folder and link your app with your Cyb
cyb link

5. Open the Appstore in CYB. You will see your app on «Your app» page

You can also use our Help App (cyb://.help/create) for more info.

## App deployment

When you are ready with development of your app you can easely publish it to the DApp Store so every user of Cyb will see it.
Open your app, click on "deploy" button and enter IPFS hash of your app. Sign the transaction - your app will be registred in Chaingear. And that is it!

## App design

App design process follows Web3 design principles.

## State rules

We use simple colored states for states of transactions or operations:

- mempool/failed - red
- confirmed/reverted - yellow
- finalized/succesful - green

## Data visualization

Data should be visualised in a simple and attractive way. No overloaded plots an diagrams, we use animation instead.

## Blockchain objects presenting

Blockchain data is too complicated and sometimes not obvious for people. Thus we use adaptive tricks to make work process more convenient:

1. Logical grouping for objects. Every app page has common groups of data (general, blockchain specific) for inheritance of views and better navigation or data observing.
2. Classical accounting terms used for balance and cashflow operations. Blockahains use econimic principles for interaction between subjects thus we can describe such processes in established terms.
3. Robohash logo for contracts entities. Contracts can act by themself, have and algorithms, so it's more natural to perceive them like robots instead of pieces of code.
