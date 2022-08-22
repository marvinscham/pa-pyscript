async function main() {
    let pyodide = await loadPyodide();
    // Pyodide is now ready to use...
    console.log(pyodide.runPython(`
      import sys
      sys.version
    `));
}
main();

// Source: https://pyodide.org/en/stable/usage/quickstart.html