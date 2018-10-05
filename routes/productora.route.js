const express = require('express');
const router = express.Router();
const productoraController = require('../controllers/productora.controller');

//rutas

router.post('/create', productoraController.create);
router.get('/readAll', productoraController.readAll);
router.get('/:id/read/', productoraController.readById);
router.put('/:id/update', productoraController.update);
router.delete('/:id/del', productoraController.delete);


module.exports = router;