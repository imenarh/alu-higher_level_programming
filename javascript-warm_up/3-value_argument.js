#!/usr/bin/node

const { argv } = require('node:process');

argv.forEach((val, index) => {
	if (index <= 1) {
	  console.log('No argument');
	  process.exit(0);
	}else{
	  console.log(val);
	}
});
