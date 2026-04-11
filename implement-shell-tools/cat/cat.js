import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("cat")
    .description("Reading the file and print the content")
    .option("-n", "Number all lines")
    .option("-b", "Number only lines with content")
    .argument("<path...>", "The file path to process");

program.parse();

const paths = program.args;
const flags = program.opts();
// console.log(flags)

for (const path of paths) {
    try {
        const content = await fs.readFile(path, "utf-8");
        const lines = content.split("\n");
        lines.pop()
        // console.log("lines", lines)
        let lineNum = 1;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            if (flags.n) {
                console.log(`${lineNum}  ${line}`)
                lineNum++
            } else if (flags.b) {
                if (line != "") {
                    console.log(`${lineNum} ${line}`)
                    lineNum++
                }
            }
            else {
                console.log(line)
            }
        }
    } catch (err) {
        console.error(`${path}: ${err.message}`)
    }
}
