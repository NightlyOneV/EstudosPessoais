//Calculadora simples
function calcNum(n1: number, n2: number): number{
    return n1 + n2
}

console.log(calcNum(1,2))

//RGB -> HEX
interface Color {
    red: number;
    green: number;
    blue: number;
}

let cor1: Color = {red: 255, green: 100, blue: 0}

function convertHEX(RGB: Color): string{
    const toHEX = (color: number) => {
        const Hex = color.toString(16)
        return Hex.length === 1 ? 0 + Hex: Hex
    }

    const convHex = `#${toHEX(cor1.red)}${toHEX(cor1.green)}${toHEX(cor1.blue)}`
    return convHex
}

function convertRGB(HEX: string): any{
    HEX = HEX.replace(/^#/, '')

    let _HEX = parseInt(HEX, 16)

    let _R = (_HEX >> 16) & 255
    let _G = (_HEX >> 8) & 255
    let _B = _HEX & 255

    let RGB: Color = {red: _R, green: _G, blue: _B}
    return RGB
}

let cor1_Hex = convertHEX(cor1)
console.log(cor1_Hex)
let cor1_RGB = convertRGB(cor1_Hex)
console.log(cor1.red, cor1.green, cor1.blue)