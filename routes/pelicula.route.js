const express = require('express');
const router = express.Router();

const peliculaController = require('../controllers/pelicula.controller');

//rutas del api

router.get('/test', peliculaController.test);
router.post('/create', peliculaController.create);
router.get('/readAll', peliculaController.readAll);


module.exports = router;