const mongoose = require('mongoose');
const Schema =  mongoose.Schema;

let ProductoraSchema = new Schema({
    nombre: {type: String, required: true, max: 50},
    anno: {type: Number, required: true},
    direccion: {type: String , required: true, max: 50},
});

//Exportar el model
module.exports = mongoose.model('Productora', ProductoraSchema);

