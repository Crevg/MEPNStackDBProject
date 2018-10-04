const mongoose = require('mongoose');
const Schema =  mongoose.Schema;

let PeliculaSchema = new Schema({
    nombre: {type: String, required: true, max: 50},
    genero: {type: String, required: true, max: 50},
    nombreDirector: {type: String, required: true, max: 50},
    franquicia: {type: String, required: false, max: 50},
    pais: {type: String, required: true, max: 50},
    anno: {type: Number, required: true},
    duracion: {type: Number , required: true},
    actores: {type: [String], required: true},
});

//Exportar el model
module.exports = mongoose.model('Pelicula', PeliculaSchema);

