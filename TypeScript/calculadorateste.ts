class Calculadora {
    numerosCalc: Array<number> = []

    inserir(num: number) {
        this.numerosCalc.push(num)
    }

    limpar(){
        this.numerosCalc = []
    }

    consultar(){
        let nums: string = ""

        for (let numAtual of this.numerosCalc){
            nums = nums + ", "+numAtual
        }

        console.log(`O Valor armazenado na calculadora atualmente é: ${nums}`)
    }

    somar(){
        let resultado: number = 0

        for (let numAtual of this.numerosCalc){
            resultado += numAtual
        }

        console.log(`O Resultado foi: ${resultado}`)
    }

    subtrair(){
        let resultado: number = this.numerosCalc[0]

        for (let numAtual of this.numerosCalc){
            resultado -= numAtual
        }

        console.log(`O Resultado foi ${resultado}`)
    }

    multiplicar(){
        let resultado: number = 1

        for (let numAtual of this.numerosCalc){
            resultado *= numAtual
        }

        console.log(`O Resultado foi ${resultado}`)

    }

}

const Calc = new Calculadora()
Calc.inserir(10)
Calc.inserir(14)
Calc.inserir(2)
Calc.inserir(3)
Calc.consultar()
Calc.somar()
Calc.subtrair()
Calc.multiplicar()