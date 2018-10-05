// dependencies
const express = require('express');
const bodyParser = require ('body-parser');
const cors = require('cors')



// init app

const app = express();


//bodyparser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(cors({credentials:true, origin: true}))

//rutas
const pelicula = require('./routes/pelicula.route'); 
app.use('/peliculas', pelicula);

const productora = require('./routes/productora.route');
app.use('/productoras', productora);

//port 
let port = 3000
app.listen(port, () => console.log('Server is running on port ' + port))

//Mongo

//Import the mongoose module
var mongoose = require('mongoose');
//Set up default mongoose connection
var mongoDB = "mongodb://localhost:27017/Pelis";
mongoose.connect(mongoDB);
// Get Mongoose to use the global promise library
mongoose.Promise = global.Promise;
//Get the default connection
let db = mongoose.connection;
//Bind connection to error event (to get notification of connection errors)
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
