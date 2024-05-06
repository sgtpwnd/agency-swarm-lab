const path = require('path');

module.exports = {
  // Entry point of the application
  entry: './background.js',
  
  // Output configuration
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  
  // Module rules and loaders
  module: {
    rules: [
      {
        test: /\.js$/, // Regex to match JavaScript files
        exclude: /node_modules/, // Exclude the node_modules directory
        use: {
          loader: 'babel-loader', // Use babel-loader for transpiling JavaScript
          options: {
            presets: ['@babel/preset-env'] // Preset used for modern JavaScript
          }
        }
      }
    ]
  }
};