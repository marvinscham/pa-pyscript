(module
    (func $i (import "imports" "imported_func") (param i32))
    (func (export "exported_func")
        i32.const 42
        call $i
    )
)

;; Source: https://developer.mozilla.org/en-US/docs/WebAssembly/Text_format_to_wasm