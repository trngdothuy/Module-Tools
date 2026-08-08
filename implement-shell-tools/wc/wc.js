import { program } from "commander";
import { promises as fs } from "node:fs";

program
    .name("wc")
    .description("Word count")
    .option("-l", "Count lines")
    .option("-w", "Count words")
    .option("-c", "Count bytes")
    .argument("<path...>", "Files to process");

program.parse();

const paths = program.args;
const flags = program.opts();

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const path of paths) {
    try {
        const buffer = await fs.readFile(path);
        const content = buffer.toString();

        const lines = content.split("\n").length - 1
        const wordCount = content.trim().split(/\s+/).length
        const bytes = buffer.length;

        totalLines += lines;
        totalWords += wordCount;
        totalBytes += bytes;

        if (flags.l) {
            console.log(`${lines}      ${path}`)
        } else if (flags.w) {
            console.log(`${wordCount}      ${path}`)
        } else if (flags.c) {
            console.log(`${bytes}      ${path}`)
        }
        else {
            console.log(`${lines}      ${wordCount}       ${bytes}      ${path}`)
        }
    } catch (err) {
        console.error(`wc - ${path}: ${err.message}`)
    }
}

if (paths.length > 1) {
    if (flags.l) {
        console.log(`${totalLines}      total`)
    } else if (flags.w) {
        console.log(`${totalWords}      total`)
    } else if (flags.c) {
        console.log(`${totalBytes}      total`)
    } else {
        console.log(`${totalLines}      ${totalWords}      ${totalBytes}      total`)
    }
}
