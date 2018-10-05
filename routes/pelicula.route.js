const express = require('express');
const router = express.Router();

const peliculaController = require('../controllers/pelicula.controller');

//rutas del api

router.post('/create', peliculaController.create);
router.get('/readAll', peliculaController.readAll);
router.get('/:id/read/', peliculaController.readById);
router.put('/:id/update', peliculaController.update);
router.delete('/:id/del', peliculaController.delete);
router.get('/:titulo/porTitulo', peliculaController.porTitulo);
router.get('/:franquicia/porFranquicia', peliculaController.porFranquicia);
router.get('/:fechaInicial/:fechaFinal/porAnno', peliculaController.porAnno);
router.get('/:productora/porProductora/datos', peliculaController.porProductoraDatos);
router.get('/:productora/porProductora/duraciones', peliculaController.porProductoraDuraciones);
module.exports = router;