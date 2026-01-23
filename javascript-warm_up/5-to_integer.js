#!/usr/bin/node

const arg = process.argv[2];

const output = Number(arg);

if (!arg || isNaN(output)) {
  console.log('Not a number');
  process.exit(0);
}

console.log(`My number: ${output}`);
