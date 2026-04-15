import { program } from "commander";
import { promises as fs } from "node:fs";

program
    .name("ls")
    .description("List all files name")
    .option("-1", "A new line for each file")
    .option("-a", "Show hidden files")
    .argument("[path]", "The directory to list");

program.parse();

let path = "";
program.args.length == 0 ? path = '.' : path = program.args[0];
const flags = program.opts()

try {
    let files = await fs.readdir(path);
    if (!flags["a"]) {
        files = files.filter(file => !file.startsWith("."))
    }
    if (flags["1"]) {
        console.log(files.join("\n"));
    } else {
        console.log(files.join("       "));
    }
} catch (err) {
    console.error(`ls - ${path}: ${err.message}`)
}
