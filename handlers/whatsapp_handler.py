"""WhatsApp Handler for Personal AI Assistant"""
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from loguru import logger

class WhatsAppHandler:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_number = os.getenv('TWILIO_WHATSAPP_FROM', 'whatsapp:+14155238886')
        
        if not self.account_sid or not self.auth_token:
            raise ValueError("Twilio credentials not found in environment variables")
        
        self.client = Client(self.account_sid, self.auth_token)
        logger.info("WhatsApp Handler initialized successfully")
    
    def send_message(self, to_number: str, message: str) -> bool:
        """Send WhatsApp message via Twilio"""
        try:
            if not to_number.startswith('whatsapp:'):
                to_number = f'whatsapp:{to_number}'
            
            message_obj = self.client.messages.create(
                from_=self.from_number,
                body=message,
                to=to_number
            )
            
            logger.info(f"WhatsApp message sent: {message_obj.sid}")
            return True
        except Exception as e:
            logger.error(f"Failed to send WhatsApp message: {e}")
            return False
    
    def send_media(self, to_number: str, message: str, media_url: str) -> bool:
        """Send WhatsApp message with media attachment"""
        try:
            if not to_number.startswith('whatsapp:'):
                to_number = f'whatsapp:{to_number}'
            
            message_obj = self.client.messages.create(
                from_=self.from_number,
                body=message,
                media_url=[media_url],
                to=to_number
            )
            
            logger.info(f"WhatsApp media message sent: {message_obj.sid}")
            return True
        except Exception as e:
            logger.error(f"Failed to send WhatsApp media: {e}")
            return False
    
    def handle_incoming(self, request_data: dict) -> str:
        """Handle incoming WhatsApp messages"""
        try:
            from_number = request_data.get('From', '')
            message_body = request_data.get('Body', '')
            
            logger.info(f"Received WhatsApp message from {from_number}: {message_body}")
            
            # Create response
            response = MessagingResponse()
            
            # Echo back the message (customize based on your needs)
            reply = f"Received your message: {message_body}"
            response.message(reply)
            
            return str(response)
        except Exception as e:
            logger.error(f"Error handling incoming WhatsApp message: {e}")
            response = MessagingResponse()
            response.message("Sorry, an error occurred processing your message.")
            return str(response)
