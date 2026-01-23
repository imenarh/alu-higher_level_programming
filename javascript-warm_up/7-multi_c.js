#!/usr/bin/node

const arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
  process.exit(0);
}

for (let i = 0; i < arg; i++) {
  console.log('C is fun');
}
