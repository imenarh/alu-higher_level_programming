#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

for (let i = 0; i < args.length; i++) {
  for (let j = i + 1; j < args.length; j++) {
    if (args[j] > args[i]) {
      const temp = args[i];
      args[i] = args[j];
      args[j] = temp;
    }
  }
}

console.log(args[1]);
