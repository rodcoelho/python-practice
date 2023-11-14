

# initialize a new Node.js project
# 1 - Creates a package.json file:
#       The heart of any Node.js project. 
#       It contains metadata relevant to the project.
npm init -y

# install webpack, bundles all js files into one file
npm i webpack webpack-cli --save-dev

# install babel, transpiles js into more js friendly to all browsers
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

# install react
npm i react react-dom --save-dev

# material ui, gives us cards and grids (similar to bootstrap)
npm config set legacy-peer-deps true
npm i
npm install @material-ui/core

# to use async and await
npm install @babel/plugin-proposal-class-properties

# allows us to reroute pages within react
npm install react-router-dom

# access to icons from material ui
npm install @material-ui/icons