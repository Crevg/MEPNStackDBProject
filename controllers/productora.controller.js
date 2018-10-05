const Productora = require('../models/productora.model');


exports.create = function(req,res){
    let productora = new Productora({
        nombre: req.body.nombre,
        anno: req.body.anno,
        direccion: req.body.direccion
    });
    productora.save(function(err){
        if (err){
            res.send(err)
        }
        res.send("OK");
    })
};


exports.readAll = function(req, res){
    Productora.find(function (err, productoras){
        if (err){
            res.send(err)
        }
        res.send(productoras);
    });
};

exports.readById = function(req, res){
    Productora.findById(req.params.id, function(err, productora){
        if (err){
            res.send(err);
        }
        res.send(productora);
    });
};

exports.update = function(req, res){
    Productora.findByIdAndUpdate(req.params.id, {$set: req.body}, function(err, productora){
        if (err){
            res.send(err);
        }
        res.send("OK");
    });
}

exports.delete = function(req, res){
    Productora.findByIdAndRemove(req.params.id, function(err){
        if (err){
            res.send(err);
        }
        res.send("OK");
    });
}

