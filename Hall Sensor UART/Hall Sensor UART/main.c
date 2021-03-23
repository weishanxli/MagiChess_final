/*
 * Hall Sensor UART.c
 *
 * Created: 3/18/2021 3:20:48 PM
 * Author : Sam Klein
 */ 


#define F_CPU 16000000

#include <util/delay.h>
#include <avr/io.h>

//#define Mux0 PD6
#define Mux0 6
//#define Mux1 PD7
#define Mux2 PB0
#define Mux3 PB1
#define Mux4 PC0
#define Mux5 PC1
#define Mux6 PC2
#define Mux7 PC3

#define A PD2
#define B PD3
#define C PD4

void USART_Transmit(uint8_t data)
{

	_delay_ms(1);
	/* Wait for empty transmit buffer */
	while ( !( UCSR0A & (1<<UDRE0)) );
	/* Put data into buffer, sends the data */
	UDR0 = data;
}

/*
* Function Name : USART_Receive
 * Description: Returns the received parameters from UART
 * Input Parameters : NONE
 * Return value: 8-bit data received from UART
 */
int USART_Receive(void){
	while ( !(UCSR0A & (1<<RXC0)) ){}
	/* Get and return received data from buffer */
	return UDR0;
	
}

void USART_init(void){
	
	//DISABLE POWER REDUCTION FOR USART
	PRR &= ~( 1 << PRUSART0);
	/*Set baud rate */
	//9600 for 16MHz clock
	UBRR0L = 0b01100111;
	
	/*Enable receiver and transmitter //and Receive INterrupt*/
	UCSR0B = (1<<RXEN0)|(1<<TXEN0);//|(1<<RXCIE0);
	/* 8-bit data */
	UCSR0C = (3<<UCSZ00);
}

void MuxInit(void) 
{
	DDRD |= (1<<A);
	DDRD |= (1<<B);
	DDRD |= (1<<C);
	
	DDRD &= ~(1<<Mux0);
	//DDRD &= ~(1<<Mux1);
	DDRB &= ~(1<<Mux2);
	DDRB &= ~(1<<Mux3);
	DDRC &= ~(1<<Mux4);
	DDRC &= ~(1<<Mux5);
	DDRC &= ~(1<<Mux6);
	DDRC &= ~(1<<Mux7);
}

void SetABC(uint8_t row)
{
	if((row >> 2) & 1) {
		PORTD |= (1<<C);
	} else {
		PORTD &= ~(1<<C);
	}
	
	if((row >> 1) & 1) {
		PORTD |= (1<<B);
	} else {
		PORTD &= ~(1<<B);
	}
	
	if((row >> 0) & 1) {
		PORTD |= (1<<A);
	} else {
		PORTD &= ~(1<<A);
	}
}

uint8_t GatherMuxData(uint8_t Mux)
{
	if(Mux == 0) {
		Mux = Mux0;
	} else if(Mux == 1) {
		Mux = Mux0;
	} else if(Mux == 2) {
		Mux = Mux2;
	} else if(Mux == 3) {
		Mux = Mux3;
	} else if(Mux == 4) {
		Mux = Mux4;
	} else if(Mux == 5) {
		Mux = Mux5;
	} else if(Mux == 6) {
		Mux = Mux6;
	} else {
		Mux = Mux7;
	} 
	
	uint8_t MuxData = 0x00;
	for (uint8_t i = 0; i < 8; i++) {
		SetABC(i);
		PIND |= (1<<6);
		if(bit_is_clear(PIND,PD6)) {
			MuxData |= (1<<i);
		}
	}
	return MuxData;
}

uint8_t GatherMuxData2(uint8_t Mux)
{
	Mux = Mux0;
	
	PORTD &= ~(1<<C);
	
	return Mux;
}

void SendData(uint8_t Byte1, uint8_t Byte2)
{
	USART_Transmit(Byte1);
	USART_Transmit(Byte2);
}

int main(void)
{
	
	MuxInit();
	
	//PORTD |= (1<<A);
	//PORTD |= (1<<B);
	//PORTD |= (1<<C);
	
	
	//uint8_t UART_lastRecievedByte;
	USART_init();
    while (1) 
    {
		//UART_lastRecievedByte = USART_Receive();
		
		//uint8_t MD0 = GatherMuxData(0);
		
		//PIND |= (1<<Mux0);
		
		uint8_t MD0 = GatherMuxData(0);
		
		//PIND |= (1<<6);
		
		//PORTD &= ~(1<<C);
		//PORTD &= ~(1<<B);
		//PORTD &= ~(1<<A);
				
		//if(bit_is_clear(PIND,Mux0)) {
		//if ((PIND & (1<<Mux0))) {

			//MD0 = 0xFF;
		//}
		
// 		PORTD |= (1<<C);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<1);
// 		}
// 		
// 		PORTD &= ~(1<<C);
// 		PORTD |= (1<<B);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<2);
// 		}
// 		
// 		PORTD |= (1<<C);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<3);
// 		}
// 		
// 		PORTD &= ~(1<<C);
// 		PORTD &= ~(1<<B);
// 		PORTD |= (1<<A);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<4);
// 		}
// 		
// 		PORTD |= (1<<C);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<5);
// 		}
// 		
// 		PORTD &= ~(1<<C);
// 		PORTD |= (1<<B);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<6);
// 		}
// 		
// 		PORTD |= (1<<C);
// 		
// 		//if(bit_is_clear(PIND,Mux0)) {
// 		if ((PIND & (1<<Mux0))) {
// 			MD0 |= (1<<7);
// 		}
		
		//Sending UART message 0xF0
		USART_Transmit(MD0);
    }
}

