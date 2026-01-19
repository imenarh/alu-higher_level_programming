#!/usr/bin/node

const { argv } = require('node:process');

let num;
argv.forEach((val, index) => {
  num=index;	
});

if (num <= 1) {
  console.log('No argument');
}else {
 console.log(argv[2]);
}
