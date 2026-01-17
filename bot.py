from aiohttp import ClientResponseError, ClientSession, ClientTimeout, BasicAuth, CookieJar
from aiohttp_socks import ProxyConnector
from yarl import URL
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import to_hex
from datetime import datetime, timezone
from colorama import *
import asyncio, random, json, re, os, pytz, hashlib, time

wib = pytz.timezone('Asia/Jakarta')

class VeeraBot:
    def __init__(self) -> None:
        self.BASE_API = "https://hub.veerarewards.com"
        self.WEB_ID = "d2c97001-a40d-45b6-b69c-11927e144773"
        self.ORG_ID = "3cf0dde2-04c0-424a-a603-13fcf79e440e"
        self.REF_CODE = "3A0VFM64"
        self.HEADERS = {}
        self.proxies = []
        self.proxy_index = 0
        self.account_proxies = {}
        self.sessions = {}
        self.ua_index = 0
        self.fingerprints = {}
        
        self.USER_AGENTS = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/117.0.0.0",
            "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Brave/1.61.109"
        ]

        self.SCREEN_RESOLUTIONS = ["1920x1080", "1366x768", "1536x864", "1440x900", "1280x720", "2560x1440", "1680x1050", "1600x900"]
        self.TIMEZONES = ["America/New_York", "America/Los_Angeles", "Europe/London", "Europe/Paris", "Asia/Tokyo", "Asia/Singapore", "Australia/Sydney"]

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}", flush=True)

    def welcome(self):
        banner = f"""
{Fore.MAGENTA + Style.BRIGHT}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  {Fore.CYAN}██╗   ██╗███████╗███████╗██████╗  █████╗     ██████╗  ██████╗ ████████╗{Fore.MAGENTA}  ║
║  {Fore.CYAN}██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝{Fore.MAGENTA}  ║
║  {Fore.CYAN}██║   ██║█████╗  █████╗  ██████╔╝███████║    ██████╔╝██║   ██║   ██║   {Fore.MAGENTA}  ║
║  {Fore.CYAN}╚██╗ ██╔╝██╔══╝  ██╔══╝  ██╔══██╗██╔══██║    ██╔══██╗██║   ██║   ██║   {Fore.MAGENTA}  ║
║   {Fore.CYAN}╚████╔╝ ███████╗███████╗██║  ██║██║  ██║    ██████╔╝╚██████╔╝   ██║   {Fore.MAGENTA}  ║
║    {Fore.CYAN}╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   {Fore.MAGENTA}  ║
║                                                               ║
║           {Fore.GREEN + Style.BRIGHT}🚀 Advanced Automation System v2.0 🚀{Fore.MAGENTA + Style.BRIGHT}              ║
║                                                               ║
║  {Fore.YELLOW}Creator:{Fore.WHITE} mejri02                    {Fore.YELLOW}Status:{Fore.GREEN} Active ✓{Fore.MAGENTA}      ║
║  {Fore.YELLOW}Ref Code:{Fore.WHITE} 3A0VFM64                 {Fore.YELLOW}Mode:{Fore.CYAN} Enhanced{Fore.MAGENTA}      ║
║                                                               ║
║  {Fore.RED}⚡ Features: Anti-Detection | Smart Delays | Fingerprinting{Fore.MAGENTA}  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(banner)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_accounts(self):
        filename = "accounts.txt"
        try:
            with open(filename, 'r') as file:
                accounts = [line.strip() for line in file if line.strip()]
            return accounts
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}❌ Failed To Load Accounts: {e}{Style.RESET_ALL}")
            return None

    def load_proxies(self):
        filename = "proxy.txt"
        try:
            if not os.path.exists(filename):
                self.log(f"{Fore.RED + Style.BRIGHT}❌ File {filename} Not Found.{Style.RESET_ALL}")
                return
            with open(filename, 'r') as f:
                self.proxies = [line.strip() for line in f.read().splitlines() if line.strip()]
            
            if not self.proxies:
                self.log(f"{Fore.RED + Style.BRIGHT}❌ No Proxies Found.{Style.RESET_ALL}")
                return

            self.log(f"{Fore.GREEN + Style.BRIGHT}✓ Proxies Loaded:{Style.RESET_ALL}{Fore.YELLOW + Style.BRIGHT} {len(self.proxies)} proxies{Style.RESET_ALL}")
        
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}❌ Failed To Load Proxies: {e}{Style.RESET_ALL}")
            self.proxies = []

    def check_proxy_schemes(self, proxies):
        schemes = ["http://", "https://", "socks4://", "socks5://"]
        if any(proxies.startswith(scheme) for scheme in schemes):
            return proxies
        return f"http://{proxies}"
    
    def get_next_proxy_for_account(self, account):
        if account not in self.account_proxies:
            if not self.proxies:
                return None
            proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
            self.account_proxies[account] = proxy
            self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return self.account_proxies[account]

    def rotate_proxy_for_account(self, account):
        if not self.proxies:
            return None
        proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
        self.account_proxies[account] = proxy
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return proxy
    
    def build_proxy_config(self, proxy=None):
        if not proxy:
            return None, None, None

        if proxy.startswith("socks"):
            connector = ProxyConnector.from_url(proxy)
            return connector, None, None

        elif proxy.startswith("http"):
            match = re.match(r"http://(.*?):(.*?)@(.*)", proxy)
            if match:
                username, password, host_port = match.groups()
                clean_url = f"http://{host_port}"
                auth = BasicAuth(username, password)
                return None, clean_url, auth
            else:
                return None, proxy, None

        raise Exception("Unsupported Proxy Type.")
    
    def generate_fingerprint(self, address: str):
        if address not in self.fingerprints:
            seed = int(hashlib.sha256(address.encode()).hexdigest(), 16)
            random.seed(seed)
            
            self.fingerprints[address] = {
                'user_agent': random.choice(self.USER_AGENTS),
                'screen_resolution': random.choice(self.SCREEN_RESOLUTIONS),
                'timezone': random.choice(self.TIMEZONES),
                'language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'en-US,en;q=0.8']),
                'platform': random.choice(['Win32', 'MacIntel', 'Linux x86_64']),
                'color_depth': random.choice([24, 32]),
                'device_memory': random.choice([4, 8, 16]),
                'hardware_concurrency': random.choice([4, 8, 12, 16])
            }
            
            random.seed()
        
        return self.fingerprints[address]
    
    def initialize_headers(self, address: str):
        if address not in self.HEADERS:
            fingerprint = self.generate_fingerprint(address)
            
            self.HEADERS[address] = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": fingerprint['language'],
                "Cache-Control": "no-cache",
                "Origin": "https://hub.veerarewards.com",
                "Pragma": "no-cache",
                "Referer": "https://hub.veerarewards.com/loyality",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": fingerprint['user_agent'],
                "Sec-Ch-Ua-Platform": f'"{fingerprint["platform"]}"',
                "Sec-Ch-Ua-Mobile": "?0",
                "DNT": "1"
            }
        return self.HEADERS[address]
    
    async def get_session(self, address: str, proxy_url=None, timeout=60):
        if address not in self.sessions:
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            
            cookie_jar = CookieJar(unsafe=True)
            cookie_jar.update_cookies({'referral_code': self.REF_CODE}, URL(self.BASE_API))
            
            session = ClientSession(connector=connector, timeout=ClientTimeout(total=timeout), cookie_jar=cookie_jar)
            
            self.sessions[address] = {'session': session, 'proxy': proxy, 'proxy_auth': proxy_auth}
        
        return self.sessions[address]
    
    async def close_session(self, address: str):
        if address in self.sessions:
            await self.sessions[address]['session'].close()
            del self.sessions[address]
    
    async def close_all_sessions(self):
        for address in list(self.sessions.keys()):
            await self.close_session(address)
        
    def generate_address(self, account: str):
        try:
            account = Account.from_key(account)
            address = account.address
            return address
        except Exception as e:
            return None
    
    async def random_delay(self, min_sec=1.0, max_sec=3.0):
        delay = random.uniform(min_sec, max_sec)
        await asyncio.sleep(delay)
        
    def generate_payload(self, account: str, address: str, csrf_token: str):
        try:
            timestamp_offset = random.randint(0, 999)
            issued_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
            issued_at = issued_at[:-3] + f"{timestamp_offset:03d}Z"

            raw_message = json.dumps({
                "domain": "hub.veerarewards.com",
                "address": address,
                "statement": "Sign in to the app. Powered by Snag Solutions.",
                "uri": "https://hub.veerarewards.com",
                "version": "1",
                "chainId": 1,
                "nonce": csrf_token,
                "issuedAt": issued_at
            }, separators=(',', ':'))

            message = (
                "hub.veerarewards.com wants you to sign in with your Ethereum account:\n"
                f"{address}\n\n"
                "Sign in to the app. Powered by Snag Solutions.\n\n"
                "URI: https://hub.veerarewards.com\n"
                "Version: 1\n"
                "Chain ID: 1\n"
                f"Nonce: {csrf_token}\n"
                f"Issued At: {issued_at}"
            )

            encoded_message = encode_defunct(text=message)
            signed_message = Account.sign_message(encoded_message, private_key=account)
            signature = to_hex(signed_message.signature)

            payload = {
                "message": raw_message,
                "accessToken": signature,
                "signature": signature,
                "walletConnectorName": "MetaMask",
                "walletAddress": address,
                "redirect": "false",
                "callbackUrl": "/protected",
                "chainType": "evm",
                "walletProvider": "undefined",
                "csrfToken": csrf_token,
                "json": "true"
            }

            return payload
        except Exception as e:
            raise Exception(f"Generate Req Payload Failed: {str(e)}")

    def mask_account(self, account):
        try:
            mask_account = account[:6] + '*' * 6 + account[-6:]
            return mask_account
        except Exception as e:
            return None

    def print_question(self):
        print(f"\n{Fore.CYAN + Style.BRIGHT}╔════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}║{Style.RESET_ALL}  {Fore.YELLOW + Style.BRIGHT}⚙️  Configuration Menu{Style.RESET_ALL}              {Fore.CYAN + Style.BRIGHT}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}╚════════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        while True:
            try:
                print(f"{Fore.GREEN + Style.BRIGHT}[1]{Style.RESET_ALL} {Fore.WHITE}🔒 Run With Proxy (Recommended){Style.RESET_ALL}")
                print(f"{Fore.YELLOW + Style.BRIGHT}[2]{Style.RESET_ALL} {Fore.WHITE}⚠️  Run Without Proxy{Style.RESET_ALL}\n")
                proxy_choice = int(input(f"{Fore.MAGENTA + Style.BRIGHT}👉 Choose [1/2] → {Style.RESET_ALL}").strip())

                if proxy_choice in [1, 2]:
                    proxy_type = "With Proxy 🔒" if proxy_choice == 1 else "Without Proxy ⚠️"
                    print(f"\n{Fore.GREEN + Style.BRIGHT}✓ Selected: {proxy_type}{Style.RESET_ALL}\n")
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}❌ Please enter either 1 or 2.{Style.RESET_ALL}\n")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}❌ Invalid input. Enter a number (1 or 2).{Style.RESET_ALL}\n")

        rotate_proxy = False
        if proxy_choice == 1:
            while True:
                rotate_proxy = input(f"{Fore.MAGENTA + Style.BRIGHT}🔄 Rotate Invalid Proxy? [y/n] → {Style.RESET_ALL}").strip().lower()

                if rotate_proxy in ["y", "n"]:
                    rotate_proxy = rotate_proxy == "y"
                    status = "Enabled ✓" if rotate_proxy else "Disabled ✗"
                    print(f"{Fore.CYAN + Style.BRIGHT}Proxy Rotation: {status}{Style.RESET_ALL}\n")
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}❌ Invalid input. Enter 'y' or 'n'.{Style.RESET_ALL}\n")

        return proxy_choice, rotate_proxy
    
    async def ensure_ok(self, response):
        if response.status >= 400:
            error_text = await response.text()
            raise Exception(f"HTTP {response.status}: {error_text}")
    
    async def check_connection(self, address: str, proxy_url=None):
        url = "https://api.ipify.org?format=json"

        try:
            session_info = await self.get_session(address, proxy_url, 15)
            session = session_info['session']
            proxy = session_info['proxy']
            proxy_auth = session_info['proxy_auth']
            
            async with session.get(url=url, proxy=proxy, proxy_auth=proxy_auth) as response:
                await self.ensure_ok(response)
                return True
        except (Exception, ClientResponseError) as e:
            self.log(f"{Fore.CYAN+Style.BRIGHT}Status  :{Style.RESET_ALL}{Fore.RED+Style.BRIGHT} ❌ Connection Failed {Style.RESET_ALL}{Fore.MAGENTA+Style.BRIGHT}→{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} {str(e)[:50]} {Style.RESET_ALL}")
        
        return None
    
    async def auth_csrf(self, address: str, retries=5):
        url = f"{self.BASE_API}/api/auth/csrf"
        
        for attempt in range(retries):
            try:
                await self.random_delay(0.5, 1.5)
                
                session_info = await self.get_session(address)
                session = session_info['session']
                proxy = session_info['proxy']
                proxy_auth = session_info['proxy_auth']

                headers = self.initialize_headers(address)
                headers["Content-Type"] = "application/json"
                
                async with session.get(url=url, headers=headers, proxy=proxy, proxy_auth=proxy_auth) as response:
                    await self.ensure_ok(response)
                    result = await response.json()
                    return result
                    
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(f"{Fore.CYAN+Style.BRIGHT}Status  :{Style.RESET_ALL}{Fore.RED+Style.BRIGHT} ❌ Fetch Nonce Failed {Style.RESET_ALL}{Fore.MAGENTA+Style.BRIGHT}→{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} {str(e)[:50]} {Style.RESET_ALL}")

        return None
    
    async def auth_credentials(self, account: str, address: str, csrf_token: str, retries=5):
        url = f"{self.BASE_API}/api/auth/callback/credentials"
        payload = self.generate_payload(account, address, csrf_token)
        
        for attempt in range(retries):
            try:
                await self.random_delay(1.0, 2.5)
                
                session_info = await self.get_session(address)
                session = session_info['session']
                proxy = session_info['proxy']
                proxy_auth = session_info['proxy_auth']

                headers = self.initialize_headers(address)
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                
                async with session.post(url=url, headers=headers, data=payload, proxy=proxy, proxy_auth=proxy_auth, allow_redirects=False) as response:
                    cookies = session.cookie_jar.filter_cookies(URL(url))
                    if any('session-token' in str(cookie.key) for cookie in cookies.values()):
                        return True
                        
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(f"{Fore.CYAN+Style.BRIGHT}Status  :{Style.RESET_ALL}{Fore.RED+Style.BRIGHT} ❌ Login Failed {Style.RESET_ALL}{Fore.MAGENTA+Style.BRIGHT}→{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} {str(e)[:50]} {Style.RESET_ALL}")

        return None

    async def loyality_account(self, address: str, retries=5):
        url = f"{self.BASE_API}/api/loyalty/accounts?websiteId={self.WEB_ID}&organizationId={self.ORG_ID}&walletAddress={address}"
        
        for attempt in range(retries):
            try:
                await self.random_delay(0.5, 1.5)
                
                session_info = await self.get_session(address)
                session = session_info['session']
                proxy = session_info['proxy']
                proxy_auth = session_info['proxy_auth']

                headers = self.initialize_headers(address)
                
                async with session.get(url=url, headers=headers, proxy=proxy, proxy_auth=proxy_auth) as response:
                    await self.ensure_ok(response)
                    return await response.json()
                    
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(f"{Fore.CYAN+Style.BRIGHT}Balance :{Style.RESET_ALL}{Fore.RED+Style.BRIGHT} ❌ Fetch Points Failed {Style.RESET_ALL}{Fore.MAGENTA+Style.BRIGHT}→{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} {str(e)[:50]} {Style.RESET_ALL}")

        return None
    
    async def complete_checkin(self, address: str, retries=5):
        url = f"{self.BASE_API}/api/loyalty/rules/0c2c81eb-c631-48a8-9f27-a97d192e0039/complete"
        
        for attempt in range(retries):
            try:
                await self.random_delay(1.0, 2.0)
                
                session_info = await self.get_session(address)
                session = session_info['session']
                proxy = session_info['proxy']
                proxy_auth = session_info['proxy_auth']

                headers = self.initialize_headers(address)
                headers["Content-Type"] = "application/json"
                
                async with session.post(url=url, headers=headers, json={}, proxy=proxy, proxy_auth=proxy_auth) as response:
                    if response.status == 400:
                        self.log(f"{Fore.CYAN+Style.BRIGHT}Check-In:{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} ⏭️  Already Claimed Today {Style.RESET_ALL}")
                        return None
                    await self.ensure_ok(response)
                    return await response.json()
                    
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(f"{Fore.CYAN+Style.BRIGHT}Check-In:{Style.RESET_ALL}{Fore.RED+Style.BRIGHT} ❌ Failed {Style.RESET_ALL}{Fore.MAGENTA+Style.BRIGHT}→{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} {str(e)[:50]} {Style.RESET_ALL}")

        return None
    
    async def process_check_connection(self, address: str, use_proxy: bool, rotate_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(address) if use_proxy else None
            if proxy:
                masked_proxy = proxy[:15] + "..." + proxy[-10:] if len(proxy) > 30 else proxy
                self.log(f"{Fore.CYAN+Style.BRIGHT}Proxy   :{Style.RESET_ALL}{Fore.GREEN+Style.BRIGHT} 🔒 {masked_proxy} {Style.RESET_ALL}")
            else:
                self.log(f"{Fore.CYAN+Style.BRIGHT}Proxy   :{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} ⚠️  Direct Connection {Style.RESET_ALL}")

            is_valid = await self.check_connection(address, proxy)
            if is_valid: 
                return True

            if rotate_proxy:
                await self.close_session(address)
                proxy = self.rotate_proxy_for_account(address)
                await asyncio.sleep(1)
                continue

            return False
    
    async def process_user_login(self, account: str, address: str, use_proxy: bool, rotate_proxy: bool):
        is_valid = await self.process_check_connection(address, use_proxy, rotate_proxy)
        if is_valid:
            auth_csrf = await self.auth_csrf(address)
            if not auth_csrf: 
                return False

            csrf_token = auth_csrf.get("csrfToken")

            credentials = await self.auth_credentials(account, address, csrf_token)
            if not credentials: 
                return False

            self.log(f"{Fore.CYAN + Style.BRIGHT}Status  :{Style.RESET_ALL}{Fore.GREEN + Style.BRIGHT} ✅ Login Success {Style.RESET_ALL}")
            return True
        
        return False

    async def process_accounts(self, account: str, address: str, use_proxy: bool, rotate_proxy: bool):
        logined = await self.process_user_login(account, address, use_proxy, rotate_proxy)
        if logined:
            loyality = await self.loyality_account(address)
            if loyality:
                loyality_data = loyality.get("data", [])
                amount = loyality_data[0].get("amount", 0) if loyality_data else 0
                self.log(f"{Fore.CYAN+Style.BRIGHT}Balance :{Style.RESET_ALL}{Fore.YELLOW+Style.BRIGHT} 💰 {amount} Points {Style.RESET_ALL}")

            checkin = await self.complete_checkin(address)
            if checkin:
                self.log(f"{Fore.CYAN+Style.BRIGHT}Check-In:{Style.RESET_ALL}{Fore.GREEN+Style.BRIGHT} ✅ Success {Style.RESET_ALL}")

    async def main(self):
        try:
            accounts = self.load_accounts()
            if not accounts: 
                return

            proxy_choice, rotate_proxy = self.print_question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}{Fore.WHITE + Style.BRIGHT}{len(accounts)}{Style.RESET_ALL}")

                use_proxy = True if proxy_choice == 1 else False
                if use_proxy: 
                    self.load_proxies()

                separator = "=" * 25
                for account in accounts:
                    if account:
                        address = self.generate_address(account)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}{separator}[{Style.RESET_ALL}{Fore.WHITE + Style.BRIGHT} {self.mask_account(address)} {Style.RESET_ALL}{Fore.CYAN + Style.BRIGHT}]{separator}{Style.RESET_ALL}")

                        if not address:
                            self.log(f"{Fore.CYAN + Style.BRIGHT}Status  :{Style.RESET_ALL}{Fore.RED + Style.BRIGHT} ❌ Invalid Private Key {Style.RESET_ALL}")
                            continue
                        
                        await self.process_accounts(account, address, use_proxy, rotate_proxy)
                        await asyncio.sleep(random.uniform(3.0, 6.0))

                await self.close_all_sessions()

                self.log(f"{Fore.CYAN + Style.BRIGHT}={'=' * 72}{Style.RESET_ALL}")
                
                delay = 24 * 60 * 60
                while delay > 0:
                    formatted_time = self.format_seconds(delay)
                    print(f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}{Fore.WHITE+Style.BRIGHT} | {Style.RESET_ALL}{Fore.BLUE+Style.BRIGHT}All Accounts Have Been Processed...{Style.RESET_ALL}", end="\r", flush=True)
                    await asyncio.sleep(1)
                    delay -= 1

        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")
            raise e
        finally:
            await self.close_all_sessions()

if __name__ == "__main__":
    try:
        bot = VeeraBot()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{Fore.RED + Style.BRIGHT}[ EXIT ] Veera BOT by mejri02{Style.RESET_ALL}                                       ")
