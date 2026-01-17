# 🚀 Veera Rewards Auto Bot

Advanced automation bot for Veera Rewards with anti-detection features and smart fingerprinting technology.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Anti-Detection Features](#anti-detection-features)
- [Support](#support)
- [Disclaimer](#disclaimer)

## ✨ Features

- 🔐 **Auto Check-In**: Automatic daily check-in system
- 💰 **Balance Tracking**: Real-time points balance monitoring
- 🎭 **Browser Fingerprinting**: Unique fingerprint per account
- 🔄 **Smart Proxy Rotation**: Automatic proxy switching on failure
- ⏱️ **Random Delays**: Human-like behavior simulation
- 🎨 **Colorful Interface**: Beautiful ASCII art and colored output
- 🛡️ **Anti-Detection**: Advanced evasion techniques
- 📊 **Multi-Account Support**: Manage unlimited accounts
- 🌐 **Proxy Support**: HTTP, HTTPS, SOCKS4, SOCKS5

## 📌 Prerequisites

- Python 3.8 or higher
- Git (for cloning repository)
- Ethereum wallet private keys

## 🔗 Registration

Register on Veera Rewards using the referral link:

👉 **[https://hub.veerarewards.com/loyalty?referral_code=3A0VFM64](https://hub.veerarewards.com/loyalty?referral_code=3A0VFM64)**

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mejri02/veera-bot.git
cd veera-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install aiohttp aiohttp-socks yarl eth-account colorama pytz
```

## ⚙️ Configuration

### 1. Create `accounts.txt`

Create a file named `accounts.txt` in the root directory and add your Ethereum private keys (one per line):

```
0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

### 2. Create `proxy.txt` (Optional)

If you want to use proxies, create a file named `proxy.txt` with your proxies (one per line):

**Supported formats:**
```
http://username:password@ip:port
http://ip:port
socks5://username:password@ip:port
socks5://ip:port
```

**Example:**
```
http://user:pass@123.456.789.0:8080
socks5://198.23.45.67:1080
http://10.0.0.1:3128
```

## 🎮 Usage

### Start the Bot

```bash
python bot.py
```

### Configuration Menu

When you start the bot, you'll see a configuration menu:

```
╔════════════════════════════════════════╗
║  ⚙️  Configuration Menu               ║
╚════════════════════════════════════════╝

[1] 🔒 Run With Proxy (Recommended)
[2] ⚠️  Run Without Proxy

👉 Choose [1/2] →
```

**Option 1**: Run with proxy (recommended for multi-account)
**Option 2**: Run without proxy (direct connection)

If you choose proxy mode, you'll be asked:

```
🔄 Rotate Invalid Proxy? [y/n] →
```

- **y**: Automatically rotate to next proxy if current one fails
- **n**: Stop on failed proxy

### What the Bot Does

1. ✅ **Logs into each account** with unique fingerprint
2. 💰 **Checks current points balance**
3. ✔️ **Completes daily check-in**
4. ⏰ **Waits 24 hours** and repeats

## 🛡️ Anti-Detection Features

### Browser Fingerprinting

Each account gets a unique, deterministic fingerprint:

- **User Agent**: 14 different browser signatures
- **Screen Resolution**: 8 common resolutions
- **Timezone**: 7 different timezones
- **Language**: Multiple language preferences
- **Platform**: Windows, macOS, Linux
- **Hardware**: CPU cores, memory, color depth

### Smart Delays

- Random delays between requests (0.5-2.5 seconds)
- Account processing delays (3-6 seconds)
- Human-like timing patterns

### Request Randomization

- Randomized timestamp offsets
- Unique session cookies per account
- Varied header combinations

## 📊 Output Example

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  ██╗   ██╗███████╗███████╗██████╗  █████╗     ██████╗  ██████╗ ████████╗  ║
║  ██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝  ║
║  ██║   ██║█████╗  █████╗  ██████╔╝███████║    ██████╔╝██║   ██║   ██║     ║
║  ╚██╗ ██╔╝██╔══╝  ██╔══╝  ██╔══██╗██╔══██║    ██╔══██╗██║   ██║   ██║     ║
║   ╚████╔╝ ███████╗███████╗██║  ██║██║  ██║    ██████╔╝╚██████╔╝   ██║     ║
║    ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝     ║
║                                                               ║
║           🚀 Advanced Automation System v2.0 🚀              ║
║                                                               ║
║  Creator: mejri02                    Status: Active ✓        ║
║  Ref Code: 3A0VFM64                 Mode: Enhanced           ║
║                                                               ║
║  ⚡ Features: Anti-Detection | Smart Delays | Fingerprinting  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

[ 01/18/26 10:30:45 WIB ] | Account's Total: 5
[ 01/18/26 10:30:45 WIB ] | ✓ Proxies Loaded: 10 proxies
[ 01/18/26 10:30:45 WIB ] | =========================[0x1234******5678]=========================
[ 01/18/26 10:30:45 WIB ] | Proxy   : 🔒 http://123.456...89.0:8080
[ 01/18/26 10:30:46 WIB ] | Status  : ✅ Login Success
[ 01/18/26 10:30:47 WIB ] | Balance : 💰 1250 Points
[ 01/18/26 10:30:48 WIB ] | Check-In: ✅ Success
```

## 🔧 Troubleshooting

### Common Issues

**"Failed To Load Accounts"**
- Make sure `accounts.txt` exists
- Check that private keys are valid (0x format)

**"Connection Failed"**
- Check your internet connection
- Verify proxy format if using proxies
- Try without proxy first

**"Login Failed"**
- Verify private key is correct
- Check if account is registered on Veera
- Try again after a few minutes

**"Already Claimed Today"**
- Normal behavior, check-in is once per 24 hours
- Bot will wait and try again tomorrow

## 📝 Files Structure

```
veera-bot/
├── bot.py              # Main bot script
├── accounts.txt        # Your private keys (create this)
├── proxy.txt           # Your proxies (optional)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔐 Security Notes

- Never share your `accounts.txt` file
- Keep your private keys secure
- Use proxies for better anonymity
- The bot stores no data externally

## ⚠️ Disclaimer

This bot is for educational purposes only. Use at your own risk. The author is not responsible for:

- Account bans or restrictions
- Loss of funds or points
- Any violations of Veera Rewards terms of service

Always ensure you're complying with the platform's terms and conditions.

## 🤝 Support

If you find this bot helpful, please:

- ⭐ Star this repository
- 🔗 Use the referral link: [https://hub.veerarewards.com/loyalty?referral_code=3A0VFM64](https://hub.veerarewards.com/loyalty?referral_code=3A0VFM64)
- 🐛 Report bugs via GitHub Issues

## 👨‍💻 Developer

**mejri02**

- GitHub: [@mejri02](https://github.com/mejri02)
- Referral Code: `3A0VFM64`

## 📜 License

MIT License - feel free to use and modify as needed.

---

Made with ❤️ by mejri02

**Happy Farming! 🌾**
