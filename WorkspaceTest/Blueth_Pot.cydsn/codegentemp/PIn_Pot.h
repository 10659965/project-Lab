/*******************************************************************************
* File Name: PIn_Pot.h  
* Version 2.20
*
* Description:
*  This file contains Pin function prototypes and register defines
*
* Note:
*
********************************************************************************
* Copyright 2008-2015, Cypress Semiconductor Corporation.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
*******************************************************************************/

#if !defined(CY_PINS_PIn_Pot_H) /* Pins PIn_Pot_H */
#define CY_PINS_PIn_Pot_H

#include "cytypes.h"
#include "cyfitter.h"
#include "cypins.h"
#include "PIn_Pot_aliases.h"

/* APIs are not generated for P15[7:6] */
#if !(CY_PSOC5A &&\
	 PIn_Pot__PORT == 15 && ((PIn_Pot__MASK & 0xC0) != 0))


/***************************************
*        Function Prototypes             
***************************************/    

/**
* \addtogroup group_general
* @{
*/
void    PIn_Pot_Write(uint8 value);
void    PIn_Pot_SetDriveMode(uint8 mode);
uint8   PIn_Pot_ReadDataReg(void);
uint8   PIn_Pot_Read(void);
void    PIn_Pot_SetInterruptMode(uint16 position, uint16 mode);
uint8   PIn_Pot_ClearInterrupt(void);
/** @} general */

/***************************************
*           API Constants        
***************************************/
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup driveMode Drive mode constants
     * \brief Constants to be passed as "mode" parameter in the PIn_Pot_SetDriveMode() function.
     *  @{
     */
        #define PIn_Pot_DM_ALG_HIZ         PIN_DM_ALG_HIZ
        #define PIn_Pot_DM_DIG_HIZ         PIN_DM_DIG_HIZ
        #define PIn_Pot_DM_RES_UP          PIN_DM_RES_UP
        #define PIn_Pot_DM_RES_DWN         PIN_DM_RES_DWN
        #define PIn_Pot_DM_OD_LO           PIN_DM_OD_LO
        #define PIn_Pot_DM_OD_HI           PIN_DM_OD_HI
        #define PIn_Pot_DM_STRONG          PIN_DM_STRONG
        #define PIn_Pot_DM_RES_UPDWN       PIN_DM_RES_UPDWN
    /** @} driveMode */
/** @} group_constants */
    
/* Digital Port Constants */
#define PIn_Pot_MASK               PIn_Pot__MASK
#define PIn_Pot_SHIFT              PIn_Pot__SHIFT
#define PIn_Pot_WIDTH              1u

/* Interrupt constants */
#if defined(PIn_Pot__INTSTAT)
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup intrMode Interrupt constants
     * \brief Constants to be passed as "mode" parameter in PIn_Pot_SetInterruptMode() function.
     *  @{
     */
        #define PIn_Pot_INTR_NONE      (uint16)(0x0000u)
        #define PIn_Pot_INTR_RISING    (uint16)(0x0001u)
        #define PIn_Pot_INTR_FALLING   (uint16)(0x0002u)
        #define PIn_Pot_INTR_BOTH      (uint16)(0x0003u) 
    /** @} intrMode */
/** @} group_constants */

    #define PIn_Pot_INTR_MASK      (0x01u) 
#endif /* (PIn_Pot__INTSTAT) */


/***************************************
*             Registers        
***************************************/

/* Main Port Registers */
/* Pin State */
#define PIn_Pot_PS                     (* (reg8 *) PIn_Pot__PS)
/* Data Register */
#define PIn_Pot_DR                     (* (reg8 *) PIn_Pot__DR)
/* Port Number */
#define PIn_Pot_PRT_NUM                (* (reg8 *) PIn_Pot__PRT) 
/* Connect to Analog Globals */                                                  
#define PIn_Pot_AG                     (* (reg8 *) PIn_Pot__AG)                       
/* Analog MUX bux enable */
#define PIn_Pot_AMUX                   (* (reg8 *) PIn_Pot__AMUX) 
/* Bidirectional Enable */                                                        
#define PIn_Pot_BIE                    (* (reg8 *) PIn_Pot__BIE)
/* Bit-mask for Aliased Register Access */
#define PIn_Pot_BIT_MASK               (* (reg8 *) PIn_Pot__BIT_MASK)
/* Bypass Enable */
#define PIn_Pot_BYP                    (* (reg8 *) PIn_Pot__BYP)
/* Port wide control signals */                                                   
#define PIn_Pot_CTL                    (* (reg8 *) PIn_Pot__CTL)
/* Drive Modes */
#define PIn_Pot_DM0                    (* (reg8 *) PIn_Pot__DM0) 
#define PIn_Pot_DM1                    (* (reg8 *) PIn_Pot__DM1)
#define PIn_Pot_DM2                    (* (reg8 *) PIn_Pot__DM2) 
/* Input Buffer Disable Override */
#define PIn_Pot_INP_DIS                (* (reg8 *) PIn_Pot__INP_DIS)
/* LCD Common or Segment Drive */
#define PIn_Pot_LCD_COM_SEG            (* (reg8 *) PIn_Pot__LCD_COM_SEG)
/* Enable Segment LCD */
#define PIn_Pot_LCD_EN                 (* (reg8 *) PIn_Pot__LCD_EN)
/* Slew Rate Control */
#define PIn_Pot_SLW                    (* (reg8 *) PIn_Pot__SLW)

/* DSI Port Registers */
/* Global DSI Select Register */
#define PIn_Pot_PRTDSI__CAPS_SEL       (* (reg8 *) PIn_Pot__PRTDSI__CAPS_SEL) 
/* Double Sync Enable */
#define PIn_Pot_PRTDSI__DBL_SYNC_IN    (* (reg8 *) PIn_Pot__PRTDSI__DBL_SYNC_IN) 
/* Output Enable Select Drive Strength */
#define PIn_Pot_PRTDSI__OE_SEL0        (* (reg8 *) PIn_Pot__PRTDSI__OE_SEL0) 
#define PIn_Pot_PRTDSI__OE_SEL1        (* (reg8 *) PIn_Pot__PRTDSI__OE_SEL1) 
/* Port Pin Output Select Registers */
#define PIn_Pot_PRTDSI__OUT_SEL0       (* (reg8 *) PIn_Pot__PRTDSI__OUT_SEL0) 
#define PIn_Pot_PRTDSI__OUT_SEL1       (* (reg8 *) PIn_Pot__PRTDSI__OUT_SEL1) 
/* Sync Output Enable Registers */
#define PIn_Pot_PRTDSI__SYNC_OUT       (* (reg8 *) PIn_Pot__PRTDSI__SYNC_OUT) 

/* SIO registers */
#if defined(PIn_Pot__SIO_CFG)
    #define PIn_Pot_SIO_HYST_EN        (* (reg8 *) PIn_Pot__SIO_HYST_EN)
    #define PIn_Pot_SIO_REG_HIFREQ     (* (reg8 *) PIn_Pot__SIO_REG_HIFREQ)
    #define PIn_Pot_SIO_CFG            (* (reg8 *) PIn_Pot__SIO_CFG)
    #define PIn_Pot_SIO_DIFF           (* (reg8 *) PIn_Pot__SIO_DIFF)
#endif /* (PIn_Pot__SIO_CFG) */

/* Interrupt Registers */
#if defined(PIn_Pot__INTSTAT)
    #define PIn_Pot_INTSTAT            (* (reg8 *) PIn_Pot__INTSTAT)
    #define PIn_Pot_SNAP               (* (reg8 *) PIn_Pot__SNAP)
    
	#define PIn_Pot_0_INTTYPE_REG 		(* (reg8 *) PIn_Pot__0__INTTYPE)
#endif /* (PIn_Pot__INTSTAT) */

#endif /* CY_PSOC5A... */

#endif /*  CY_PINS_PIn_Pot_H */


/* [] END OF FILE */
