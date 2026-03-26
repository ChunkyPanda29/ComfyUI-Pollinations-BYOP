"""
BYOP (Bring Your Own Pollen) Authentication Module
Implements the official Pollinations BYOP device code flow for headless/CLI apps
Reference: https://github.com/pollinations/pollinations/blob/main/BRING_YOUR_OWN_POLLEN.md
"""

import requests
import time
import json
import os
from typing import Optional, Dict, Any

# Default app key for attribution (users can override with their own)
# Create one at enter.pollinations.ai for proper branding on consent screen
DEFAULT_APP_KEY = "pk_iMLHCKZ31UTDgWQr"  # comfyui_byop app key

class BYOPAuth:
    """
    Handles BYOP authentication flows:
    - Device Code Flow (for headless/CLI - no browser needed)
    - User Info retrieval
    - App Key attribution
    """
    
    BASE_URL = "https://enter.pollinations.ai"
    
    def __init__(self, app_key: Optional[str] = None):
        """
        Initialize BYOP Auth.
        
        Args:
            app_key: Optional publishable key for attribution.
                    Without it: consent screen shows generic hostname
                    With it: consent screen shows your app name + GitHub
        """
        self.app_key = app_key or DEFAULT_APP_KEY
        self.session = requests.Session()
    
    def request_device_code(self, scope: str = "generate") -> Dict[str, Any]:
        """
        Step 1: Request a device code for CLI/headless auth.
        
        Returns:
            {
                "device_code": "...",      # For polling
                "user_code": "ABCD-1234",  # Show this to user
                "verification_uri": "/device",  # Where to enter code
                "expires_in": 1800,
                "interval": 5
            }
        """
        response = self.session.post(
            f"{self.BASE_URL}/api/device/code",
            headers={"Content-Type": "application/json"},
            json={
                "client_id": self.app_key,  # App key for attribution
                "scope": scope  # "generate", "profile", "balance", etc.
            }
        )
        response.raise_for_status()
        return response.json()
    
    def poll_for_token(self, device_code: str, interval: int = 5, 
                       max_attempts: int = 60) -> Optional[str]:
        """
        Step 2: Poll for the access token after user authorizes.
        
        Args:
            device_code: From request_device_code()
            interval: Seconds between polls (default 5)
            max_attempts: Max polling attempts (default 60 = 5 min)
            
        Returns:
            API key (sk_...) or None if expired/cancelled
        """
        for attempt in range(max_attempts):
            response = self.session.post(
                f"{self.BASE_URL}/api/device/token",
                headers={"Content-Type": "application/json"},
                json={"device_code": device_code}
            )
            
            data = response.json()
            
            # Success!
            if "access_token" in data:
                return data["access_token"]
            
            # Pending - user hasn't authorized yet
            if data.get("error") == "authorization_pending":
                time.sleep(interval)
                continue
            
            # Other errors (expired, rejected, etc.)
            if "error" in data:
                print(f"BYOP Auth error: {data.get('error_description', data['error'])}")
                return None
        
        print("BYOP Auth: Polling timeout (user took too long)")
        return None
    
    def get_user_info(self, api_key: str) -> Optional[Dict[str, Any]]:
        """
        Get user profile info from an API key.
        
        Args:
            api_key: The user's API key (sk_...)
            
        Returns:
            {
                "sub": "user-id",
                "name": "Thomas",
                "preferred_username": "voodoohop",
                "email": "...",
                "picture": "...",
                "balance": 100
            }
        """
        try:
            response = self.session.get(
                f"{self.BASE_URL}/api/device/userinfo",
                headers={"Authorization": f"Bearer {api_key}"}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Failed to get user info: {e}")
            return None
    
    def authenticate_interactive(self) -> Optional[str]:
        """
        Full interactive device flow - prompts user in terminal.
        
        Returns:
            API key if successful, None otherwise
        """
        print("\n🔐 BYOP Authentication")
        print("=" * 50)
        print("Getting authorization code...")
        
        try:
            device_data = self.request_device_code()
            user_code = device_data["user_code"]
            device_code = device_data["device_code"]
            interval = device_data.get("interval", 5)
            
            print(f"\n📱 Go to: https://enter.pollinations.ai{device_data['verification_uri']}")
            print(f"🔑 Enter code: {user_code}")
            print("\n⏳ Waiting for authorization...")
            
            api_key = self.poll_for_token(device_code, interval)
            
            if api_key:
                # Get user info to confirm
                user_info = self.get_user_info(api_key)
                if user_info:
                    name = user_info.get('name', user_info.get('preferred_username', 'User'))
                    balance = user_info.get('balance', 'unknown')
                    print(f"\n✅ Authenticated as: {name}")
                    print(f💰 Balance: {balance} Pollen")
                return api_key
            else:
                print("\n❌ Authentication failed or timed out")
                return None
                
        except Exception as e:
            print(f"\n❌ Authentication error: {e}")
            return None


# Convenience function for quick auth
def byop_login(app_key: Optional[str] = None) -> Optional[str]:
    """
    Quick interactive BYOP login.
    
    Example:
        api_key = byop_login()
        if api_key:
            # Save to config, use in nodes
            pass
    """
    auth = BYOPAuth(app_key)
    return auth.authenticate_interactive()


if __name__ == "__main__":
    # Test the flow
    key = byop_login()
    if key:
        print(f"\nAPI Key: {key[:20]}...")
