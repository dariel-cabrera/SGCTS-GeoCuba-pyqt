import { IsNumber,IsNotEmpty } from "class-validator"
export class CreateCalculoDto{

        @IsNumber()
        @IsNotEmpty()
        densidad_a:number

        @IsNumber()
        @IsNotEmpty()
        densidad_m: number
        
        @IsNumber()
        @IsNotEmpty()
        indice: number
        
        @IsNumber()
        @IsNotEmpty()
        coeficiente:number

        @IsNumber()
        @IsNotEmpty()
        altura:number

        @IsNumber()
        @IsNotEmpty()
        angulo:number

        @IsNumber()
        @IsNotEmpty()
        aceleracion:number

        @IsNumber()
        @IsNotEmpty()
        P:number

        @IsNumber()
        @IsNotEmpty()
        K:number
}