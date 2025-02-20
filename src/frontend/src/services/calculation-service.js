import HttpService from "./htttp.service";

class  CalculationService {
    getCalculation=async()=>{
        const getCalculation="getCalculation";
        return await HttpService.get(getCalculation);
    }




}

export default new CalculationService();