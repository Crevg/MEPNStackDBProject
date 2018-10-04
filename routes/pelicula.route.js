const express = require('express');
const router = express.Router();

const peliculaController = require('../controllers/pelicula.controller');

//rutas del api

router.get('/test', peliculaController.test);
router.post('/create', peliculaController.create);
router.get('/readAll', peliculaController.readAll);/*
router.get('/read:id', peliculaController.readById);
router.put('/update:id', peliculaController.update);
router.delete('del:id', peliculaController.delete);*/

module.exports = router;