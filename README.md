# Food Recommendation Quiz

This is an interactive multi-page Flask app for HCDE 310. You answer a few questions that get progressively more specific (taste → dish type → cuisine), and the app recommends what to eat plus real nearby restaurants using the Google Places API

# Instructions on Getting a Google Places API key
1. Go to the Google Cloud Console: https://console.cloud.google.com/
2. Create or select a project
3. Enable billing for the project (required even for the free tier but you won't be charged)
4. Under APIs & Services / Library, enable the Places API
5. Under APIs & Services / Credentials, create an API key
6. Paste the key into `keys.py` as `API_KEY = "your-key-here"`.
