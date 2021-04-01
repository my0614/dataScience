const express = require('express');
const router = express.Router();
const cv = require("opencv")

/* GET home page. */
router.get('/', function(req, res, next) {
  cv.readImage(__dirname + '/../public/images/jesus2.jpg', function (err, img) {
    if (err) throw err;

    let width = img.width();
    let height = img.height();
    if (width < 1 || height < 1) {
      throw new Error('Image has no size');
    }

    img.convertGrayscale();
    img.gaussianBlur([3, 3]);
    img.save(__dirname + '/../public/img/newFoo.png');
  })

  res.render("index",{ title: "express"})
});

module.exports = router;