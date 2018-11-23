#include "p16f887.inc"

; CONFIG1
; __config 0xE0F4
 __CONFIG _CONFIG1, _FOSC_INTRC_NOCLKOUT & _WDTE_OFF & _PWRTE_OFF & _MCLRE_OFF & _CP_OFF & _CPD_OFF & _BOREN_OFF & _IESO_OFF & _FCMEN_OFF & _LVP_OFF
; CONFIG2
; __config 0xFFFF
 __CONFIG _CONFIG2, _BOR4V_BOR40V & _WRT_OFF
;*********
   GPR_VAR        UDATA
   W_TEMP         RES        1      ; w register for context saving (ACCESS)
   STATUS_TEMP    RES        1      ; status used for context saving
   DELAY1	  RES	     1
   DELAY2	  RES	     1
   CERVO1	  RES	     1	    ;VARIABLE ADC 1
   CERVO2	  RES	     1	    ;VARIABLE ADC 2
   CERVO3	  RES	     1	    ;VARIABLE ADC 3
   CERVO4	  RES	     1	    ;VARIABLE ADC 4
   MANUAL3	  RES	     1	    ;SERVO MANUAL 1
   MANUAL4	  RES	     1	    ;SERVO MANUAL 2
   CONTADOR	  RES	     1      ;Variable control
   CONTADOR1	  RES	     1
;*********
; Reset Vector
;*********

RES_VECT  CODE    0x0000            ; processor reset vector
    GOTO    START                   ; go to beginning of program

;*********
ISR       CODE    0x0004           ; interrupt vector location
PUSH:
    MOVWF   W_TEMP
    SWAPF   STATUS, 0
    MOVWF   STATUS_TEMP

ISR:
    BTFSC   INTCON, T0IF
    CALL    MANUAL_PWM
    GOTO    POP
   
POP:
    SWAPF   STATUS_TEMP, 0
    MOVWF   STATUS
    SWAPF   W_TEMP, F
    SWAPF   W_TEMP, W
    RETFIE
     
;-------------------------------------------------------------------------------
; MAIN PROGRAM
    MAIN_PROG CODE                      ; let linker place main program

START
;-------------------CONFIGURACIONES---------------------------------------------
    CALL    CONFIG_RELOJ	    ; RELOJ INTERNO DE 2Mhz
    CALL    CONFIG_IO
    CALL    CONFIG_TX_RX	    ; 10417hz
    CALL    CONFIG_ADC		    ; canal 0, fosc/8, adc on, justificado a la izquierda, Vref interno (0-5V)
    CALL    CONFIG_TMR0
    CALL    CONFIG_INT_TMR0
    BANKSEL PORTA 
;---------------------------LOOP-----------------------------------------------    
    LOOP:
;---------------------------CANAL 0--------------------------------------------
    BCF	    ADCON0, CHS3	   
    BCF	    ADCON0, CHS2
    BCF	    ADCON0, CHS1
    BCF	    ADCON0, CHS0
    
    CALL    DELAY_50MS
    BSF	    ADCON0, GO		    ; EMPIEZA LA CONVERSIÓN
CHECK_AD0:
    BTFSC   ADCON0, GO		    ; revisa que terminó la conversión
    GOTO    CHECK_AD0
    BCF	    PIR1, ADIF		    ; borramos la bandera del adC
    RRF	    ADRESH, F
    RRF	    ADRESH, F
    RRF	    ADRESH, W		; LE QUITAMOS LOS 3 BITS MENOS SIGNIFICATIVOS A LA CONVERSION
    ANDLW   B'00011111'
    MOVWF   CERVO1		    ; MOVEMOS EL VALOR HACIA VARIABLE CCP1

CHECK_TXIF: 
    MOVLW   .169		    ; ENVÍA PORTB POR EL TX
    MOVWF   TXREG
    
    BTFSS   PIR1, TXIF
    GOTO    $-1

;;----------------------------CANAL 1--------------------------------------------   
;    BCF	    ADCON0, CHS3	   
;    BCF	    ADCON0, CHS2
;    BCF	    ADCON0, CHS1
;    BSF	    ADCON0, CHS0
;    CALL    DELAY_50MS
;    BSF     ADCON0, GO		    ; EMPIECE LA CONVERSIÓN
;
;CHECKADC1:
;    BTFSC   ADCON0, GO		    ; LOOP HASTA QUE TERMINE DE CONVERTIR
;    GOTO    CHECKADC1
;    BCF	    PIR1, ADIF		    ; BORRAMOS BANDERA DE INTERRUPCION
;    MOVFW   ADRESH
;    MOVWF   CERVO2		    ; MOVEMOS EL VALOR HACIA VARIABLE	CCP1
;    
;;----------------------------CANAL 2--------------------------------------------    
;    BCF	    ADCON0, CHS3	    ; CANAL 2 PARA LA CONVERSION
;    BCF	    ADCON0, CHS2
;    BSF	    ADCON0, CHS1
;    BCF	    ADCON0, CHS0
;    CALL    DELAY_50MS
;    BSF     ADCON0, GO		    ; EMPIECE LA CONVERSIÓN
;
;CHECKADC2:
;    BTFSC   ADCON0, GO		    ; LOOP HASTA QUE TERMINE DE CONVERTIR
;    GOTO    CHECKADC2
;    BCF	    PIR1, ADIF		    ; BORRAMOS BANDERA DE INTERRUPCIÓN
;    MOVFW   ADRESH
;    MOVWF   CERVO3		    ; MOVEMOS EL VALOR HACIA VARIABLE	CCP1
;    
;;----------------------------CANAL 3--------------------------------------------    
;    BCF	    ADCON0, CHS3	    ; CANAL 3 PARA LA CONVERSION
;    BCF	    ADCON0, CHS2
;    BSF	    ADCON0, CHS1
;    BSF	    ADCON0, CHS0
;    CALL    DELAY_50MS
;    BSF     ADCON0, GO		    ; EMPIECE LA CONVERSIÓN
;
;CHECKADC3:
;    BTFSC   ADCON0, GO		    ; LOOP HASTA QUE TERMINE DE CONVERTIR
;    GOTO    CHECKADC3
;    BCF	    PIR1, ADIF		    ; BORRAMOS BANDERA DE INTERRUPCION
;    MOVFW   ADRESH
;    MOVWF   CERVO4		    ; MOVEMOS EL VALOR HACIA VARIABLE
;    
    
    
    GOTO LOOP
    
    
MANUAL_PWM
    BCF	    INTCON, GIE
    BCF	    INTCON, T0IF
    MOVLW   .177
    MOVWF   TMR0
    INCF    CONTADOR
    MOVLW   .255
    XORWF   CONTADOR,W
    BTFSC   STATUS, Z
    CALL    LIMPIA
    MOVFW   CERVO1
    XORWF   CONTADOR,W
    BTFSC   STATUS, Z
    BCF	    PORTD,0
    MOVFW   CERVO2
    XORWF   CONTADOR,W
    BTFSC   STATUS, Z
    BCF	    PORTD,1
    MOVFW   CERVO3
    XORWF   CONTADOR,W
    BTFSC   STATUS, Z
    BCF	    PORTD,2
    MOVFW   CERVO4
    XORWF   CONTADOR,W
    BTFSC   STATUS, Z
    BCF	    PORTD,3
    BSF	    INTCON, GIE
    RETURN
    
LIMPIA
    CLRF    CONTADOR
    BSF	    PORTD,0
    BSF	    PORTD,1
    BSF	    PORTD,2
    BSF	    PORTD,3
    RETURN
    
 
;-------------------------CONFIGURACIONES---------------------------------------
CONFIG_IO
    BANKSEL TRISA
    CLRF    TRISA
    BSF	    TRISA, RA0	; RA0 COMO ENTRADA
    BSF	    TRISA, RA1	; RA1 COMO ENTRADA
    BSF	    TRISA, RA2	; RA2 COMO ENTRADA
    BSF	    TRISA, RA3	; RA3 COMO ENTRADA
    CLRF    TRISC
    CLRF    TRISD
    CLRF    TRISB
    BANKSEL ANSEL
    CLRF    ANSEL
    BSF	    ANSEL, 0	; ANS0 COMO ENTRADA ANALÓGICA
    BSF	    ANSEL, 1	; ANS1 COMO ENTRADA ANALÓGICA
    BSF	    ANSEL, 2	; ANS0 COMO ENTRADA ANALÓGICA
    BSF	    ANSEL, 3	; ANS1 COMO ENTRADA ANALÓGICA
    CLRF    ANSELH
    BANKSEL PORTA
    CLRF    PORTA
    CLRF    PORTC
    CLRF    PORTB
    CLRF    PORTD
    CLRF    CERVO1
    CLRF    CERVO2
    CLRF    CERVO3
    CLRF    CERVO4
    RETURN    
    
;------------------------------RELOJ--------------------------------------------
    CONFIG_RELOJ
    BANKSEL OSCCON
    
    BSF OSCCON, IRCF2
    BSF OSCCON, IRCF1
    BSF OSCCON, IRCF0		    
    RETURN
;---------------------CONFIGURACION ADC-----------------------------------------
    CONFIG_ADC
    BANKSEL ADCON0
    BSF ADCON0, ADCS1
    BCF ADCON0, ADCS0		
    
    BANKSEL ADCON1
    BCF ADCON1, ADFM		; JUSTIFICACIÓN A LA IZQUIERDA
    BCF ADCON1, VCFG1		; VSS COMO REFERENCIA VREF-
    BCF ADCON1, VCFG0		; VDD COMO REFERENCIA VREF+
    
    BANKSEL PORTA
    BSF ADCON0, ADON		; ENCIENDO EL MÓDULO ADC
    
    RETURN
    
 ;----------------------------CONFIGURACION SERIAL------------------------------
CONFIG_TX_RX
    BANKSEL BAUDCTL
    BSF	    BAUDCTL,BRG16
    
    BANKSEL TXSTA
    BCF	    TXSTA,TX9
    BCF	    TXSTA,SYNC
    BSF	    TXSTA,BRGH
    BSF	    TXSTA,TXEN
    
    BANKSEL SPBRG
    MOVLW   .207	; BAUDRATE 9600
    MOVWF   SPBRG
    CLRF    SPBRGH
    
    
    BANKSEL RCSTA
    BCF	    RCSTA,RX9
    BSF	    RCSTA,CREN
    BSF	    RCSTA,SPEN
    
    BANKSEL PIR1
    BCF	    PIR1,RCIF
    BCF	    PIR1,TXIF
    
    RETURN
;----------------------------DELAYS---------------------------------------------
DELAY_50MS
    MOVLW   .200		    ; 1US 
    MOVWF   DELAY2
    CALL    DELAY_500US
    DECFSZ  DELAY2		    ;DECREMENTA CONT1
    GOTO    $-2			    ; IR A LA POSICION DEL PC - 1
    RETURN
    
DELAY_500US
    MOVLW   .250		    ; 1US 
    MOVWF   DELAY1	    
    DECFSZ  DELAY1		    ;DECREMENTA CONT1
    GOTO    $-1			    ; IR A LA POSICION DEL PC - 1
    RETURN
;----------------------------PWM------------------------------------------------
    
;----------------------------INTERRUPCIONES TMR0--------------------------------
CONFIG_INT_TMR0
    
    BANKSEL PORTA
    BSF	    INTCON, GIE
    BSF	    INTCON, T0IE
    BCF	    INTCON, T0IF
    BCF	    INTCON, PEIE
    BCF	    INTCON, INTE
    BCF	    INTCON, RBIE
    BCF	    INTCON, INTF
    BCF	    INTCON, RBIF
    RETURN
    
CONFIG_TMR0
    BANKSEL OPTION_REG
    BCF	    OPTION_REG,T0CS	; INTERNAL CYCLE CLOCK
    BCF	    OPTION_REG,T0SE	; INCREMENT LOW-TO-HIGH
    BCF	    OPTION_REG,PSA	; PRESCALES ASIGNADO A TMR0
    
    BCF	    OPTION_REG,PS2
    BCF	    OPTION_REG,PS1
    BSF	    OPTION_REG,PS0	; PRESCALER DE 1:4

    BANKSEL INTCON
    BSF	    INTCON,T0IE		; ENABLE TMR0 
    
    BANKSEL TMR0
    CLRF    TMR0
    MOVLW   .177
    MOVWF   TMR0
    
    RETURN
    
    END