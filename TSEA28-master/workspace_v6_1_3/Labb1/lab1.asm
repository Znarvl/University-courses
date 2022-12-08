
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 
;; Mall för lab1 i TSEA28 Datorteknik Y
;;
;; 190123 K.Palmkvist
;;

	;; Ange att koden är för thumb mode
	.thumb
	.text
	.align 2

	;; Ange att labbkoden startar här efter initiering
	.global	main
	
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 	Placera programmet här

main: 		; Start av programmet
		bl inituart
		bl initGPIOF
		bl initGPIOB
		bl printchar
		b START



; MEM 0x20001000–0x20001003
;Code 0x20001010–0x20001013
felmed:	.string "Felaktig kod!",10,13

START:
	bl setpassword

	;testing
	;bl deactivatealarm ;OK
	;bl printstring ;OK
	;bl getkey ;OK
	;bl checkcode ;OK

	;bl addkey ; Ok
	;bl setpassword ;ok
	;bl getkey ;ok
	;bl clearinput

mainloop:
	  ;logiskt att rensa inputs och sätta på alarm

	bl activatealarm
clearloop:
	bl clearinput
waitkeypress:
	mov r1,#(GPIOB_GPIODATA & 0xffff)
	movt r1,#(GPIOB_GPIODATA >> 16)

	ldr r0, [r1]
	ands r0, #0x10
	beq waitkeypress
waitkeyrelease:
	ldr r0, [r1]
	ands r0, #0x10
	bne waitkeyrelease
storekeys:
	bl getkey
	;bl addkey ; NYTT
	cmp r4, #9
	bls keyisnumber

	cmp r4, #0x0f ;NYTT
	beq checkpassword ;NYTT L�gger till nya knappar tills sista blir F

	;G�r n�got HALP LUDDEH
	b waitkeypress

keyisnumber:
	bl addkey
	b waitkeypress


checkpassword:
	bl checkcode  ;NYTT VET INTE OM BEQ med BNE FUNKAR MEN BRA MINDMAP
	beq correctcode
	b wrongcode

wrongcode:
	bl printstring



	b mainloop

	;cmp r4, check

	;cmp r4,#0x0a
	;beq lettera

	;If the program has not jumped yet the key is a letter thats not f




correctcode:
	bl deactivatealarm
	bl clearinput
bokstav_a: ;FUNKAR NYTT
	bl getkey

	CMP r4,#0x0a
	BNE bokstav_a
restart:
	b mainloop
	;bl setpassword
	;bl getkey
	;bl addkey
	;bl checkcode
	;bl printstring

;;;;;;;;;tester;;;;;;;;;;;;;;;
;printchar
endloop:
;FIXA
	;mov r0
	bl printchar
	b endloop
	;test initGPIOB
endloop2:
	bl initGPIOB
	b endloop2
	; initGPIOF
endloop3:
	bl  initGPIOF
	b endloop3
;printstring
endloop4:
;FIXA
	bl inituart
	mov r4, #0x00c0
	;movt t4, #0x0100
	mov r5, #13
	bl printstring
	b endloop4
;activate alarm
endloop5:
	bl initGPIOF
	bl activatealarm
	b endloop5
;deactivate alarm
endloop6:
	bl initGPIOF
	bl deactivatealarm
	b endloop6

;getkey
endloop7:
	bl getkey
	b endloop7










;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;subrutiner

setpassword:
	mov r0, #(0x20001010 & 0xffff)
	movt r0, #(0x20001010 >> 16)
	mov r1, #7 ;nummer 7
	str r1, [r0], #1
	mov r1, #9
	str r1, [r0], #1
	mov r1, #5
	str r1 , [r0], #1
	mov r1, #3
	str r1, [r0]
	bx lr

printstring:
	mov r5, #15
	adr r4, felmed
printloop: ; ldrb
	ldr r0, [r4], #1
	push{lr}
	bl printchar
	;LSL r0, r0, #8
	subs r5, r5, #1
	cmp r5, #0x00
	pop{lr}
	bne printloop
	bx lr

deactivatealarm:
	mov r1,#(GPIOF_GPIODATA & 0xffff)
	movt r1,#(GPIOF_GPIODATA >> 16) ;flyttar 16 bit
	mov r0, #8 ;3bit 1000
	str r0, [r1]
	bx lr


activatealarm:
	mov r1,#(GPIOF_GPIODATA & 0xffff)
	movt r1,#(GPIOF_GPIODATA >> 16)
	mov r0, #2 ;1bit  0010
	str r0, [r1]; whats in r0 to the adress that r1 is pointing to

	bx lr

;atkey:
	;mov r0, #(GPIOB_GPIODATA >> 16)
	;cmp r0, r1 ;jämför r0 och r1
	;beq atkey ;branch if equal

getkey:
	mov r1,#(GPIOB_GPIODATA & 0xffff) ;titta sista 4 bitar, sätter 0 på rest
	movt r1,#(GPIOB_GPIODATA >> 16)

	ldrb r4,[r1] ;Load register byte (hämtar bits lägger i annan)
	bx lr



addkey: ; indata r4, f�rst�r

	mov r0,#0x1000
	movt r0,#0x2000


	;bge ost
	ldr r1, [r0]
	LSL r1, r1, #8

	str r1, [r0]
	strb r4, [r0]

	bx lr

clearinput:
	mov r0, #0xFFFF
	movt r0, #0xFFFF

	mov r1, #0x1000
	movt r1, #0x2000

	str r0, [r1]
	bx lr
clearinput1:
	mov r0,#0xFF
	mov r1,#0x1000
	movt r1,#0x2000
	mov r1, r0
	mov r2,#0x1001
	movt r2,#0x2000
	mov r2, r0
	mov r3, #0x1002
	movt r3,#0x2000
	mov r3, r0
	mov r4, #1003
	movt r4, #2000
	mov r4, r0

	bx lr


checkcode:
	mov r0, #(0x20001000 & 0xffff)
	movt r0, #(0x20001000 >> 16)
	ldr r1, [r0]
	mov r0, #(0x20001010 & 0xffff)
	movt r0, #(0x20001010 >> 16)
	ldr r2, [r0]
	cmp r1, r2
	beq deactivatealarm
	bx lr






;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
;;;
;;; Allt här efter ska inte ändras
;;;
;;; Rutiner för initiering
;;; Se labmanual för vilka namn som ska användas
;;;
	
	.align 4

;; 	Initiering av seriekommunikation
;;	Förstör r0, r1 
	
inituart:
	mov r1,#(RCGCUART & 0xffff)		; Koppla in serieport
	movt r1,#(RCGCUART >> 16)
	mov r0,#0x01
	str r0,[r1]

	mov r1,#(RCGCGPIO & 0xffff)
	movt r1,#(RCGCGPIO >> 16)
	ldr r0,[r1]
	orr r0,r0,#0x01
	str r0,[r1]		; Koppla in GPIO port A

	nop			; vänta lite
	nop
	nop

	mov r1,#(GPIOA_GPIOAFSEL & 0xffff)
	movt r1,#(GPIOA_GPIOAFSEL >> 16)
	mov r0,#0x03
	str r0,[r1]		; pinnar PA0 och PA1 som serieport

	mov r1,#(GPIOA_GPIODEN & 0xffff)
	movt r1,#(GPIOA_GPIODEN >> 16)
	mov r0,#0x03
	str r0,[r1]		; Digital I/O på PA0 och PA1

	mov r1,#(UART0_UARTIBRD & 0xffff)
	movt r1,#(UART0_UARTIBRD >> 16)
	mov r0,#0x08
	str r0,[r1]		; Sätt hastighet till 115200 baud
	mov r1,#(UART0_UARTFBRD & 0xffff)
	movt r1,#(UART0_UARTFBRD >> 16)
	mov r0,#44
	str r0,[r1]		; Andra värdet för att få 115200 baud

	mov r1,#(UART0_UARTLCRH & 0xffff)
	movt r1,#(UART0_UARTLCRH >> 16)
	mov r0,#0x60
	str r0,[r1]		; 8 bit, 1 stop bit, ingen paritet, ingen FIFO
	
	mov r1,#(UART0_UARTCTL & 0xffff)
	movt r1,#(UART0_UARTCTL >> 16)
	mov r0,#0x0301
	str r0,[r1]		; Börja använda serieport

	bx  lr

; Definitioner för registeradresser (32-bitars konstanter) 
GPIOHBCTL	.equ	0x400FE06C
RCGCUART	.equ	0x400FE618
RCGCGPIO	.equ	0x400fe608
UART0_UARTIBRD	.equ	0x4000c024
UART0_UARTFBRD	.equ	0x4000c028
UART0_UARTLCRH	.equ	0x4000c02c
UART0_UARTCTL	.equ	0x4000c030
UART0_UARTFR	.equ	0x4000c018
UART0_UARTDR	.equ	0x4000c000
GPIOA_GPIOAFSEL	.equ	0x40004420
GPIOA_GPIODEN	.equ	0x4000451c
GPIOB_GPIODATA	.equ	0x400053fc
GPIOB_GPIODIR	.equ	0x40005400
GPIOB_GPIOAFSEL	.equ	0x40005420
GPIOB_GPIOPUR	.equ	0x40005510
GPIOB_GPIODEN	.equ	0x4000551c
GPIOB_GPIOAMSEL	.equ	0x40005528
GPIOB_GPIOPCTL	.equ	0x4000552c
GPIOF_GPIODATA	.equ	0x4002507c
GPIOF_GPIODIR	.equ	0x40025400
GPIOF_GPIOAFSEL	.equ	0x40025420
GPIOF_GPIODEN	.equ	0x4002551c
GPIOF_GPIOLOCK	.equ	0x40025520
GPIOKEY		.equ	0x4c4f434b
GPIOF_GPIOPUR	.equ	0x40025510
GPIOF_GPIOCR	.equ	0x40025524
GPIOF_GPIOAMSEL	.equ	0x40025528
GPIOF_GPIOPCTL	.equ	0x4002552c

;; Initiering av port F
;; Förstör r0, r1, r2
initGPIOF:
	mov r1,#(RCGCGPIO & 0xffff)
	movt r1,#(RCGCGPIO >> 16)
	ldr r0,[r1]
	orr r0,r0,#0x20		; Koppla in GPIO port F
	str r0,[r1]
	nop 			; Vänta lite
	nop
	nop

	mov r1,#(GPIOHBCTL & 0xffff)	; Använd apb för GPIO
	movt r1,#(GPIOHBCTL >> 16)
	ldr r0,[r1]
	mvn r2,#0x2f		; bit 5-0 = 0, övriga = 1
	and r0,r0,r2
	str r0,[r1]

	mov r1,#(GPIOF_GPIOLOCK & 0xffff)
	movt r1,#(GPIOF_GPIOLOCK >> 16)
	mov r0,#(GPIOKEY & 0xffff)
	movt r0,#(GPIOKEY >> 16)
	str r0,[r1]		; Lås upp port F konfigurationsregister

	mov r1,#(GPIOF_GPIOCR & 0xffff)
	movt r1,#(GPIOF_GPIOCR >> 16)
	mov r0,#0x1f		; tillåt konfigurering av alla bitar i porten
	str r0,[r1]

	mov r1,#(GPIOF_GPIOAMSEL & 0xffff)
	movt r1,#(GPIOF_GPIOAMSEL >> 16)
	mov r0,#0x00		; Koppla bort analog funktion
	str r0,[r1]

	mov r1,#(GPIOF_GPIOPCTL & 0xffff)
	movt r1,#(GPIOF_GPIOPCTL >> 16)
	mov r0,#0x00		; använd port F som GPIO
	str r0,[r1]

	mov r1,#(GPIOF_GPIODIR & 0xffff)
	movt r1,#(GPIOF_GPIODIR >> 16)
	mov r0,#0x0e		; styr LED (3 bits), andra bitar är ingångar
	str r0,[r1]

	mov r1,#(GPIOF_GPIOAFSEL & 0xffff)
	movt r1,#(GPIOF_GPIOAFSEL >> 16)
	mov r0,#0		; alla portens bitar är GPIO
	str r0,[r1]

	mov r1,#(GPIOF_GPIOPUR & 0xffff)
	movt r1,#(GPIOF_GPIOPUR >> 16)
	mov r0,#0x11		; svag pull-up för tryckknapparna
	str r0,[r1]

	mov r1,#(GPIOF_GPIODEN & 0xffff)
	movt r1,#(GPIOF_GPIODEN >> 16)
	mov r0,#0xff		; alla pinnar som digital I/O
	str r0,[r1]

	bx lr


;; Initiering av port B
;; Förstör r0, r1
initGPIOB:
	mov r1,#(RCGCGPIO & 0xffff)
	movt r1,#(RCGCGPIO >> 16)
	ldr r0,[r1]
	orr r0,r0,#0x02		; koppla in GPIO port B
	str r0,[r1]
	nop			; vänta lite
	nop
	nop

	mov r1,#(GPIOB_GPIODIR & 0xffff)
	movt r1,#(GPIOB_GPIODIR >> 16)
	mov r0,#0x0		; alla bitar är ingångar
	str r0,[r1]

	mov r1,#(GPIOB_GPIOAFSEL & 0xffff)
	movt r1,#(GPIOB_GPIOAFSEL >> 16)
	mov r0,#0		; alla portens bitar är GPIO
	str r0,[r1]

	mov r1,#(GPIOB_GPIOAMSEL & 0xffff)
	movt r1,#(GPIOB_GPIOAMSEL >> 16)
	mov r0,#0x00		; använd inte analoga funktioner
	str r0,[r1]

	mov r1,#(GPIOB_GPIOPCTL & 0xffff)
	movt r1,#(GPIOB_GPIOPCTL >> 16)
	mov r0,#0x00		; använd inga specialfunktioner på port B	
	str r0,[r1]

	mov r1,#(GPIOB_GPIOPUR & 0xffff)
	movt r1,#(GPIOB_GPIOPUR >> 16)
	mov r0,#0x00		; ingen pullup på port B
	str r0,[r1]

	mov r1,#(GPIOB_GPIODEN & 0xffff)
	movt r1,#(GPIOB_GPIODEN >> 16)
	mov r0,#0xff		; alla pinnar är digital I/O
	str r0,[r1]

	bx lr


;; Utskrift av ett tecken på serieport
;; r0 innehåller tecken att skriva ut (1 byte)
;; returnerar först när tecken skickats
;; förstör r0, r1 och r2 
printchar:
	mov r1,#(UART0_UARTFR & 0xffff)	; peka på serieportens statusregister
	movt r1,#(UART0_UARTFR >> 16)
loop1:
	ldr r2,[r1]			; hämta statusflaggor
	ands r2,r2,#0x20		; kan ytterligare tecken skickas?
	bne loop1			; nej, försök igen
	mov r1,#(UART0_UARTDR & 0xffff)	; ja, peka på serieportens dataregister
	movt r1,#(UART0_UARTDR >> 16)
	str r0,[r1]			; skicka tecken
	bx lr




