var webpack = require('webpack'); //use ES6 verbage. Make variable webpack to require local webpack
module.exports = {
  //webpack everything (loaders, plugins, read files, all go here)
  //entry is an array of all the locations of js files, can have multiple
  entry: [
    './javascripts/main.js',
    './javascripts/file2.js'
  ],
  //bundle file: js file that webpack generates
  output: {
      filename: 'bundle.js', //what we watnt to call the bundle (anything we want)
      path: './javascripts' //where we want to put the bundle
  },
  //my extras that I am adding to webpack's process, in this case just minifying
  plugins: [
    new webpack.optimize.UglifyJsPlugin() //this will minify modules using webpack variable
  ],
  //define my loaders for preprocessed files, in this case we only want to use the babel preprocessor 
  module: { //this is the babel loader. says for any files with .js extension (except for node modules directory), have babel read them
    loaders: [
      {
        test: /\.js$/, //target any files with .js extension.
        exclude: /(node_modules|bower_components)/, //ignore files in node modules directory
        loader: 'babel-loader', //have babel read targeted js files
        query: {
          presets: ['es2015']
        }
      }
    ]
  }
}
