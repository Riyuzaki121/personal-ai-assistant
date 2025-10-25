# Personal AI Assistant

A robust personal AI assistant with WhatsApp and Telegram integration, file management, task automation, and API capabilities. Deploy easily in GitHub Codespaces.

## Features

- 🤖 AI-powered conversational assistant
- 📱 WhatsApp integration for messaging
- 💬 Telegram bot support
- 📁 File download and management
- 🔄 Task automation
- 🔒 Secure API configuration
- ☁️ Cloud-ready deployment in Codespaces

## Prerequisites

- GitHub account
- WhatsApp Business API access (or Twilio for WhatsApp)
- Telegram Bot Token (from @BotFather)
- OpenAI API key (or other LLM API)

## Setup Instructions

### 1. Clone Repository in Codespaces

1. Click the green **Code** button on this repository
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for the environment to initialize

### 2. Configure API Keys

Create a `.env` file in the root directory with your API credentials:

```bash
# AI/LLM Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Telegram Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# WhatsApp Configuration (Twilio)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
YOUR_WHATSAPP_NUMBER=whatsapp:+1234567890

# Alternative: WhatsApp Business API
WHATSAPP_API_TOKEN=your_whatsapp_business_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
```

### 3. Install Dependencies

Run in the Codespaces terminal:

```bash
pip install -r requirements.txt
```

### 4. Getting API Credentials

#### Telegram Bot Token
1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow prompts to create your bot
4. Copy the API token provided
5. Get your chat ID by messaging @userinfobot

#### WhatsApp (Twilio)
1. Sign up at [twilio.com](https://www.twilio.com)
2. Get a Twilio phone number with WhatsApp enabled
3. Copy Account SID and Auth Token from dashboard
4. Configure WhatsApp sandbox for testing

#### WhatsApp Business API
1. Apply for WhatsApp Business API access
2. Set up through Meta Business Suite
3. Get access token and phone number ID

#### OpenAI API
1. Sign up at [platform.openai.com](https://platform.openai.com)
2. Navigate to API keys section
3. Create new secret key
4. Copy and save securely

### 5. Run the Assistant

```bash
python main.py
```

## Project Structure

```
personal-ai-assistant/
├── main.py              # Main application entry point
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── handlers/
│   ├── telegram_handler.py
│   ├── whatsapp_handler.py
│   └── ai_handler.py
├── utils/
│   ├── file_manager.py
│   └── task_automation.py
└── README.md
```

## Usage Examples

### Sending Messages via Telegram
```python
from handlers.telegram_handler import send_telegram_message

send_telegram_message("Hello from AI Assistant!")
```

### Sending Messages via WhatsApp
```python
from handlers.whatsapp_handler import send_whatsapp_message

send_whatsapp_message("+1234567890", "Hello from AI!")
```

### Downloading Files
```python
from utils.file_manager import download_file

download_file("https://example.com/file.pdf", "./downloads/")
```

### Task Automation
```python
from utils.task_automation import schedule_task

schedule_task("daily_report", "0 9 * * *")  # Cron format
```

## Deployment in Codespaces

### Keep Codespace Running
1. Set timeout in Codespace settings (default: 30 min)
2. Use `screen` or `tmux` for persistent sessions
3. Consider port forwarding for webhooks

### Port Forwarding for Webhooks
1. In Codespaces, go to **Ports** tab
2. Forward port 8000 (or your app port)
3. Set visibility to **Public** for webhooks
4. Copy forwarded URL for webhook configuration

## Security Best Practices

- ✅ Never commit `.env` file to repository
- ✅ Use GitHub Secrets for production deployments
- ✅ Rotate API keys regularly
- ✅ Implement rate limiting
- ✅ Validate all inputs
- ✅ Use HTTPS for all API calls

## Troubleshooting

### Common Issues

**Bot not responding:**
- Check API tokens are correct
- Verify network connectivity
- Check logs for error messages

**WhatsApp messages failing:**
- Verify Twilio sandbox activation
- Check phone number format
- Ensure sufficient Twilio credits

**File downloads failing:**
- Check download permissions
- Verify URL accessibility
- Check available disk space

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section

---

**Happy Automating! 🚀**
