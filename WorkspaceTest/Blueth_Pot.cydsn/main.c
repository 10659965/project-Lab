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
#include "project.h"
#include "stdio.h"
#include "interrupt_routine.h"



void SendData(){
        if(PacketReadyFlag==1){
        //instert function for usb module
        // UART_BlueT_PutString("PacketreadyFlag=1\r\n");
        UART_BlueT_PutString(DataBuffer);
        //reset the value Packet read to 0 
        PacketReadyFlag=0;
        }
    }




int main(void)
{
    CyGlobalIntEnable; /* Enable global interrupts. */
    Timer_ADC_Enable();//Enable timer
    Timer_ADC_Start();//start timer(porcodio)
    ADC_Pot_Start();//Start ADC
    isr_TimerADC_inter_StartEx(Custom_ISR_ADC_inter);
    isr_RX_inter_StartEx(Custom_ISR_RX_inter);//start esecution interrupt
    PacketReadyFlag=0;//set flag packet to 0
    ADC_Pot_StartConvert();//start convertion of the adc
    UART_BlueT_Start();//start the UART module
    
    UART_BlueT_PutString("UART BlueThoot Module HC-06\r\n");//init string 

    /* Place your initialization/startup code here (e.g. MyInst_Start()) */

    for(;;)
    {
        //control Rx to associate application
      
    
       if(RxFlag_Start==0){ UART_BlueT_PutString("READY\r\n");
                               
                                CyDelay(1000);}
       
        //if connection is done send the datas
       while(RxFlag_Start){ 
            SendData();
       }
        
       
    }
}





/* [] END OF FILE */
