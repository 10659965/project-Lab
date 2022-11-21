/* ========================================
 *
 * Copyright YOUR COMPANY, THE YEAR
 * All Rights Reserved
 * UNPUBLISHED, LICENSED SOFTWARE.
 *
 * CONFIDENTIAL AND PROPRIETARY INFORMATION
 * WHICH IS THE PROPERTY OF your company.
 *
 * ========================================
*/
#include "interrupt_routine.h"
#include "project.h"


int32 Value_Digit,Value_mV;
char statusrx;





CY_ISR(Custom_ISR_ADC_inter){
     //Reset Timer Register For ISR
     Timer_ADC_ReadStatusRegister();
     //Read vhe value of the Potentiometer
     Value_Digit=ADC_Pot_Read32();//vlues in digits
     //constrain the value_digit to the + range
     if(Value_Digit<0) Value_Digit=0;
     if(Value_Digit>65535) Value_Digit=65535;
    
        
     Value_mV=ADC_Pot_CountsTo_mVolts(Value_Digit);//Vdd=5V
     //Put in DataBuffer the result of convertion   
     sprintf(DataBuffer, "Sample: %ld mV\r\n",Value_mV);
    //set value of packet received to 1
     PacketReadyFlag=1;
     
 }

CY_ISR(Custom_ISR_RX_inter){
    statusrx=UART_BlueT_GetChar();
    if(statusrx){
        RxFlag_Start=1;
    }
    
}






/* [] END OF FILE */
