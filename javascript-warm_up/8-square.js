#!/usr/bin/node

const arg = Number(process.argv[2]);

if (isNaN(arg)) {
	console.log("Missing size");
	process.exit(0);
}

for (let i=0; i<arg; i++) {
	console.log("X".repeat(arg));
}
