const Pelicula = require('../models/pelicula.model');

//test
exports.test = function(req, res){
    res.send('Working');
};

exports.create = function(req, res){
    let pelicula = new Pelicula({
        nombre: req.body.nombre,
        genero: req.body.genero,
        nombreDirector: req.body.nombreDirector,
        franquicia: req.body.franquicia,
        pais: req.body.pais,
        anno: req.body.anno,
        duracion: req.body.duracion,
        actores: req.body.actores
    });
    pelicula.save(function(err){
        if (err){
            res.send(err)
        }
        res.send('Se insertó el producto');
    })
};


exports.readAll = function(req, res){
    Pelicula.find(function (err, pelis){
        if (err){
            res.send(err)
        }
        res.send(pelis);
    });
};
