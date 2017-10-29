var path = require('path')
var webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')

const PRODUCTION = process.env.NODE_ENV === 'production'

console.log('Production mode?', PRODUCTION)

const productionEntry = ['./src/index.tsx']

function getPlugins() {
    const prodOnlyPlugins = [
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false,
                screw_ie8: true,
                // drop_console: true,
                drop_debugger: true
            }
        })
    ]
    const basePlugins = [
        new webpack.optimize.OccurrenceOrderPlugin(true),

        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor',
            minChunks: (module) => module.context && module.context.indexOf('node_modules') !== -1,
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'manifest',
        }),
        new HtmlWebpackPlugin({
            template: './src/index.html',
        }),
    ]
    const devOnlyPlugins = [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NamedModulesPlugin(),
    ]
    if (PRODUCTION) {
        return [...prodOnlyPlugins, ...basePlugins]
    }

    return [...devOnlyPlugins, ...basePlugins]
}

module.exports = {
    devtool: (!PRODUCTION) ? process.env.WEBPACK_DEVTOOL || 'source-map' : undefined,
    devServer: (!PRODUCTION) ? {
        historyApiFallback: true,
        hotOnly: true,
        host: '0.0.0.0',
        hot: true,
        port: parseInt(process.env.NODE_PORT, 10) || 3000,
    } : undefined,
    entry: {
        main: PRODUCTION ? productionEntry : [
            'react-hot-loader/patch',
            './src/index.tsx', // your app's entry point
        ],
    },
    output: {
        path: path.join(__dirname, 'dist'),
        // filename: 'bundle.js',
        filename: '[name].js',
        publicPath: '/'
    },
    resolve: {
        alias: {'@src': path.resolve(__dirname, './src')},
        extensions: ['.js', '.jsx', '.ts', '.tsx'],
    },
    plugins: getPlugins(),
    module: {
        rules: [
            {
                test: /\.(t|j)sx?$/,
                exclude: /node_modules/,
                include: path.resolve(__dirname, './src'),
                use: PRODUCTION ? [
                    'awesome-typescript-loader',
                ] : [
                    'react-hot-loader/webpack',
                    'awesome-typescript-loader',
                ]
            },
            { enforce: "pre", test: /\.js$/, loader: "source-map-loader" }
        ]
    }
}
